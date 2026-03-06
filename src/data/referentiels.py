# -*- coding: utf-8 -*-
"""
OHADA-COMPTA - Données de référence
Référentiels pour les pays UEMOA, formes juridiques, régimes fiscaux et taux
"""

# ============================================================================
# SYSTÈMES COMPTABLES
# ============================================================================
SYSTEMES_COMPTABLES = [
    {"code": "SYSCOHADA", "libelle": "Système Comptable OHADA", "lucratif": True, "description": "Pour les entités à but lucratif"},
    {"code": "SYCEBNL", "libelle": "Système Comptable Entités à But Non Lucratif", "lucratif": False, "description": "Pour les associations, ONG, fondations"},
    {"code": "COMPTA_PUB", "libelle": "Comptabilité Publique", "lucratif": False, "description": "Pour les établissements publics administratifs"},
]

# ============================================================================
# PAYS DE L'UEMOA
# ============================================================================
PAYS_UEMOA = [
    {
        "code": "BJ", "nom": "Bénin", "capitale": "Porto-Novo", "monnaie": "XOF",
        "indicatif": "+229", "langue": "Français",
        "tva_normal": 18.0, "tva_reduit": 0.0,
        "is_normal": 30.0, "is_reduit": 25.0,
        "imf_taux": 1.0, "imf_min": 200000, "imf_max": 2000000,
        "patente_taux": 0.5,
        "ircm_taux": 15.0,
        "tas_taux": 4.0,  # Taxe sur les salaires
    },
    {
        "code": "BF", "nom": "Burkina Faso", "capitale": "Ouagadougou", "monnaie": "XOF",
        "indicatif": "+226", "langue": "Français",
        "tva_normal": 18.0, "tva_reduit": 0.0,
        "is_normal": 27.5, "is_reduit": 25.0,
        "imf_taux": 0.5, "imf_min": 500000, "imf_max": 3000000,
        "patente_taux": 0.5,
        "ircm_taux": 12.5,
        "tas_taux": 3.0,
    },
    {
        "code": "CI", "nom": "Côte d'Ivoire", "capitale": "Yamoussoukro", "monnaie": "XOF",
        "indicatif": "+225", "langue": "Français",
        "tva_normal": 18.0, "tva_reduit": 9.0,
        "is_normal": 25.0, "is_reduit": 20.0,
        "imf_taux": 0.5, "imf_min": 400000, "imf_max": 30000000,
        "patente_taux": 0.5,
        "ircm_taux": 10.0,
        "tas_taux": 2.8,
    },
    {
        "code": "GW", "nom": "Guinée-Bissau", "capitale": "Bissau", "monnaie": "XOF",
        "indicatif": "+245", "langue": "Portugais",
        "tva_normal": 17.0, "tva_reduit": 0.0,
        "is_normal": 25.0, "is_reduit": 20.0,
        "imf_taux": 1.0, "imf_min": 300000, "imf_max": 2000000,
        "patente_taux": 0.5,
        "ircm_taux": 10.0,
        "tas_taux": 2.0,
    },
    {
        "code": "ML", "nom": "Mali", "capitale": "Bamako", "monnaie": "XOF",
        "indicatif": "+223", "langue": "Français",
        "tva_normal": 18.0, "tva_reduit": 5.0,
        "is_normal": 30.0, "is_reduit": 25.0,
        "imf_taux": 1.0, "imf_min": 500000, "imf_max": 12500000,
        "patente_taux": 0.75,
        "ircm_taux": 7.0,
        "tas_taux": 3.5,
    },
    {
        "code": "NE", "nom": "Niger", "capitale": "Niamey", "monnaie": "XOF",
        "indicatif": "+227", "langue": "Français",
        "tva_normal": 19.0, "tva_reduit": 5.0,
        "is_normal": 30.0, "is_reduit": 25.0,
        "imf_taux": 1.0, "imf_min": 500000, "imf_max": 5000000,
        "patente_taux": 0.5,
        "ircm_taux": 15.0,
        "tas_taux": 3.0,
    },
    {
        "code": "SN", "nom": "Sénégal", "capitale": "Dakar", "monnaie": "XOF",
        "indicatif": "+221", "langue": "Français",
        "tva_normal": 18.0, "tva_reduit": 10.0,
        "is_normal": 30.0, "is_reduit": 25.0,
        "imf_taux": 0.5, "imf_min": 500000, "imf_max": 5000000,
        "patente_taux": 0.5,
        "ircm_taux": 10.0,
        "tas_taux": 3.0,
    },
    {
        "code": "TG", "nom": "Togo", "capitale": "Lomé", "monnaie": "XOF",
        "indicatif": "+228", "langue": "Français",
        "tva_normal": 18.0, "tva_reduit": 10.0,
        "is_normal": 27.0, "is_reduit": 22.0,
        "imf_taux": 1.0, "imf_min": 100000, "imf_max": 5000000,
        "patente_taux": 0.5,
        "ircm_taux": 7.0,  # 3% pour personnes physiques
        "tas_taux": 3.0,
    },
]

