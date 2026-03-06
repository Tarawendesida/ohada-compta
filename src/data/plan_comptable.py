# -*- coding: utf-8 -*-
"""
Plan comptable SYSCOHADA et SYCEBNL
Conforme aux normes OHADA
"""

PLAN_COMPTABLE_SYSCOHADA = [
    # Classe 1 - Comptes de ressources durables
    {'numero': '10', 'libelle': 'Capital', 'classe': 1, 'type': 'Bilan', 'sens': 'Crédit'},
    {'numero': '101', 'libelle': 'Capital social', 'classe': 1, 'type': 'Bilan', 'sens': 'Crédit'},
    {'numero': '1011', 'libelle': 'Capital souscrit, appelé, versé', 'classe': 1, 'type': 'Bilan', 'sens': 'Crédit'},
    {'numero': '1012', 'libelle': 'Capital souscrit non appelé', 'classe': 1, 'type': 'Bilan', 'sens': 'Crédit'},
    {'numero': '1013', 'libelle': 'Capital souscrit appelé non versé', 'classe': 1, 'type': 'Bilan', 'sens': 'Crédit'},
    
    {'numero': '11', 'libelle': 'Réserves', 'classe': 1, 'type': 'Bilan', 'sens': 'Crédit'},
    {'numero': '111', 'libelle': 'Réserve légale', 'classe': 1, 'type': 'Bilan', 'sens': 'Crédit'},
    {'numero': '112', 'libelle': 'Réserves statutaires', 'classe': 1, 'type': 'Bilan', 'sens': 'Crédit'},
    {'numero': '113', 'libelle': 'Réserves réglementées', 'classe': 1, 'type': 'Bilan', 'sens': 'Crédit'},
    {'numero': '118', 'libelle': 'Autres réserves', 'classe': 1, 'type': 'Bilan', 'sens': 'Crédit'},
    
    {'numero': '12', 'libelle': 'Report à nouveau', 'classe': 1, 'type': 'Bilan', 'sens': 'Crédit'},
    {'numero': '121', 'libelle': 'Report à nouveau créditeur', 'classe': 1, 'type': 'Bilan', 'sens': 'Crédit'},
    {'numero': '129', 'libelle': 'Report à nouveau débiteur', 'classe': 1, 'type': 'Bilan', 'sens': 'Débit'},
    
    {'numero': '13', 'libelle': 'Résultat net de l\'exercice', 'classe': 1, 'type': 'Bilan', 'sens': 'Crédit'},
    {'numero': '131', 'libelle': 'Résultat net: Bénéfice', 'classe': 1, 'type': 'Bilan', 'sens': 'Crédit'},
    {'numero': '139', 'libelle': 'Résultat net: Perte', 'classe': 1, 'type': 'Bilan', 'sens': 'Débit'},
    
    {'numero': '14', 'libelle': 'Subventions d\'investissement', 'classe': 1, 'type': 'Bilan', 'sens': 'Crédit'},
    {'numero': '141', 'libelle': 'Subventions d\'équipement', 'classe': 1, 'type': 'Bilan', 'sens': 'Crédit'},
    
    {'numero': '16', 'libelle': 'Emprunts et dettes assimilées', 'classe': 1, 'type': 'Bilan', 'sens': 'Crédit'},
    {'numero': '161', 'libelle': 'Emprunts obligataires', 'classe': 1, 'type': 'Bilan', 'sens': 'Crédit'},
    {'numero': '162', 'libelle': 'Emprunts et dettes auprès des établissements de crédit', 'classe': 1, 'type': 'Bilan', 'sens': 'Crédit'},
    {'numero': '163', 'libelle': 'Avances reçues de l\'État', 'classe': 1, 'type': 'Bilan', 'sens': 'Crédit'},
    {'numero': '164', 'libelle': 'Avances et acomptes reçus sur commandes', 'classe': 1, 'type': 'Bilan', 'sens': 'Crédit'},
    {'numero': '165', 'libelle': 'Dépôts et cautionnements reçus', 'classe': 1, 'type': 'Bilan', 'sens': 'Crédit'},
    {'numero': '166', 'libelle': 'Intérêts courus', 'classe': 1, 'type': 'Bilan', 'sens': 'Crédit'},
    {'numero': '168', 'libelle': 'Autres emprunts et dettes', 'classe': 1, 'type': 'Bilan', 'sens': 'Crédit'},
    
    # Classe 2 - Comptes d'actif immobilisé
    {'numero': '21', 'libelle': 'Immobilisations incorporelles', 'classe': 2, 'type': 'Bilan', 'sens': 'Débit'},
    {'numero': '211', 'libelle': 'Frais de développement et de prospection', 'classe': 2, 'type': 'Bilan', 'sens': 'Débit'},
    {'numero': '212', 'libelle': 'Brevets, licences, logiciels', 'classe': 2, 'type': 'Bilan', 'sens': 'Débit'},
    {'numero': '213', 'libelle': 'Concessions et droits similaires', 'classe': 2, 'type': 'Bilan', 'sens': 'Débit'},
    {'numero': '214', 'libelle': 'Fonds commercial et droit au bail', 'classe': 2, 'type': 'Bilan', 'sens': 'Débit'},
    {'numero': '218', 'libelle': 'Autres immobilisations incorporelles', 'classe': 2, 'type': 'Bilan', 'sens': 'Débit'},
    
    {'numero': '22', 'libelle': 'Terrains', 'classe': 2, 'type': 'Bilan', 'sens': 'Débit'},
    {'numero': '221', 'libelle': 'Terrains agricoles et forestiers', 'classe': 2, 'type': 'Bilan', 'sens': 'Débit'},
    {'numero': '222', 'libelle': 'Terrains nus', 'classe': 2, 'type': 'Bilan', 'sens': 'Débit'},
    {'numero': '223', 'libelle': 'Terrains bâtis', 'classe': 2, 'type': 'Bilan', 'sens': 'Débit'},
    {'numero': '224', 'libelle': 'Travaux de mise en valeur des terrains', 'classe': 2, 'type': 'Bilan', 'sens': 'Débit'},
    
    {'numero': '23', 'libelle': 'Bâtiments, installations techniques et agencements', 'classe': 2, 'type': 'Bilan', 'sens': 'Débit'},
    {'numero': '231', 'libelle': 'Bâtiments industriels, agricoles, administratifs et commerciaux', 'classe': 2, 'type': 'Bilan', 'sens': 'Débit'},
    {'numero': '232', 'libelle': 'Bâtiments affectés aux autres activités', 'classe': 2, 'type': 'Bilan', 'sens': 'Débit'},
    {'numero': '233', 'libelle': 'Ouvrages d\'infrastructure', 'classe': 2, 'type': 'Bilan', 'sens': 'Débit'},
    {'numero': '234', 'libelle': 'Installations techniques', 'classe': 2, 'type': 'Bilan', 'sens': 'Débit'},
    {'numero': '235', 'libelle': 'Aménagements de bureaux', 'classe': 2, 'type': 'Bilan', 'sens': 'Débit'},
    {'numero': '238', 'libelle': 'Autres installations et agencements', 'classe': 2, 'type': 'Bilan', 'sens': 'Débit'},
    
    {'numero': '24', 'libelle': 'Matériel', 'classe': 2, 'type': 'Bilan', 'sens': 'Débit'},
    {'numero': '241', 'libelle': 'Matériel et outillage industriel et commercial', 'classe': 2, 'type': 'Bilan', 'sens': 'Débit'},
    {'numero': '242', 'libelle': 'Matériel et outillage agricole', 'classe': 2, 'type': 'Bilan', 'sens': 'Débit'},
    {'numero': '243', 'libelle': 'Matériel d\'emballage récupérable et identifiable', 'classe': 2, 'type': 'Bilan', 'sens': 'Débit'},
    {'numero': '244', 'libelle': 'Matériel de bureau et informatique', 'classe': 2, 'type': 'Bilan', 'sens': 'Débit'},
    {'numero': '245', 'libelle': 'Matériel de transport', 'classe': 2, 'type': 'Bilan', 'sens': 'Débit'},
    {'numero': '246', 'libelle': 'Immobilisations animales et agricoles', 'classe': 2, 'type': 'Bilan', 'sens': 'Débit'},
    {'numero': '248', 'libelle': 'Autres matériels', 'classe': 2, 'type': 'Bilan', 'sens': 'Débit'},
    
    {'numero': '28', 'libelle': 'Amortissements', 'classe': 2, 'type': 'Bilan', 'sens': 'Crédit'},
    {'numero': '281', 'libelle': 'Amortissements des immobilisations incorporelles', 'classe': 2, 'type': 'Bilan', 'sens': 'Crédit'},
    {'numero': '282', 'libelle': 'Amortissements des terrains', 'classe': 2, 'type': 'Bilan', 'sens': 'Crédit'},
    {'numero': '283', 'libelle': 'Amortissements des bâtiments', 'classe': 2, 'type': 'Bilan', 'sens': 'Crédit'},
    {'numero': '284', 'libelle': 'Amortissements du matériel', 'classe': 2, 'type': 'Bilan', 'sens': 'Crédit'},
    
    # Classe 3 - Comptes de stocks
    {'numero': '31', 'libelle': 'Marchandises', 'classe': 3, 'type': 'Bilan', 'sens': 'Débit'},
    {'numero': '311', 'libelle': 'Marchandises A', 'classe': 3, 'type': 'Bilan', 'sens': 'Débit'},
    {'numero': '312', 'libelle': 'Marchandises B', 'classe': 3, 'type': 'Bilan', 'sens': 'Débit'},
    
    {'numero': '32', 'libelle': 'Matières premières et fournitures liées', 'classe': 3, 'type': 'Bilan', 'sens': 'Débit'},
    {'numero': '321', 'libelle': 'Matières A', 'classe': 3, 'type': 'Bilan', 'sens': 'Débit'},
    {'numero': '322', 'libelle': 'Matières B', 'classe': 3, 'type': 'Bilan', 'sens': 'Débit'},
    
    {'numero': '33', 'libelle': 'Autres approvisionnements', 'classe': 3, 'type': 'Bilan', 'sens': 'Débit'},
    {'numero': '331', 'libelle': 'Matières consommables', 'classe': 3, 'type': 'Bilan', 'sens': 'Débit'},
    {'numero': '332', 'libelle': 'Fournitures d\'atelier et d\'usine', 'classe': 3, 'type': 'Bilan', 'sens': 'Débit'},
    {'numero': '333', 'libelle': 'Fournitures de magasin', 'classe': 3, 'type': 'Bilan', 'sens': 'Débit'},
    {'numero': '334', 'libelle': 'Fournitures de bureau', 'classe': 3, 'type': 'Bilan', 'sens': 'Débit'},
    
    {'numero': '35', 'libelle': 'Produits finis', 'classe': 3, 'type': 'Bilan', 'sens': 'Débit'},
    {'numero': '351', 'libelle': 'Produits A', 'classe': 3, 'type': 'Bilan', 'sens': 'Débit'},
    {'numero': '352', 'libelle': 'Produits B', 'classe': 3, 'type': 'Bilan', 'sens': 'Débit'},
    
    # Classe 4 - Comptes de tiers
    {'numero': '40', 'libelle': 'Fournisseurs et comptes rattachés', 'classe': 4, 'type': 'Bilan', 'sens': 'Crédit'},
    {'numero': '401', 'libelle': 'Fournisseurs d\'exploitation', 'classe': 4, 'type': 'Bilan', 'sens': 'Crédit'},
    {'numero': '4011', 'libelle': 'Fournisseurs - Achats de biens et prestations de services', 'classe': 4, 'type': 'Bilan', 'sens': 'Crédit'},
    {'numero': '402', 'libelle': 'Fournisseurs d\'investissements', 'classe': 4, 'type': 'Bilan', 'sens': 'Crédit'},
    {'numero': '408', 'libelle': 'Fournisseurs - Factures non parvenues', 'classe': 4, 'type': 'Bilan', 'sens': 'Crédit'},
    
    {'numero': '41', 'libelle': 'Clients et comptes rattachés', 'classe': 4, 'type': 'Bilan', 'sens': 'Débit'},
    {'numero': '411', 'libelle': 'Clients', 'classe': 4, 'type': 'Bilan', 'sens': 'Débit'},
    {'numero': '4111', 'libelle': 'Clients - Ventes de biens et prestations de services', 'classe': 4, 'type': 'Bilan', 'sens': 'Débit'},
    {'numero': '416', 'libelle': 'Clients douteux', 'classe': 4, 'type': 'Bilan', 'sens': 'Débit'},
    {'numero': '418', 'libelle': 'Clients - Factures à établir', 'classe': 4, 'type': 'Bilan', 'sens': 'Débit'},
    
    {'numero': '42', 'libelle': 'Personnel', 'classe': 4, 'type': 'Bilan', 'sens': 'Crédit'},
    {'numero': '421', 'libelle': 'Personnel - Avances et acomptes', 'classe': 4, 'type': 'Bilan', 'sens': 'Débit'},
    {'numero': '422', 'libelle': 'Commissions et courtages à payer', 'classe': 4, 'type': 'Bilan', 'sens': 'Crédit'},
    {'numero': '423', 'libelle': 'Personnel - Rémunérations dues', 'classe': 4, 'type': 'Bilan', 'sens': 'Crédit'},
    {'numero': '424', 'libelle': 'Personnel - Œuvres sociales', 'classe': 4, 'type': 'Bilan', 'sens': 'Crédit'},
    {'numero': '425', 'libelle': 'Personnel - Oppositions sur salaires', 'classe': 4, 'type': 'Bilan', 'sens': 'Crédit'},
    {'numero': '427', 'libelle': 'Personnel - Dépôts', 'classe': 4, 'type': 'Bilan', 'sens': 'Crédit'},
    
    {'numero': '43', 'libelle': 'Organismes sociaux', 'classe': 4, 'type': 'Bilan', 'sens': 'Crédit'},
    {'numero': '431', 'libelle': 'Sécurité sociale', 'classe': 4, 'type': 'Bilan', 'sens': 'Crédit'},
    {'numero': '432', 'libelle': 'Caisses de retraite', 'classe': 4, 'type': 'Bilan', 'sens': 'Crédit'},
    {'numero': '438', 'libelle': 'Autres organismes sociaux', 'classe': 4, 'type': 'Bilan', 'sens': 'Crédit'},
    
    {'numero': '44', 'libelle': 'État et collectivités publiques', 'classe': 4, 'type': 'Bilan', 'sens': 'Variable'},
    {'numero': '441', 'libelle': 'État - Subventions à recevoir', 'classe': 4, 'type': 'Bilan', 'sens': 'Débit'},
    {'numero': '442', 'libelle': 'État - Impôts et taxes recouvrables', 'classe': 4, 'type': 'Bilan', 'sens': 'Débit'},
    {'numero': '443', 'libelle': 'Opérations particulières avec l\'État', 'classe': 4, 'type': 'Bilan', 'sens': 'Variable'},
    {'numero': '444', 'libelle': 'État - Impôt sur le résultat', 'classe': 4, 'type': 'Bilan', 'sens': 'Crédit'},
    {'numero': '445', 'libelle': 'État - TVA', 'classe': 4, 'type': 'Bilan', 'sens': 'Variable'},
    {'numero': '4451', 'libelle': 'État - TVA facturée', 'classe': 4, 'type': 'Bilan', 'sens': 'Crédit'},
    {'numero': '4452', 'libelle': 'État - TVA déductible sur achats', 'classe': 4, 'type': 'Bilan', 'sens': 'Débit'},
    {'numero': '4454', 'libelle': 'État - TVA à décaisser', 'classe': 4, 'type': 'Bilan', 'sens': 'Crédit'},
    {'numero': '4456', 'libelle': 'État - TVA à récupérer', 'classe': 4, 'type': 'Bilan', 'sens': 'Débit'},
    {'numero': '447', 'libelle': 'État - Autres impôts et taxes', 'classe': 4, 'type': 'Bilan', 'sens': 'Crédit'},
    
    {'numero': '46', 'libelle': 'Débiteurs et créditeurs divers', 'classe': 4, 'type': 'Bilan', 'sens': 'Variable'},
    {'numero': '461', 'libelle': 'Créances sur cessions d\'immobilisations', 'classe': 4, 'type': 'Bilan', 'sens': 'Débit'},
    {'numero': '462', 'libelle': 'Créances sur cessions de titres', 'classe': 4, 'type': 'Bilan', 'sens': 'Débit'},
    {'numero': '465', 'libelle': 'Créances sur cessions de valeurs mobilières de placement', 'classe': 4, 'type': 'Bilan', 'sens': 'Débit'},
    {'numero': '467', 'libelle': 'Autres comptes débiteurs', 'classe': 4, 'type': 'Bilan', 'sens': 'Débit'},
    {'numero': '4671', 'libelle': 'Débiteurs divers', 'classe': 4, 'type': 'Bilan', 'sens': 'Débit'},
    {'numero': '468', 'libelle': 'Divers créditeurs', 'classe': 4, 'type': 'Bilan', 'sens': 'Crédit'},
    
    {'numero': '47', 'libelle': 'Comptes transitoires ou d\'attente', 'classe': 4, 'type': 'Bilan', 'sens': 'Variable'},
    {'numero': '471', 'libelle': 'Comptes d\'attente - Opérations faites', 'classe': 4, 'type': 'Bilan', 'sens': 'Variable'},
    {'numero': '472', 'libelle': 'Attente de régularisation', 'classe': 4, 'type': 'Bilan', 'sens': 'Variable'},
    
    # Classe 5 - Comptes de trésorerie
    {'numero': '50', 'libelle': 'Titres de placement', 'classe': 5, 'type': 'Bilan', 'sens': 'Débit'},
    {'numero': '501', 'libelle': 'Parts dans des entreprises liées', 'classe': 5, 'type': 'Bilan', 'sens': 'Débit'},
    {'numero': '502', 'libelle': 'Actions', 'classe': 5, 'type': 'Bilan', 'sens': 'Débit'},
    {'numero': '503', 'libelle': 'Obligations', 'classe': 5, 'type': 'Bilan', 'sens': 'Débit'},
    {'numero': '508', 'libelle': 'Autres titres de placement', 'classe': 5, 'type': 'Bilan', 'sens': 'Débit'},
    
    {'numero': '52', 'libelle': 'Banques', 'classe': 5, 'type': 'Bilan', 'sens': 'Débit'},
    {'numero': '521', 'libelle': 'Banques locales', 'classe': 5, 'type': 'Bilan', 'sens': 'Débit'},
    {'numero': '5211', 'libelle': 'Banque X', 'classe': 5, 'type': 'Bilan', 'sens': 'Débit'},
    {'numero': '5212', 'libelle': 'Banque Y', 'classe': 5, 'type': 'Bilan', 'sens': 'Débit'},
    {'numero': '522', 'libelle': 'Banques autres', 'classe': 5, 'type': 'Bilan', 'sens': 'Débit'},
    
    {'numero': '53', 'libelle': 'Établissements financiers et assimilés', 'classe': 5, 'type': 'Bilan', 'sens': 'Débit'},
    {'numero': '531', 'libelle': 'Chèques postaux', 'classe': 5, 'type': 'Bilan', 'sens': 'Débit'},
    {'numero': '532', 'libelle': 'Trésor', 'classe': 5, 'type': 'Bilan', 'sens': 'Débit'},
    {'numero': '538', 'libelle': 'Autres établissements financiers', 'classe': 5, 'type': 'Bilan', 'sens': 'Débit'},
    
    {'numero': '54', 'libelle': 'Instruments de trésorerie', 'classe': 5, 'type': 'Bilan', 'sens': 'Débit'},
    
    {'numero': '57', 'libelle': 'Caisse', 'classe': 5, 'type': 'Bilan', 'sens': 'Débit'},
    {'numero': '571', 'libelle': 'Caisse siège social', 'classe': 5, 'type': 'Bilan', 'sens': 'Débit'},
    {'numero': '572', 'libelle': 'Caisse succursale A', 'classe': 5, 'type': 'Bilan', 'sens': 'Débit'},
    {'numero': '573', 'libelle': 'Caisse succursale B', 'classe': 5, 'type': 'Bilan', 'sens': 'Débit'},
    
    {'numero': '58', 'libelle': 'Régies d\'avances, accréditifs et virements internes', 'classe': 5, 'type': 'Bilan', 'sens': 'Débit'},
    {'numero': '581', 'libelle': 'Régies d\'avances', 'classe': 5, 'type': 'Bilan', 'sens': 'Débit'},
    {'numero': '582', 'libelle': 'Accréditifs', 'classe': 5, 'type': 'Bilan', 'sens': 'Débit'},
    {'numero': '585', 'libelle': 'Virements de fonds', 'classe': 5, 'type': 'Bilan', 'sens': 'Débit'},
    
    # Classe 6 - Comptes de charges
    {'numero': '60', 'libelle': 'Achats et variations de stocks', 'classe': 6, 'type': 'Gestion', 'sens': 'Débit'},
    {'numero': '601', 'libelle': 'Achats de marchandises', 'classe': 6, 'type': 'Gestion', 'sens': 'Débit'},
    {'numero': '602', 'libelle': 'Achats de matières premières', 'classe': 6, 'type': 'Gestion', 'sens': 'Débit'},
    {'numero': '604', 'libelle': 'Achats stockés de matières et fournitures consommables', 'classe': 6, 'type': 'Gestion', 'sens': 'Débit'},
    {'numero': '605', 'libelle': 'Autres achats', 'classe': 6, 'type': 'Gestion', 'sens': 'Débit'},
    
    {'numero': '61', 'libelle': 'Transports', 'classe': 6, 'type': 'Gestion', 'sens': 'Débit'},
    {'numero': '611', 'libelle': 'Transports sur achats', 'classe': 6, 'type': 'Gestion', 'sens': 'Débit'},
    {'numero': '612', 'libelle': 'Transports sur ventes', 'classe': 6, 'type': 'Gestion', 'sens': 'Débit'},
    {'numero': '614', 'libelle': 'Transports du personnel', 'classe': 6, 'type': 'Gestion', 'sens': 'Débit'},
    {'numero': '618', 'libelle': 'Autres frais de transport', 'classe': 6, 'type': 'Gestion', 'sens': 'Débit'},
    
    {'numero': '62', 'libelle': 'Services extérieurs A', 'classe': 6, 'type': 'Gestion', 'sens': 'Débit'},
    {'numero': '621', 'libelle': 'Sous-traitance générale', 'classe': 6, 'type': 'Gestion', 'sens': 'Débit'},
    {'numero': '622', 'libelle': 'Locations et charges locatives', 'classe': 6, 'type': 'Gestion', 'sens': 'Débit'},
    {'numero': '623', 'libelle': 'Redevances de crédit-bail', 'classe': 6, 'type': 'Gestion', 'sens': 'Débit'},
    {'numero': '624', 'libelle': 'Entretien, réparations et maintenance', 'classe': 6, 'type': 'Gestion', 'sens': 'Débit'},
    {'numero': '625', 'libelle': 'Primes d\'assurances', 'classe': 6, 'type': 'Gestion', 'sens': 'Débit'},
    {'numero': '626', 'libelle': 'Études, recherches et documentation', 'classe': 6, 'type': 'Gestion', 'sens': 'Débit'},
    {'numero': '627', 'libelle': 'Publicité, publications et relations publiques', 'classe': 6, 'type': 'Gestion', 'sens': 'Débit'},
    {'numero': '628', 'libelle': 'Frais de télécommunications', 'classe': 6, 'type': 'Gestion', 'sens': 'Débit'},
    
    {'numero': '63', 'libelle': 'Services extérieurs B', 'classe': 6, 'type': 'Gestion', 'sens': 'Débit'},
    {'numero': '631', 'libelle': 'Frais bancaires', 'classe': 6, 'type': 'Gestion', 'sens': 'Débit'},
    {'numero': '632', 'libelle': 'Rémunérations d\'intermédiaires et de conseils', 'classe': 6, 'type': 'Gestion', 'sens': 'Débit'},
    {'numero': '633', 'libelle': 'Frais de formation du personnel', 'classe': 6, 'type': 'Gestion', 'sens': 'Débit'},
    {'numero': '634', 'libelle': 'Redevances pour brevets, licences, logiciels', 'classe': 6, 'type': 'Gestion', 'sens': 'Débit'},
    {'numero': '635', 'libelle': 'Cotisations', 'classe': 6, 'type': 'Gestion', 'sens': 'Débit'},
    {'numero': '637', 'libelle': 'Rémunérations de personnel extérieur', 'classe': 6, 'type': 'Gestion', 'sens': 'Débit'},
    {'numero': '638', 'libelle': 'Autres charges externes', 'classe': 6, 'type': 'Gestion', 'sens': 'Débit'},
    
    {'numero': '64', 'libelle': 'Impôts et taxes', 'classe': 6, 'type': 'Gestion', 'sens': 'Débit'},
    {'numero': '641', 'libelle': 'Impôts et taxes directs', 'classe': 6, 'type': 'Gestion', 'sens': 'Débit'},
    {'numero': '642', 'libelle': 'Impôts et taxes indirects', 'classe': 6, 'type': 'Gestion', 'sens': 'Débit'},
    {'numero': '645', 'libelle': 'Autres impôts et taxes', 'classe': 6, 'type': 'Gestion', 'sens': 'Débit'},
    
    {'numero': '66', 'libelle': 'Charges de personnel', 'classe': 6, 'type': 'Gestion', 'sens': 'Débit'},
    {'numero': '661', 'libelle': 'Appointements, salaires et commissions', 'classe': 6, 'type': 'Gestion', 'sens': 'Débit'},
    {'numero': '662', 'libelle': 'Primes et gratifications', 'classe': 6, 'type': 'Gestion', 'sens': 'Débit'},
    {'numero': '663', 'libelle': 'Indemnités de congés payés', 'classe': 6, 'type': 'Gestion', 'sens': 'Débit'},
    {'numero': '664', 'libelle': 'Charges sociales', 'classe': 6, 'type': 'Gestion', 'sens': 'Débit'},
    {'numero': '665', 'libelle': 'Autres charges sociales', 'classe': 6, 'type': 'Gestion', 'sens': 'Débit'},
    {'numero': '667', 'libelle': 'Rémunérations transférées de charges', 'classe': 6, 'type': 'Gestion', 'sens': 'Débit'},
    {'numero': '668', 'libelle': 'Autres charges de personnel', 'classe': 6, 'type': 'Gestion', 'sens': 'Débit'},
    
    {'numero': '67', 'libelle': 'Frais financiers et charges assimilées', 'classe': 6, 'type': 'Gestion', 'sens': 'Débit'},
    {'numero': '671', 'libelle': 'Intérêts des emprunts', 'classe': 6, 'type': 'Gestion', 'sens': 'Débit'},
    {'numero': '672', 'libelle': 'Intérêts dans loyers de crédit-bail', 'classe': 6, 'type': 'Gestion', 'sens': 'Débit'},
    {'numero': '673', 'libelle': 'Escomptes accordés', 'classe': 6, 'type': 'Gestion', 'sens': 'Débit'},
    {'numero': '674', 'libelle': 'Autres frais financiers', 'classe': 6, 'type': 'Gestion', 'sens': 'Débit'},
    {'numero': '676', 'libelle': 'Pertes de change', 'classe': 6, 'type': 'Gestion', 'sens': 'Débit'},
    {'numero': '678', 'libelle': 'Autres charges financières', 'classe': 6, 'type': 'Gestion', 'sens': 'Débit'},
    
    {'numero': '68', 'libelle': 'Dotations aux amortissements', 'classe': 6, 'type': 'Gestion', 'sens': 'Débit'},
    {'numero': '681', 'libelle': 'Dotations aux amortissements d\'exploitation', 'classe': 6, 'type': 'Gestion', 'sens': 'Débit'},
    {'numero': '687', 'libelle': 'Dotations aux amortissements financiers', 'classe': 6, 'type': 'Gestion', 'sens': 'Débit'},
    
    # Classe 7 - Comptes de produits
    {'numero': '70', 'libelle': 'Ventes', 'classe': 7, 'type': 'Gestion', 'sens': 'Crédit'},
    {'numero': '701', 'libelle': 'Ventes de marchandises', 'classe': 7, 'type': 'Gestion', 'sens': 'Crédit'},
    {'numero': '702', 'libelle': 'Ventes de produits finis', 'classe': 7, 'type': 'Gestion', 'sens': 'Crédit'},
    {'numero': '703', 'libelle': 'Ventes de produits intermédiaires', 'classe': 7, 'type': 'Gestion', 'sens': 'Crédit'},
    {'numero': '704', 'libelle': 'Ventes de produits résiduels', 'classe': 7, 'type': 'Gestion', 'sens': 'Crédit'},
    {'numero': '706', 'libelle': 'Prestations de services', 'classe': 7, 'type': 'Gestion', 'sens': 'Crédit'},
    {'numero': '707', 'libelle': 'Produits accessoires', 'classe': 7, 'type': 'Gestion', 'sens': 'Crédit'},
    
    {'numero': '71', 'libelle': 'Subventions d\'exploitation', 'classe': 7, 'type': 'Gestion', 'sens': 'Crédit'},
    {'numero': '711', 'libelle': 'Subventions d\'équilibre', 'classe': 7, 'type': 'Gestion', 'sens': 'Crédit'},
    
    {'numero': '72', 'libelle': 'Production immobilisée', 'classe': 7, 'type': 'Gestion', 'sens': 'Crédit'},
    {'numero': '721', 'libelle': 'Immobilisations incorporelles', 'classe': 7, 'type': 'Gestion', 'sens': 'Crédit'},
    {'numero': '722', 'libelle': 'Immobilisations corporelles', 'classe': 7, 'type': 'Gestion', 'sens': 'Crédit'},
    
    {'numero': '73', 'libelle': 'Variations de stocks de biens et services produits', 'classe': 7, 'type': 'Gestion', 'sens': 'Crédit'},
    {'numero': '734', 'libelle': 'Variation des en-cours', 'classe': 7, 'type': 'Gestion', 'sens': 'Crédit'},
    {'numero': '735', 'libelle': 'Variation des stocks de produits', 'classe': 7, 'type': 'Gestion', 'sens': 'Crédit'},
    
    {'numero': '75', 'libelle': 'Autres produits', 'classe': 7, 'type': 'Gestion', 'sens': 'Crédit'},
    {'numero': '754', 'libelle': 'Ristournes perçues', 'classe': 7, 'type': 'Gestion', 'sens': 'Crédit'},
    {'numero': '758', 'libelle': 'Produits divers', 'classe': 7, 'type': 'Gestion', 'sens': 'Crédit'},
    
    {'numero': '77', 'libelle': 'Revenus financiers et produits assimilés', 'classe': 7, 'type': 'Gestion', 'sens': 'Crédit'},
    {'numero': '771', 'libelle': 'Intérêts de prêts', 'classe': 7, 'type': 'Gestion', 'sens': 'Crédit'},
    {'numero': '772', 'libelle': 'Revenus de participations', 'classe': 7, 'type': 'Gestion', 'sens': 'Crédit'},
    {'numero': '773', 'libelle': 'Escomptes obtenus', 'classe': 7, 'type': 'Gestion', 'sens': 'Crédit'},
    {'numero': '776', 'libelle': 'Gains de change', 'classe': 7, 'type': 'Gestion', 'sens': 'Crédit'},
    {'numero': '778', 'libelle': 'Autres produits financiers', 'classe': 7, 'type': 'Gestion', 'sens': 'Crédit'},
    
    # Classe 8 - Comptes des autres charges et produits
    {'numero': '81', 'libelle': 'Valeurs comptables des cessions d\'immobilisations', 'classe': 8, 'type': 'Gestion', 'sens': 'Débit'},
    {'numero': '811', 'libelle': 'Immobilisations incorporelles', 'classe': 8, 'type': 'Gestion', 'sens': 'Débit'},
    {'numero': '812', 'libelle': 'Immobilisations corporelles', 'classe': 8, 'type': 'Gestion', 'sens': 'Débit'},
    
    {'numero': '82', 'libelle': 'Produits de cessions d\'immobilisations', 'classe': 8, 'type': 'Gestion', 'sens': 'Crédit'},
    {'numero': '821', 'libelle': 'Immobilisations incorporelles', 'classe': 8, 'type': 'Gestion', 'sens': 'Crédit'},
    {'numero': '822', 'libelle': 'Immobilisations corporelles', 'classe': 8, 'type': 'Gestion', 'sens': 'Crédit'},
    
    {'numero': '83', 'libelle': 'Charges hors activités ordinaires', 'classe': 8, 'type': 'Gestion', 'sens': 'Débit'},
    {'numero': '831', 'libelle': 'Charges HAO constatées', 'classe': 8, 'type': 'Gestion', 'sens': 'Débit'},
    
    {'numero': '84', 'libelle': 'Produits hors activités ordinaires', 'classe': 8, 'type': 'Gestion', 'sens': 'Crédit'},
    {'numero': '841', 'libelle': 'Produits HAO constatés', 'classe': 8, 'type': 'Gestion', 'sens': 'Crédit'},
    
    {'numero': '85', 'libelle': 'Dotations hors activités ordinaires', 'classe': 8, 'type': 'Gestion', 'sens': 'Débit'},
    {'numero': '851', 'libelle': 'Dotations aux amortissements HAO', 'classe': 8, 'type': 'Gestion', 'sens': 'Débit'},
    
    {'numero': '87', 'libelle': 'Participations des travailleurs', 'classe': 8, 'type': 'Gestion', 'sens': 'Débit'},
    {'numero': '871', 'libelle': 'Participation des travailleurs', 'classe': 8, 'type': 'Gestion', 'sens': 'Débit'},
    
    {'numero': '89', 'libelle': 'Impôts sur le résultat', 'classe': 8, 'type': 'Gestion', 'sens': 'Débit'},
    {'numero': '891', 'libelle': 'Impôt sur le bénéfice', 'classe': 8, 'type': 'Gestion', 'sens': 'Débit'},
]

