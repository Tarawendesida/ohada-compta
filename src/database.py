import sqlite3
import os
from datetime import datetime
from pathlib import Path


class Database:
    def __init__(self, db_path=None):
        if db_path is None:
            db_path = os.path.join(os.path.expanduser("~"), "OHADA-Compta", "comptabilite.db")
        self.db_path = db_path
        os.makedirs(os.path.dirname(db_path), exist_ok=True)
        self.conn = sqlite3.connect(db_path, check_same_thread=False)
        self.cursor = self.conn.cursor()
        self.cursor.execute("PRAGMA foreign_keys = ON")

    def execute(self, query, params=None):
        if params:
            return self.cursor.execute(query, params)
        else:
            return self.cursor.execute(query)

    def fetchone(self):
        return self.cursor.fetchone()

    def fetchall(self):
        return self.cursor.fetchall()

    def commit(self):
        self.conn.commit()

    def close(self):
        self.conn.close()

    # ================================================================
    # TABLE CREATION
    # ================================================================

    def create_tables(self):
        """Create all required tables."""
        self.execute("""CREATE TABLE IF NOT EXISTS entreprise (
            id INTEGER PRIMARY KEY, raison_sociale TEXT NOT NULL,
            sigle TEXT, pays TEXT, forme_juridique TEXT,
            systeme_comptable TEXT, capital REAL,
            nif TEXT, rccm TEXT, cnps TEXT,
            adresse TEXT, ville TEXT, telephone TEXT, email TEXT,
            debut_exercice TEXT, fin_exercice TEXT, regime_fiscal TEXT,
            date_creation TIMESTAMP DEFAULT CURRENT_TIMESTAMP)""")
        self.execute("""CREATE TABLE IF NOT EXISTS journaux (
            id INTEGER PRIMARY KEY, code TEXT UNIQUE NOT NULL,
            libelle TEXT NOT NULL, type TEXT)""")
        self.execute("""CREATE TABLE IF NOT EXISTS ecritures (
            id INTEGER PRIMARY KEY, date_ecriture TEXT NOT NULL,
            journal_id INTEGER, numero_ecriture TEXT, libelle TEXT, ref_piece TEXT,
            date_saisie TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY(journal_id) REFERENCES journaux(id))""")
        self.execute("""CREATE TABLE IF NOT EXISTS lignes_ecritures (
            id INTEGER PRIMARY KEY, ecriture_id INTEGER NOT NULL,
            numero_compte TEXT NOT NULL, libelle_compte TEXT,
            debit REAL DEFAULT 0, credit REAL DEFAULT 0, ref_piece TEXT,
            FOREIGN KEY(ecriture_id) REFERENCES ecritures(id))""")
        self.execute("""CREATE TABLE IF NOT EXISTS comptes (
            id INTEGER PRIMARY KEY, numero TEXT UNIQUE NOT NULL,
            libelle TEXT NOT NULL, classe INTEGER, type TEXT, sens TEXT)""")
        self.commit()

    def init_database(self):
        """Initialize the database: create tables + indexes + default journals."""
        self.create_tables()
        self._create_indexes()
        self._create_default_journaux()

    def _create_indexes(self):
        for idx in [
            "CREATE INDEX IF NOT EXISTS idx_ecritures_date ON ecritures(date_ecriture)",
            "CREATE INDEX IF NOT EXISTS idx_ecritures_journal ON ecritures(journal_id)",
            "CREATE INDEX IF NOT EXISTS idx_lignes_compte ON lignes_ecritures(numero_compte)",
            "CREATE INDEX IF NOT EXISTS idx_lignes_ecriture ON lignes_ecritures(ecriture_id)",
        ]:
            try:
                self.execute(idx)
            except Exception:
                pass

    def _create_default_journaux(self):
        """Seed default journals if none exist."""
        self.execute("SELECT COUNT(*) FROM journaux")
        if self.fetchone()[0] == 0:
            for code, libelle, type_j in [
                ("VT", "Ventes", "Ventes"), ("AC", "Achats", "Achats"),
                ("BQ", "Banque", "Tresorerie"), ("CA", "Caisse", "Tresorerie"),
                ("OD", "Operations Diverses", "Divers"),
            ]:
                self.execute(
                    "INSERT OR IGNORE INTO journaux (code, libelle, type) VALUES (?, ?, ?)",
                    (code, libelle, type_j))
            self.commit()

    # ================================================================
    # WRITE METHODS
    # ================================================================

    def create_entreprise(self, raison_sociale, pays, forme_juridique,
                          systeme_comptable="SYSCOHADA", capital=0,
                          sigle=None, nif=None, rccm=None, cnps=None,
                          adresse=None, ville=None, telephone=None, email=None,
                          debut_exercice=None, fin_exercice=None, regime_fiscal=None):
        """Insert a new company. Returns the new row id."""
        self.execute("""INSERT INTO entreprise
            (raison_sociale, sigle, pays, forme_juridique, systeme_comptable, capital,
             nif, rccm, cnps, adresse, ville, telephone, email,
             debut_exercice, fin_exercice, regime_fiscal)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""",
            (raison_sociale, sigle, pays, forme_juridique, systeme_comptable, capital,
             nif, rccm, cnps, adresse, ville, telephone, email,
             debut_exercice, fin_exercice, regime_fiscal))
        self.commit()
        return self.cursor.lastrowid

    def update_entreprise(self, entreprise_id, **fields):
        """Update company fields by id."""
        allowed = {
            "raison_sociale", "sigle", "pays", "forme_juridique", "systeme_comptable",
            "capital", "nif", "rccm", "cnps", "adresse", "ville", "telephone", "email",
            "debut_exercice", "fin_exercice", "regime_fiscal",
        }
        updates = {k: v for k, v in fields.items() if k in allowed}
        if not updates:
            return
        set_clause = ", ".join(f"{k} = ?" for k in updates)
        values = list(updates.values()) + [entreprise_id]
        self.execute(f"UPDATE entreprise SET {set_clause} WHERE id = ?", values)
        self.commit()

    def create_journal(self, code, libelle, type_journal=None):
        """Insert a new journal. Returns id."""
        self.execute(
            "INSERT OR IGNORE INTO journaux (code, libelle, type) VALUES (?, ?, ?)",
            (code, libelle, type_journal))
        self.commit()
        return self.cursor.lastrowid

    def create_ecriture(self, date_ecriture, journal_id, libelle, lignes,
                        numero_ecriture=None, ref_piece=None):
        """Insert a balanced journal entry with lines. Raises ValueError if unbalanced."""
        total_debit = sum(l.get("debit", 0) or 0 for l in lignes)
        total_credit = sum(l.get("credit", 0) or 0 for l in lignes)
        if abs(total_debit - total_credit) > 0.01:
            raise ValueError(
                f"Ecriture desequilibree: debit={total_debit:,.0f} credit={total_credit:,.0f}")
        self.execute("""INSERT INTO ecritures
            (date_ecriture, journal_id, numero_ecriture, libelle, ref_piece)
            VALUES (?, ?, ?, ?, ?)""",
            (str(date_ecriture), journal_id, numero_ecriture, libelle, ref_piece))
        ecriture_id = self.cursor.lastrowid
        for ligne in lignes:
            self.execute("""INSERT INTO lignes_ecritures
                (ecriture_id, numero_compte, libelle_compte, debit, credit, ref_piece)
                VALUES (?, ?, ?, ?, ?, ?)""",
                (ecriture_id, ligne["numero_compte"], ligne.get("libelle_compte", ""),
                 ligne.get("debit", 0) or 0, ligne.get("credit", 0) or 0,
                 ligne.get("ref_piece")))
        self.commit()
        return ecriture_id

    def init_plan_comptable(self, plan_comptable):
        """Bulk insert chart of accounts. Skips duplicates."""
        for compte in plan_comptable:
            self.execute("""INSERT OR IGNORE INTO comptes (numero, libelle, classe, type, sens)
                VALUES (?, ?, ?, ?, ?)""",
                (str(compte["numero"]), compte["libelle"],
                 compte.get("classe", 0), compte.get("type", ""), compte.get("sens", "")))
        self.commit()

    def delete_entreprise(self, entreprise_id):
        self.execute("DELETE FROM entreprise WHERE id = ?", (entreprise_id,))
        self.commit()

    # ================================================================
    # READ METHODS
    # ================================================================

    def get_entreprise_active(self):
        try:
            self.execute("SELECT * FROM entreprise LIMIT 1")
            return self.fetchone()
        except Exception:
            return None

    def get_all_entreprises(self):
        try:
            self.execute("SELECT * FROM entreprise")
            return self.fetchall()
        except Exception:
            return []

    def get_journaux(self):
        try:
            self.execute("SELECT * FROM journaux ORDER BY code")
            return self.fetchall()
        except Exception:
            return []

    def get_plan_comptable(self):
        try:
            self.execute("SELECT * FROM comptes ORDER BY numero")
            return self.fetchall()
        except Exception:
            return []

    def get_ecritures(self, limit=None):
        try:
            query = "SELECT * FROM ecritures ORDER BY date_ecriture DESC"
            if limit:
                query += f" LIMIT {int(limit)}"
            self.execute(query)
            return self.fetchall()
        except Exception:
            return []

    def get_ecritures_by_journal(self, journal_id):
        try:
            self.execute(
                "SELECT * FROM ecritures WHERE journal_id = ? ORDER BY date_ecriture DESC",
                (journal_id,))
            return self.fetchall()
        except Exception:
            return []

    def get_lignes_ecriture(self, ecriture_id):
        try:
            self.execute(
                "SELECT * FROM lignes_ecritures WHERE ecriture_id = ?", (ecriture_id,))
            return self.fetchall()
        except Exception:
            return []

    def get_balance(self):
        try:
            self.execute("""SELECT l.numero_compte, c.libelle,
                SUM(CASE WHEN l.debit > 0 THEN l.debit ELSE 0 END) as total_debit,
                SUM(CASE WHEN l.credit > 0 THEN l.credit ELSE 0 END) as total_credit,
                SUM(CASE WHEN l.debit > 0 THEN l.debit ELSE 0 END)
                  - SUM(CASE WHEN l.credit > 0 THEN l.credit ELSE 0 END) as solde
                FROM lignes_ecritures l LEFT JOIN comptes c ON l.numero_compte = c.numero
                GROUP BY l.numero_compte, c.libelle ORDER BY l.numero_compte""")
            return self.fetchall()
        except Exception:
            return []

    def get_grand_livre(self, numero_compte):
        try:
            self.execute("""SELECT e.date_ecriture, e.libelle, l.debit, l.credit, c.libelle
                FROM lignes_ecritures l JOIN ecritures e ON l.ecriture_id = e.id
                LEFT JOIN comptes c ON l.numero_compte = c.numero
                WHERE l.numero_compte = ? ORDER BY e.date_ecriture""", (numero_compte,))
            return self.fetchall()
        except Exception:
            return []

    def get_compte_resultat(self):
        """Income statement from real data."""
        try:
            self.execute("""SELECT c.numero, c.libelle,
                SUM(CASE WHEN l.credit > 0 THEN l.credit ELSE 0 END) as total
                FROM comptes c LEFT JOIN lignes_ecritures l ON c.numero = l.numero_compte
                WHERE c.classe = 7 GROUP BY c.numero, c.libelle ORDER BY c.numero""")
            produits = self.fetchall()
            self.execute("""SELECT c.numero, c.libelle,
                SUM(CASE WHEN l.debit > 0 THEN l.debit ELSE 0 END) as total
                FROM comptes c LEFT JOIN lignes_ecritures l ON c.numero = l.numero_compte
                WHERE c.classe = 6 GROUP BY c.numero, c.libelle ORDER BY c.numero""")
            charges = self.fetchall()
            return {"produits": produits, "charges": charges}
        except Exception:
            return {"produits": [], "charges": []}

    def get_bilan(self):
        """Balance sheet from real data."""
        try:
            self.execute("""SELECT c.numero, c.libelle,
                SUM(CASE WHEN l.debit > 0 THEN l.debit WHEN l.credit > 0 THEN -l.credit ELSE 0 END) as solde
                FROM comptes c LEFT JOIN lignes_ecritures l ON c.numero = l.numero_compte
                WHERE c.classe IN (2, 3, 4, 5)
                GROUP BY c.numero, c.libelle HAVING solde > 0 ORDER BY c.classe, c.numero""")
            actif = self.fetchall()
            self.execute("""SELECT c.numero, c.libelle,
                SUM(CASE WHEN l.credit > 0 THEN l.credit WHEN l.debit > 0 THEN -l.debit ELSE 0 END) as solde
                FROM comptes c LEFT JOIN lignes_ecritures l ON c.numero = l.numero_compte
                WHERE c.classe IN (1)
                GROUP BY c.numero, c.libelle HAVING solde > 0 ORDER BY c.classe, c.numero""")
            passif = self.fetchall()
            return {"actif": actif, "passif": passif}
        except Exception:
            return {"actif": [], "passif": []}

    def count_ecritures(self):
        try:
            self.execute("SELECT COUNT(*) FROM ecritures")
            return self.fetchone()[0]
        except Exception:
            return 0


_db_instance = None


def get_database():
    global _db_instance
    if _db_instance is None:
        _db_instance = Database()
        _db_instance.init_database()
    return _db_instance