# ============================================================================
# CATÉGORIES DE FORMES JURIDIQUES
# ============================================================================
CATEGORIES_FORMES = [
    {"code": "COMMERCIALE", "libelle": "Sociétés Commerciales", "systeme": "SYSCOHADA"},
    {"code": "CIVILE", "libelle": "Sociétés Civiles", "systeme": "SYSCOHADA"},
    {"code": "COOPERATIVE", "libelle": "Sociétés Coopératives", "systeme": "SYSCOHADA"},
    {"code": "EBNL", "libelle": "Entités à But Non Lucratif", "systeme": "SYCEBNL"},
    {"code": "PUBLIQUE", "libelle": "Structures Publiques", "systeme": "COMPTA_PUB"},
    {"code": "ETABLISSEMENT", "libelle": "Établissements Secondaires", "systeme": "SYSCOHADA"},
    {"code": "LIBERALE", "libelle": "Professions Libérales", "systeme": "SYSCOHADA"},
]

# ============================================================================
# FORMES JURIDIQUES COMPLÈTES
# ============================================================================
FORMES_JURIDIQUES = [
    # === SOCIÉTÉS COMMERCIALES (SYSCOHADA) ===
    {"code": "EI", "libelle": "Entreprise Individuelle", "categorie": "COMMERCIALE", "systeme": "SYSCOHADA", 
     "capital_min": 0, "associes_min": 1, "associes_max": 1, "ohada": True,
     "description": "Entreprise exploitée par une seule personne physique"},
    {"code": "SARL", "libelle": "Société à Responsabilité Limitée", "categorie": "COMMERCIALE", "systeme": "SYSCOHADA",
     "capital_min": 1000000, "associes_min": 2, "associes_max": 100, "ohada": True,
     "description": "Société dont les associés ne sont responsables qu'à concurrence de leurs apports"},
    {"code": "SARLU", "libelle": "SARL Unipersonnelle", "categorie": "COMMERCIALE", "systeme": "SYSCOHADA",
     "capital_min": 1000000, "associes_min": 1, "associes_max": 1, "ohada": True,
     "description": "SARL avec un associé unique"},
    {"code": "SA", "libelle": "Société Anonyme", "categorie": "COMMERCIALE", "systeme": "SYSCOHADA",
     "capital_min": 10000000, "associes_min": 1, "associes_max": None, "ohada": True,
     "description": "Société dont le capital est divisé en actions"},
    {"code": "SAS", "libelle": "Société par Actions Simplifiée", "categorie": "COMMERCIALE", "systeme": "SYSCOHADA",
     "capital_min": 0, "associes_porto_min": 1, "associes_max": None, "ohada": True,
     "description": "Société offrant une grande liberté statutaire"},
    {"code": "SASU", "libelle": "SAS Unipersonnelle", "categorie": "COMMERCIALE", "systeme": "SYSCOHADA",
     "capital_min": 0, "associes_min": 1, "associes_max": 1, "ohada": True,
     "description": "SAS avec un associé unique"},
    {"code": "SNC", "libelle": "Société en Nom Collectif", "categorie": "COMMERCIALE", "systeme": "SYSCOHADA",
     "capital_min": 0, "associes_min": 2, "associes_max": None, "ohada": True,
     "description": "Société où les associés sont solidairement et indéfiniment responsables"},
    {"code": "SCS", "libelle": "Société en Commandite Simple", "categorie": "COMMERCIALE", "systeme": "SYSCOHADA",
     "capital_min": 0, "associes_min": 2, "associes_max": None, "ohada": True,
     "description": "Société avec commandités et commanditaires"},
    {"code": "GIE", "libelle": "Groupement d'Intérêt Économique", "categorie": "COMMERCIALE", "systeme": "SYSCOHADA",
     "capital_min": 0, "associes_min": 2, "associes_max": None, "ohada": True,
     "description": "Groupement pour faciliter l'activité économique de ses membres"},
    {"code": "SEP", "libelle": "Société en Participation", "categorie": "COMMERCIALE", "systeme": "SYSCOHADA",
     "capital_min": 0, "associes_min": 2, "associes_max": None, "ohada": True,
     "description": "Société sans personnalité morale"},
    
    # === SOCIÉTÉS CIVILES (SYSCOHADA) ===
    {"code": "SCI", "libelle": "Société Civile Immobilière", "categorie": "CIVILE", "systeme": "SYSCOHADA",
     "capital_min": 0, "associes_min": 2, "associes_max": None, "ohada": False,
     "description": "Société pour la gestion de biens immobiliers"},
    {"code": "SGI", "libelle": "Société de Gestion Immobilière", "categorie": "CIVILE", "systeme": "SYSCOHADA",
     "capital_min": 0, "associes_min": 2, "associes_max": None, "ohada": False,
     "description": "Synonyme de SCI"},
    {"code": "SCP", "libelle": "Société Civile Professionnelle", "categorie": "CIVILE", "systeme": "SYSCOHADA",
     "capital_min": 0, "associes_min": 2, "associes_max": None, "ohada": False,
     "description": "Société pour l'exercice en commun d'une profession libérale"},
    {"code": "SCPA", "libelle": "Société Civile Professionnelle d'Avocats", "categorie": "CIVILE", "systeme": "SYSCOHADA",
     "capital_min": 0, "associes_min": 2, "associes_max": None, "ohada": False,
     "description": "SCP réservée aux avocats"},
    {"code": "SCM", "libelle": "Société Civile de Moyens", "categorie": "CIVILE", "systeme": "SYSCOHADA",
     "capital_min": 0, "associes_min": 2, "associes_max": None, "ohada": False,
     "description": "Société pour le partage de moyens entre professionnels"},
    {"code": "SC", "libelle": "Société Civile", "categorie": "CIVILE", "systeme": "SYSCOHADA",
     "capital_min": 0, "associes_min": 2, "associes_max": None, "ohada": False,
     "description": "Société civile de droit commun"},
    
    # === COOPÉRATIVES (SYSCOHADA) ===
    {"code": "SCOOPS", "libelle": "Société Coopérative Simplifiée", "categorie": "COOPERATIVE", "systeme": "SYSCOHADA",
     "capital_min": 0, "associes_min": 5, "associes_max": None, "ohada": True,
     "description": "Coopérative pour petites structures (5 membres minimum)"},
    {"code": "SCOOP-CA", "libelle": "Société Coopérative avec Conseil d'Administration", "categorie": "COOPERATIVE", "systeme": "SYSCOHADA",
     "capital_min": 0, "associes_min": 15, "associes_max": None, "ohada": True,
     "description": "Coopérative pour grandes structures (15 membres minimum)"},
    {"code": "COOPEC", "libelle": "Coopérative d'Épargne et de Crédit", "categorie": "COOPERATIVE", "systeme": "SYSCOHADA",
     "capital_min": 0, "associes_min": 5, "associes_max": None, "ohada": True,
     "description": "Coopérative de microfinance"},
    {"code": "UNION-COOP", "libelle": "Union de Coopératives", "categorie": "COOPERATIVE", "systeme": "SYSCOHADA",
     "capital_min": 0, "associes_min": 2, "associes_max": None, "ohada": True,
     "description": "Regroupement de coopératives"},
    {"code": "FED-COOP", "libelle": "Fédération de Coopératives", "categorie": "COOPERATIVE", "systeme": "SYSCOHADA",
     "capital_min": 0, "associes_min": 2, "associes_max": None, "ohada": True,
     "description": "Regroupement d'unions de coopératives"},
    {"code": "CONFED-COOP", "libelle": "Confédération de Coopératives", "categorie": "COOPERATIVE", "systeme": "SYSCOHADA",
     "capital_min": 0, "associes_min": 2, "associes_max": None, "ohada": True,
     "description": "Regroupement de fédérations de coopératives"},
    
    # === ENTITÉS À BUT NON LUCRATIF (SYCEBNL) ===
    {"code": "ASSO", "libelle": "Association", "categorie": "EBNL", "systeme": "SYCEBNL",
     "capital_min": 0, "associes_min": 2, "associes_max": None, "ohada": True,
     "description": "Groupement de personnes pour un but non lucratif"},
    {"code": "ONG", "libelle": "Organisation Non Gouvernementale", "categorie": "EBNL", "systeme": "SYCEBNL",
     "capital_min": 0, "associes_min": 2, "associes_max": None, "ohada": True,
     "description": "Organisation d'intérêt public indépendante de l'État"},
    {"code": "FOND", "libelle": "Fondation", "categorie": "EBNL", "systeme": "SYCEBNL",
     "capital_min": 0, "associes_min": 1, "associes_max": None, "ohada": True,
     "description": "Patrimoine affecté à une œuvre d'intérêt général"},
    {"code": "PROJ", "libelle": "Projet de Développement", "categorie": "EBNL", "systeme": "SYCEBNL",
     "capital_min": 0, "associes_min": 1, "associes_max": None, "ohada": True,
     "description": "Programme financé par des bailleurs de fonds"},
    {"code": "ORDRE", "libelle": "Ordre Professionnel", "categorie": "EBNL", "systeme": "SYCEBNL",
     "capital_min": 0, "associes_min": 2, "associes_max": None, "ohada": True,
     "description": "Organisation réglementant une profession"},
    {"code": "SYND", "libelle": "Syndicat", "categorie": "EBNL", "systeme": "SYCEBNL",
     "capital_min": 0, "associes_min": 2, "associes_max": None, "ohada": True,
     "description": "Organisation de défense des intérêts professionnels"},
    {"code": "PARTI", "libelle": "Parti Politique", "categorie": "EBNL", "systeme": "SYCEBNL",
     "capital_min": 0, "associes_min": 2, "associes_max": None, "ohada": True,
     "description": "Organisation politique"},
    {"code": "RELIG", "libelle": "Organisation Religieuse", "categorie": "EBNL", "systeme": "SYCEBNL",
     "capital_min": 0, "associes_min": 2, "associes_max": None, "ohada": True,
     "description": "Église, mosquée, temple ou autre organisation confessionnelle"},
    {"code": "SPORT", "libelle": "Club/Association Sportive", "categorie": "EBNL", "systeme": "SYCEBNL",
     "capital_min": 0, "associes_min": 2, "associes_max": None, "ohada": True,
     "description": "Association à vocation sportive"},
    {"code": "MUT", "libelle": "Mutuelle Sociale", "categorie": "EBNL", "systeme": "SYCEBNL",
     "capital_min": 0, "associes_min": 2, "associes_max": None, "ohada": True,
     "description": "Organisation de prévoyance sociale"},
    {"code": "GIC", "libelle": "Groupe d'Initiative Commune", "categorie": "EBNL", "systeme": "SYCEBNL",
     "capital_min": 0, "associes_min": 5, "associes_max": None, "ohada": True,
     "description": "Groupement communautaire (droit local)"},
    {"code": "GPF", "libelle": "Groupement de Promotion Féminine", "categorie": "EBNL", "systeme": "SYCEBNL",
     "capital_min": 0, "associes_min": 5, "associes_max": None, "ohada": True,
     "description": "Groupement de femmes"},
    
    # === STRUCTURES PUBLIQUES ===
    {"code": "EP", "libelle": "Établissement Public", "categorie": "PUBLIQUE", "systeme": "COMPTA_PUB",
     "capital_min": 0, "associes_min": 1, "associes_max": 1, "ohada": False,
     "description": "Entité publique dotée de l'autonomie"},
    {"code": "EPA", "libelle": "Établissement Public Administratif", "categorie": "PUBLIQUE", "systeme": "COMPTA_PUB",
     "capital_min": 0, "associes_min": 1, "associes_max": 1, "ohada": False,
     "description": "Établissement public à caractère administratif"},
    {"code": "EPIC", "libelle": "Établissement Public Industriel et Commercial", "categorie": "PUBLIQUE", "systeme": "SYSCOHADA",
     "capital_min": 0, "associes_min": 1, "associes_max": 1, "ohada": False,
     "description": "Établissement public à caractère commercial"},
    {"code": "SEM", "libelle": "Société d'Économie Mixte", "categorie": "PUBLIQUE", "systeme": "SYSCOHADA",
     "capital_min": 10000000, "associes_min": 2, "associes_max": None, "ohada": False,
     "description": "Société associant capitaux publics et privés"},
    {"code": "SN", "libelle": "Société Nationale", "categorie": "PUBLIQUE", "systeme": "SYSCOHADA",
     "capital_min": 0, "associes_min": 1, "associes_max": 1, "ohada": False,
     "description": "Société détenue à 100% par l'État"},
    
    # === ÉTABLISSEMENTS SECONDAIRES ===
    {"code": "SUCC", "libelle": "Succursale", "categorie": "ETABLISSEMENT", "systeme": "SYSCOHADA",
     "capital_min": 0, "associes_min": 1, "associes_max": 1, "ohada": True,
     "description": "Établissement secondaire d'une société étrangère"},
    {"code": "FILIALE", "libelle": "Filiale", "categorie": "ETABLISSEMENT", "systeme": "SYSCOHADA",
     "capital_min": 0, "associes_min": 1, "associes_max": None, "ohada": True,
     "description": "Société contrôlée par une société mère"},
    {"code": "BUREAU", "libelle": "Bureau de Représentation", "categorie": "ETABLISSEMENT", "systeme": "SYSCOHADA",
     "capital_min": 0, "associes_min": 1, "associes_max": 1, "ohada": False,
     "description": "Bureau sans activité commerciale directe"},
    {"code": "AGENCE", "libelle": "Agence", "categorie": "ETABLISSEMENT", "systeme": "SYSCOHADA",
     "capital_min": 0, "associes_min": 1, "associes_max": 1, "ohada": False,
     "description": "Point de vente ou de service"},
    
    # === PROFESSIONS LIBÉRALES ===
    {"code": "SEL", "libelle": "Société d'Exercice Libéral", "categorie": "LIBERALE", "systeme": "SYSCOHADA",
     "capital_min": 0, "associes_min": 1, "associes_max": None, "ohada": False,
     "description": "Société pour l'exercice d'une profession libérale"},
    {"code": "SELARL", "libelle": "SEL à Responsabilité Limitée", "categorie": "LIBERALE", "systeme": "SYSCOHADA",
     "capital_min": 0, "associes_min": 1, "associes_max": None, "ohada": False,
     "description": "SEL sous forme de SARL"},
    {"code": "SELAFA", "libelle": "SEL à Forme Anonyme", "categorie": "LIBERALE", "systeme": "SYSCOHADA",
     "capital_min": 0, "associes_min": 1, "associes_max": None, "ohada": False,
     "description": "SEL sous forme de SA"},
    {"code": "SELAS", "libelle": "SEL par Actions Simplifiée", "categorie": "LIBERALE", "systeme": "SYSCOHADA",
     "capital_min": 0, "associes_min": 1, "associes_max": None, "ohada": False,
     "description": "SEL sous forme de SAS"},
]