# Plan comptable SYCEBNL (pour les entités à but non lucratif)
PLAN_COMPTABLE_SYCEBNL = [
    # Le SYCEBNL partage la plupart des comptes avec SYSCOHADA
    # avec quelques spécificités pour les entités à but non lucratif
    
    # Ajouts spécifiques SYCEBNL
    {'numero': '13', 'libelle': 'Fonds dédiés', 'classe': 1, 'type': 'Bilan', 'sens': 'Crédit'},
    {'numero': '131', 'libelle': 'Fonds dédiés projet A', 'classe': 1, 'type': 'Bilan', 'sens': 'Crédit'},
    {'numero': '132', 'libelle': 'Fonds dédiés projet B', 'classe': 1, 'type': 'Bilan', 'sens': 'Crédit'},
    
    {'numero': '45', 'libelle': 'Donateurs et bailleurs de fonds', 'classe': 4, 'type': 'Bilan', 'sens': 'Variable'},
    {'numero': '451', 'libelle': 'Donateurs privés', 'classe': 4, 'type': 'Bilan', 'sens': 'Débit'},
    {'numero': '452', 'libelle': 'Bailleurs institutionnels', 'classe': 4, 'type': 'Bilan', 'sens': 'Débit'},
    {'numero': '453', 'libelle': 'Subventions à recevoir', 'classe': 4, 'type': 'Bilan', 'sens': 'Débit'},
    
    {'numero': '74', 'libelle': 'Dons et contributions', 'classe': 7, 'type': 'Gestion', 'sens': 'Crédit'},
    {'numero': '741', 'libelle': 'Dons en nature', 'classe': 7, 'type': 'Gestion', 'sens': 'Crédit'},
    {'numero': '742', 'libelle': 'Dons en espèces', 'classe': 7, 'type': 'Gestion', 'sens': 'Crédit'},
    {'numero': '743', 'libelle': 'Subventions reçues', 'classe': 7, 'type': 'Gestion', 'sens': 'Crédit'},
    {'numero': '744', 'libelle': 'Cotisations des membres', 'classe': 7, 'type': 'Gestion', 'sens': 'Crédit'},
]
