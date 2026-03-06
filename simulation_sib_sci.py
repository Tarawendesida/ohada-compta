#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
SIMULATION COMPTABLE - SIB-SCI
Société Immobilière de Bâtiment - Société Civile Immobilière
Simulation pour 1 année (2025)

Données:
- Capital initial: 300 000 000 FCFA
- Créances clients: 100 000 000 FCFA
- 132 locaux
- Loyer mensuel: 25 000 000 FCFA (total 300 000 000 FCFA/an)
"""

import sys
import sqlite3
from datetime import datetime, timedelta
from pathlib import Path
from decimal import Decimal

# Configuration de la BD
db_path = Path.home() / "OHADA-Compta" / "comptabilite.db"
db_path.parent.mkdir(exist_ok=True)

def create_connection():
    """Créer une connexion à la base de données"""
    conn = sqlite3.connect(str(db_path))
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    cursor.execute("PRAGMA foreign_keys = ON")
    return conn, cursor

def init_database(cursor, conn):
    """Initialiser la structure de la base de données"""
    
    # Table entreprise
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS entreprise (
            id INTEGER PRIMARY KEY,
            raison_sociale TEXT NOT NULL,
            sigle TEXT,
            pays TEXT,
            forme_juridique TEXT,
            systeme_comptable TEXT,
            capital REAL,
            nif TEXT,
            rccm TEXT,
            cnps TEXT,
            adresse TEXT,
            ville TEXT,
            telephone TEXT,
            email TEXT,
            debut_exercice TEXT,
            fin_exercice TEXT,
            regime_fiscal TEXT,
            date_creation TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)
    
    # Table journaux
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS journaux (
            id INTEGER PRIMARY KEY,
            code TEXT UNIQUE NOT NULL,
            libelle TEXT NOT NULL,
            type TEXT
        )
    """)
    
    # Table écritures
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS ecritures (
            id INTEGER PRIMARY KEY,
            date_ecriture TEXT NOT NULL,
            journal_id INTEGER,
            numero_ecriture TEXT,
            libelle TEXT,
            ref_piece TEXT,
            date_saisie TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY(journal_id) REFERENCES journaux(id)
        )
    """)
    
    # Table lignes écritures
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS lignes_ecritures (
            id INTEGER PRIMARY KEY,
            ecriture_id INTEGER NOT NULL,
            numero_compte TEXT NOT NULL,
            libelle_compte TEXT,
            debit REAL DEFAULT 0,
            credit REAL DEFAULT 0,
            ref_piece TEXT,
            FOREIGN KEY(ecriture_id) REFERENCES ecritures(id)
        )
    """)
    
    # Table comptes
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS comptes (
            id INTEGER PRIMARY KEY,
            numero TEXT UNIQUE NOT NULL,
            libelle TEXT NOT NULL,
            classe INTEGER,
            type TEXT,
            sens TEXT
        )
    """)
    
    conn.commit()
    print("[OK] Structure de la base de donnees initialisee")

def insert_entreprise(cursor, conn):
    """Insérer les données de l'entreprise"""
    
    cursor.execute("""
        DELETE FROM entreprise
    """)
    
    cursor.execute("""
        INSERT INTO entreprise 
        (raison_sociale, sigle, pays, forme_juridique, systeme_comptable, capital,
         nif, rccm, cnps, adresse, ville, telephone, email, 
         debut_exercice, fin_exercice, regime_fiscal)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        "SIB-SCI - Société Immobilière de Bâtiment",
        "SIB-SCI",
        "CI",  # Côte d'Ivoire
        "SCI",  # Société Civile Immobilière
        "SYCEBNL",  # Non lucratif
        300000000,
        "CI-SCI-2025-NIF",
        "CI-ABJ-2025-A-12345",
        "CI-2025-CNPS-12345",
        "Plateau - Abidjan",
        "Abidjan",
        "+225 22 50 50 50",
        "contact@sib-sci.com",
        "2025-01-01",
        "2025-12-31",
        "RN"  # Régime Normal
    ))
    
    conn.commit()
    print("[OK] Entreprise SIB-SCI creee")

def insert_journaux(cursor, conn):
    """Insérer les journaux comptables"""
    
    journaux = [
        ("VT", "Ventes", "Ventes"),
        ("AC", "Achats", "Achats"),
        ("BQ", "Banque", "Trésorerie"),
        ("CA", "Caisse", "Trésorerie"),
        ("OD", "Opérations Diverses", "Divers"),
    ]
    
    for code, libelle, type_journal in journaux:
        cursor.execute("""
            INSERT OR IGNORE INTO journaux (code, libelle, type)
            VALUES (?, ?, ?)
        """, (code, libelle, type_journal))
    
    conn.commit()
    print("[OK] Journaux comptables crees")

def insert_comptes(cursor, conn):
    """Insérer le plan comptable simplifié"""
    
    comptes = [
        # Classe 1: Ressources durables
        ("101", "Capital social", 1, "Bilan", "Crédit"),
        ("121", "Report à nouveau", 1, "Bilan", "Crédit"),
        
        # Classe 2: Actif immobilisé
        ("211", "Bâtiments", 2, "Bilan", "Débit"),
        ("2811", "Amortissement bâtiments", 2, "Bilan", "Crédit"),
        
        # Classe 3: Stocks (non applicable ici)
        
        # Classe 4: Tiers
        ("401", "Clients", 4, "Bilan", "Débit"),
        ("4011", "Créances clients", 4, "Bilan", "Débit"),
        ("411", "Fournisseurs", 4, "Bilan", "Crédit"),
        
        # Classe 5: Trésorerie
        ("512", "Banque", 5, "Bilan", "Débit"),
        ("581", "Caisse", 5, "Bilan", "Débit"),
        
        # Classe 6: Charges
        ("601", "Achats", 6, "Résultat", "Débit"),
        ("613", "Électricité", 6, "Résultat", "Débit"),
        ("614", "Eau", 6, "Résultat", "Débit"),
        ("6181", "Frais d'entretien", 6, "Résultat", "Débit"),
        ("6182", "Frais de gardiennage", 6, "Résultat", "Débit"),
        ("621", "Services du personnel", 6, "Résultat", "Débit"),
        ("622", "Rémunérations du personnel", 6, "Résultat", "Débit"),
        ("6311", "Frais de transport", 6, "Résultat", "Débit"),
        ("6314", "Frais de poste", 6, "Résultat", "Débit"),
        ("6326", "Honoraires", 6, "Résultat", "Débit"),
        ("6351", "Assurances", 6, "Résultat", "Débit"),
        ("6352", "Cotisations professionnelles", 6, "Résultat", "Débit"),
        ("681", "Dotation aux amortissements", 6, "Résultat", "Débit"),
        
        # Classe 7: Produits
        ("701", "Ventes de biens", 7, "Résultat", "Crédit"),
        ("703", "Ventes de services", 7, "Résultat", "Crédit"),
        ("706", "Loyers perçus", 7, "Résultat", "Crédit"),
        ("7061", "Loyers immobiliers", 7, "Résultat", "Crédit"),
        ("711", "Prestations de services", 7, "Résultat", "Crédit"),
        ("7711", "Intérêts bancaires", 7, "Résultat", "Crédit"),
    ]
    
    cursor.execute("DELETE FROM comptes")
    
    for numero, libelle, classe, type_compte, sens in comptes:
        cursor.execute("""
            INSERT INTO comptes (numero, libelle, classe, type, sens)
            VALUES (?, ?, ?, ?, ?)
        """, (numero, libelle, classe, type_compte, sens))
    
    conn.commit()
    print(f"[OK] {len(comptes)} comptes du plan comptable crees")

def insert_simulation_data(cursor, conn):
    """Insérer les écritures de simulation"""
    
    print("\n📊 GÉNÉRATION DES ÉCRITURES COMPTABLES")
    print("=" * 60)
    
    # Écriture 1: Ouverture - Capital social
    print("\n[1/12] Ouverture - Capital social (01/01/2025)")
    journal_id = cursor.execute("SELECT id FROM journaux WHERE code='OD'").fetchone()[0]
    
    cursor.execute("""
        INSERT INTO ecritures (date_ecriture, journal_id, numero_ecriture, libelle, ref_piece)
        VALUES (?, ?, ?, ?, ?)
    """, ("2025-01-01", journal_id, "OD-001", "Ouverture de l'exercice", "Acte constitutif"))
    ecriture_id = cursor.lastrowid
    
    # Capital
    cursor.execute("""
        INSERT INTO lignes_ecritures (ecriture_id, numero_compte, libelle_compte, debit, credit)
        VALUES (?, ?, ?, ?, ?)
    """, (ecriture_id, "512", "Banque", 200000000, 0))
    
    cursor.execute("""
        INSERT INTO lignes_ecritures (ecriture_id, numero_compte, libelle_compte, debit, credit)
        VALUES (?, ?, ?, ?, ?)
    """, (ecriture_id, "4011", "Créances clients", 100000000, 0))
    
    cursor.execute("""
        INSERT INTO lignes_ecritures (ecriture_id, numero_compte, libelle_compte, debit, credit)
        VALUES (?, ?, ?, ?, ?)
    """, (ecriture_id, "101", "Capital social", 0, 300000000))
    
    conn.commit()
    print("   [OK] Ecriture de capital: 300 000 000 FCFA")
    
    # Écritures: Loyers mensuels (25 000 000 FCFA × 12 mois)
    print("\n[2/12] Écritures de loyers mensuels (25M FCFA × 12 mois)")
    journal_ventes = cursor.execute("SELECT id FROM journaux WHERE code='VT'").fetchone()[0]
    
    loyer_mensuel = 25000000
    mois = [
        ("01-31", "Janvier"),
        ("02-28", "Février"),
        ("03-31", "Mars"),
        ("04-30", "Avril"),
        ("05-31", "Mai"),
        ("06-30", "Juin"),
        ("07-31", "Juillet"),
        ("08-31", "Août"),
        ("09-30", "Septembre"),
        ("10-31", "Octobre"),
        ("11-30", "Novembre"),
        ("12-31", "Décembre"),
    ]
    
    for idx, (dates, mois_name) in enumerate(mois):
        date_ecriture = f"2025-{dates.split('-')[0]}-01"
        
        cursor.execute("""
            INSERT INTO ecritures (date_ecriture, journal_id, numero_ecriture, libelle, ref_piece)
            VALUES (?, ?, ?, ?, ?)
        """, (date_ecriture, journal_ventes, f"VT-{idx+1:03d}", 
              f"Loyers {mois_name} 2025 (132 locaux)", f"Loyers-{mois_name}"))
        ecriture_id = cursor.lastrowid
        
        cursor.execute("""
            INSERT INTO lignes_ecritures (ecriture_id, numero_compte, libelle_compte, debit, credit)
            VALUES (?, ?, ?, ?, ?)
        """, (ecriture_id, "512", "Banque", loyer_mensuel, 0))
        
        cursor.execute("""
            INSERT INTO lignes_ecritures (ecriture_id, numero_compte, libelle_compte, debit, credit)
            VALUES (?, ?, ?, ?, ?)
        """, (ecriture_id, "7061", "Loyers immobiliers", 0, loyer_mensuel))
    
    conn.commit()
    total_loyers = loyer_mensuel * 12
    print(f"   [OK] 12 ecritures de loyers")
    print(f"   [OK] Total loyers annuels: {total_loyers:,} FCFA")
    
    # Écritures: Charges mensuelles (estimées)
    print("\n[3/12] Écritures de charges mensuelles")
    journal_achats = cursor.execute("SELECT id FROM journaux WHERE code='AC'").fetchone()[0]
    
    charges_mensuelles = {
        "613": ("Électricité", 2000000),
        "614": ("Eau", 500000),
        "6181": ("Frais d'entretien", 3000000),
        "6182": ("Frais de gardiennage", 4000000),
        "6351": ("Assurances", 2000000),
        "621": ("Services du personnel", 2500000),
    }
    
    total_charges_mensuelles = sum([v[1] for v in charges_mensuelles.values()])
    
    for idx, (dates, mois_name) in enumerate(mois):
        date_ecriture = f"2025-{dates.split('-')[0]}-15"
        
        cursor.execute("""
            INSERT INTO ecritures (date_ecriture, journal_id, numero_ecriture, libelle, ref_piece)
            VALUES (?, ?, ?, ?, ?)
        """, (date_ecriture, journal_achats, f"AC-{idx+1:03d}", 
              f"Charges {mois_name} 2025", f"Factures-{mois_name}"))
        ecriture_id = cursor.lastrowid
        
        for compte, (libelle, montant) in charges_mensuelles.items():
            cursor.execute("""
                INSERT INTO lignes_ecritures (ecriture_id, numero_compte, libelle_compte, debit, credit)
                VALUES (?, ?, ?, ?, ?)
            """, (ecriture_id, compte, libelle, montant, 0))
        
        cursor.execute("""
            INSERT INTO lignes_ecritures (ecriture_id, numero_compte, libelle_compte, debit, credit)
            VALUES (?, ?, ?, ?, ?)
        """, (ecriture_id, "512", "Banque", 0, total_charges_mensuelles))
    
    conn.commit()
    total_charges_annuelles = total_charges_mensuelles * 12
    print(f"   [OK] 12 ecritures de charges")
    print(f"   [OK] Charges mensuelles: {total_charges_mensuelles:,} FCFA")
    print(f"   [OK] Total charges annuelles: {total_charges_annuelles:,} FCFA")
    
    # Écriture: Amortissement
    print("\n[4/12] Amortissement des bâtiments")
    cursor.execute("""
        INSERT INTO ecritures (date_ecriture, journal_id, numero_ecriture, libelle, ref_piece)
        VALUES (?, ?, ?, ?, ?)
    """, ("2025-12-31", journal_achats, "AC-900", "Amortissement annuel bâtiments", "Calcul amort."))
    ecriture_id = cursor.lastrowid
    
    amortissement = 5000000  # 5M FCFA par an
    
    cursor.execute("""
        INSERT INTO lignes_ecritures (ecriture_id, numero_compte, libelle_compte, debit, credit)
        VALUES (?, ?, ?, ?, ?)
    """, (ecriture_id, "681", "Dotation aux amortissements", amortissement, 0))
    
    cursor.execute("""
        INSERT INTO lignes_ecritures (ecriture_id, numero_compte, libelle_compte, debit, credit)
        VALUES (?, ?, ?, ?, ?)
    """, (ecriture_id, "2811", "Amortissement bâtiments", 0, amortissement))
    
    conn.commit()
    print(f"   [OK] Amortissement annuel: {amortissement:,} FCFA")
    
    print("\n" + "=" * 60)
    print("[OK] SIMULATION TERMINEE")
    print("=" * 60)

def generate_balance(cursor):
    """Générer la balance générale"""
    
    print("\n📊 BALANCE GÉNÉRALE AU 31/12/2025")
    print("=" * 80)
    print(f"{'Numéro':<10} {'Libellé':<30} {'Débit (FCFA)':>18} {'Crédit (FCFA)':>18}")
    print("-" * 80)
    
    cursor.execute("""
        SELECT 
            c.numero,
            c.libelle,
            SUM(CASE WHEN le.debit > 0 THEN le.debit ELSE 0 END) as total_debit,
            SUM(CASE WHEN le.credit > 0 THEN le.credit ELSE 0 END) as total_credit
        FROM comptes c
        LEFT JOIN lignes_ecritures le ON c.numero = le.numero_compte
        GROUP BY c.id, c.numero, c.libelle
        ORDER BY c.classe, c.numero
    """)
    
    total_debit = 0
    total_credit = 0
    
    for row in cursor.fetchall():
        numero, libelle, debit, credit = row
        debit = debit or 0
        credit = credit or 0
        total_debit += debit
        total_credit += credit
        
        if debit > 0 or credit > 0:
            print(f"{numero:<10} {libelle:<30} {debit:>18,.0f} {credit:>18,.0f}")
    
    print("-" * 80)
    print(f"{'TOTAUX':<10} {'':<30} {total_debit:>18,.0f} {total_credit:>18,.0f}")
    print("=" * 80)
    
    if abs(total_debit - total_credit) < 1:
        print("[OK] Balance equilibree!")
    else:
        print(f"⚠ Différence: {abs(total_debit - total_credit):,.0f} FCFA")

def generate_financial_statements(cursor):
    """Générer les états financiers"""
    
    print("\n📈 BILAN AU 31/12/2025")
    print("=" * 80)
    
    # Actif
    print("\nACTIF")
    print("-" * 40)
    
    cursor.execute("""
        SELECT 
            c.numero,
            c.libelle,
            SUM(CASE WHEN le.debit > 0 THEN le.debit WHEN le.credit > 0 THEN -le.credit ELSE 0 END) as solde
        FROM comptes c
        LEFT JOIN lignes_ecritures le ON c.numero = le.numero_compte
        WHERE c.classe IN (2, 3, 4, 5)
        GROUP BY c.id, c.numero, c.libelle
        HAVING solde > 0
        ORDER BY c.classe, c.numero
    """)
    
    total_actif = 0
    for row in cursor.fetchall():
        numero, libelle, solde = row
        if solde:
            print(f"{numero} {libelle:<40} {solde:>18,.0f}")
            total_actif += solde
    
    print("-" * 40)
    print(f"{'TOTAL ACTIF':<50} {total_actif:>18,.0f}")
    
    # Passif
    print("\nPASSIF")
    print("-" * 40)
    
    cursor.execute("""
        SELECT 
            c.numero,
            c.libelle,
            SUM(CASE WHEN le.credit > 0 THEN le.credit WHEN le.debit > 0 THEN -le.debit ELSE 0 END) as solde
        FROM comptes c
        LEFT JOIN lignes_ecritures le ON c.numero = le.numero_compte
        WHERE c.classe IN (1)
        GROUP BY c.id, c.numero, c.libelle
        HAVING solde > 0
        ORDER BY c.classe, c.numero
    """)
    
    total_passif = 0
    for row in cursor.fetchall():
        numero, libelle, solde = row
        if solde:
            print(f"{numero} {libelle:<40} {solde:>18,.0f}")
            total_passif += solde
    
    print("-" * 40)
    print(f"{'TOTAL PASSIF':<50} {total_passif:>18,.0f}")
    
    print("\n" + "=" * 80)
    
    # Compte de résultat
    print("\n📊 COMPTE DE RÉSULTAT 2025")
    print("=" * 80)
    
    # Produits
    print("\nPRODUITS")
    print("-" * 40)
    
    cursor.execute("""
        SELECT 
            c.numero,
            c.libelle,
            SUM(CASE WHEN le.credit > 0 THEN le.credit ELSE 0 END) as total
        FROM comptes c
        LEFT JOIN lignes_ecritures le ON c.numero = le.numero_compte
        WHERE c.classe = 7
        GROUP BY c.id, c.numero, c.libelle
        ORDER BY c.numero
    """)
    
    total_produits = 0
    for row in cursor.fetchall():
        numero, libelle, total = row
        if total and total > 0:
            print(f"{numero} {libelle:<40} {total:>18,.0f}")
            total_produits += total
    
    print("-" * 40)
    print(f"{'TOTAL PRODUITS':<50} {total_produits:>18,.0f}")
    
    # Charges
    print("\nCHARGES")
    print("-" * 40)
    
    cursor.execute("""
        SELECT 
            c.numero,
            c.libelle,
            SUM(CASE WHEN le.debit > 0 THEN le.debit ELSE 0 END) as total
        FROM comptes c
        LEFT JOIN lignes_ecritures le ON c.numero = le.numero_compte
        WHERE c.classe = 6
        GROUP BY c.id, c.numero, c.libelle
        ORDER BY c.numero
    """)
    
    total_charges = 0
    for row in cursor.fetchall():
        numero, libelle, total = row
        if total and total > 0:
            print(f"{numero} {libelle:<40} {total:>18,.0f}")
            total_charges += total
    
    print("-" * 40)
    print(f"{'TOTAL CHARGES':<50} {total_charges:>18,.0f}")
    
    # Résultat
    resultat_net = total_produits - total_charges
    print("\n" + "=" * 80)
    print(f"{'RÉSULTAT NET':<50} {resultat_net:>18,.0f}")
    print("=" * 80)
    
    # Taux de marge
    if total_produits > 0:
        taux_marge = (resultat_net / total_produits) * 100
        print(f"\nTaux de marge: {taux_marge:.2f}%")

def main():
    """Fonction principale"""
    
    print("\n" + "=" * 80)
    print("SIMULATION COMPTABLE - SIB-SCI")
    print("=" * 80)
    print("\nDonnées de simulation:")
    print("  - Entreprise: SIB-SCI (Societe Civile Immobiliere)")
    print("  - Capital initial: 300 000 000 FCFA")
    print("  - Creances clients: 100 000 000 FCFA")
    print("  - Nombre de locaux: 132")
    print("  - Loyer mensuel: 25 000 000 FCFA")
    print("  - Total loyers annuels: 300 000 000 FCFA")
    print("  - Periode: 01/01/2025 - 31/12/2025")
    print("\n" + "=" * 80)
    
    try:
        # Connexion
        conn, cursor = create_connection()
        
        # Initialisation
        init_database(cursor, conn)
        insert_entreprise(cursor, conn)
        insert_journaux(cursor, conn)
        insert_comptes(cursor, conn)
        
        # Simulation
        insert_simulation_data(cursor, conn)
        
        # Rapports
        generate_balance(cursor)
        generate_financial_statements(cursor)
        
        conn.close()
        
        print("\n✅ SIMULATION COMPLÈTE!")
        print(f"\n📁 Base de données sauvegardée: {db_path}")
        print("\nVous pouvez maintenant ouvrir l'application OHADA-COMPTA")
        print("pour consulter les données saisies.")
        
    except Exception as e:
        print(f"\n[ERREUR] {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    main()