# ============================================================================
# RÉGIMES FISCAUX
# ============================================================================
REGIMES_FISCAUX = [
    {
        "code": "CME", 
        "libelle": "Contribution Micro-Entreprise",
        "description": "Régime forfaitaire pour les très petites entreprises",
        "seuil_commerce": 30000000,  # 30 millions FCFA
        "seuil_services": 20000000,  # 20 millions FCFA
        "tva_applicable": False,
        "comptabilite": "Simplifiée",
        "declarations": ["Annuelle"]
    },
    {
        "code": "TF",
        "libelle": "Taxe Forfaitaire",
        "description": "Régime forfaitaire intermédiaire",
        "seuil_commerce": 50000000,  # 50 millions FCFA
        "seuil_services": 25000000,  # 25 millions FCFA
        "tva_applicable": False,
        "comptabilite": "Simplifiée",
        "declarations": ["Annuelle"]
    },
    {
        "code": "RSI",
        "libelle": "Réel Simplifié d'Imposition",
        "description": "Régime réel avec obligations allégées",
        "seuil_commerce": 100000000,  # 100 millions FCFA
        "seuil_services": 50000000,   # 50 millions FCFA
        "tva_applicable": True,
        "comptabilite": "Normale simplifiée",
        "declarations": ["Mensuelle TVA", "Annuelle IS"]
    },
    {
        "code": "RN",
        "libelle": "Réel Normal",
        "description": "Régime de droit commun avec obligations complètes",
        "seuil_commerce": None,  # Pas de limite
        "seuil_services": None,
        "tva_applicable": True,
        "comptabilite": "Normale",
        "declarations": ["Mensuelle TVA", "Trimestrielle IS", "Annuelle"]
    },
]

# ============================================================================
# CODES JOURNAUX COMPTABLES
# ============================================================================
CODES_JOURNAUX = [
    {"code": "AC", "libelle": "Achats", "description": "Journal des achats fournisseurs"},
    {"code": "VT", "libelle": "Ventes", "description": "Journal des ventes clients"},
    {"code": "BQ", "libelle": "Banque", "description": "Journal des opérations bancaires"},
    {"code": "CA", "libelle": "Caisse", "description": "Journal des opérations de caisse"},
    {"code": "OD", "libelle": "Opérations Diverses", "description": "Journal des opérations diverses"},
    {"code": "AN", "libelle": "À Nouveau", "description": "Journal des à-nouveaux"},
    {"code": "SA", "libelle": "Salaires", "description": "Journal de paie"},
    {"code": "IM", "libelle": "Immobilisations", "description": "Journal des immobilisations"},
    {"code": "ST", "libelle": "Stocks", "description": "Journal des stocks"},
    {"code": "CL", "libelle": "Clôture", "description": "Journal des écritures de clôture"},
]

# ============================================================================
# TAXES ET IMPÔTS
# ============================================================================
TYPES_TAXES = [
    {"code": "TVA", "libelle": "Taxe sur la Valeur Ajoutée", "type": "INDIRECT"},
    {"code": "IS", "libelle": "Impôt sur les Sociétés", "type": "DIRECT"},
    {"code": "IMF", "libelle": "Impôt Minimum Forfaitaire", "type": "DIRECT"},
    {"code": "IRCM", "libelle": "Impôt sur les Revenus des Capitaux Mobiliers", "type": "DIRECT"},
    {"code": "PATENTE", "libelle": "Contribution des Patentes", "type": "DIRECT"},
    {"code": "CF", "libelle": "Contribution Foncière", "type": "DIRECT"},
    {"code": "TAS", "libelle": "Taxe sur les Salaires", "type": "DIRECT"},
    {"code": "TA", "libelle": "Taxe d'Apprentissage", "type": "DIRECT"},
    {"code": "TFP", "libelle": "Taxe Formation Professionnelle", "type": "DIRECT"},
    {"code": "RAS", "libelle": "Retenue à la Source", "type": "DIRECT"},
    {"code": "AIB", "libelle": "Acompte sur Impôt assis sur les Bénéfices", "type": "DIRECT"},
]

# ============================================================================
# FONCTIONS UTILITAIRES
# ============================================================================
def get_pays_par_code(code):
    """Retourne les informations d'un pays par son code"""
    for pays in PAYS_UEMOA:
        if pays["code"] == code:
            return pays
    return None

def get_forme_juridique_par_code(code):
    """Retourne les informations d'une forme juridique par son code"""
    for forme in FORMES_JURIDIQUES:
        if forme["code"] == code:
            return forme
    return None

def get_formes_par_categorie(categorie):
    """Retourne toutes les formes juridiques d'une catégorie"""
    return [f for f in FORMES_JURIDIQUES if f["categorie"] == categorie]

def get_formes_par_systeme(systeme):
    """Retourne toutes les formes juridiques d'un système comptable"""
    return [f for f in FORMES_JURIDIQUES if f["systeme"] == systeme]

def get_regime_fiscal_par_ca(chiffre_affaires, type_activite="commerce"):
    """Détermine le régime fiscal applicable en fonction du CA"""
    seuil_key = f"seuil_{type_activite}"
    for regime in REGIMES_FISCAUX:
        seuil = regime.get(seuil_key)
        if seuil is None or chiffre_affaires <= seuil:
            return regime
    return REGIMES_FISCAUX[-1]  # Réel Normal par défaut

def calculer_imf(chiffre_affaires, pays_code):
    """Calcule l'Impôt Minimum Forfaitaire pour un pays donné"""
    pays = get_pays_par_code(pays_code)
    if not pays:
        return 0
    
    imf = chiffre_affaires * (pays["imf_taux"] / 100)
    imf = max(imf, pays["imf_min"])
    imf = min(imf, pays["imf_max"])
    return imf

def calculer_is(benefice, pays_code, taux_reduit=False):
    """Calcule l'Impôt sur les Sociétés pour un pays donné"""
    pays = get_pays_par_code(pays_code)
    if not pays:
        return 0
    
    taux = pays["is_reduit"] if taux_reduit else pays["is_normal"]
    return benefice * (taux / 100)

def get_impot_du(benefice, chiffre_affaires, pays_code):
    """Détermine l'impôt dû (IS ou IMF, le plus élevé)"""
    is_calcule = calculer_is(benefice, pays_code)
    imf_calcule = calculer_imf(chiffre_affaires, pays_code)
    
    if is_calcule >= imf_calcule:
        return {"type": "IS", "montant": is_calcule}
    else:
        return {"type": "IMF", "montant": imf_calcule}
