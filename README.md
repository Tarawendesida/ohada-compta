# OHADA-COMPTA

**Application de comptabilité SYSCOHADA / SYCEBNL pour les pays UEMOA**

[![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/Tarawendesida/ohada-compta)
[![Python](https://img.shields.io/badge/Python-3.11-blue)](https://python.org)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.30+-red)](https://streamlit.io)
[![OHADA](https://img.shields.io/badge/Référentiel-OHADA%202017-green)](https://www.ohada.com)

---

## 📋 Présentation

OHADA-COMPTA est une application web Streamlit de gestion comptable complète, conforme aux normes **SYSCOHADA** (Système Comptable OHADA) et **SYCEBNL** (Entités à But Non Lucratif et Assimilées).

Couvre les 17 États membres de l'OHADA, avec une spécialisation UEMOA (8 pays, zone franc CFA).

---

## ✨ Fonctionnalités

| Page | Description |
|------|-------------|
| 🏢 **Entreprise** | Configuration société, forme juridique, pays, exercice |
| 📒 **Saisie des écritures** | Journal comptable multi-lignes équilibré en temps réel |
| ⚖️ **Balance des comptes** | Balance générale avec totaux et export CSV |
| 📖 **Grand Livre** | Détail par compte avec soldes cumulés |
| 📈 **Compte de résultat** | Produits (Classe 7) vs Charges (Classe 6) |
| 🏦 **Bilan** | Actif / Passif avec contrôle d'équilibre |
| 🧮 **Calculateur fiscal** | IS, IMF, TVA par pays UEMOA en temps réel |
| 📋 **Plan comptable** | Consultation et chargement SYSCOHADA ou SYCEBNL |
| 🏗️ **Demo SCI** | Simulation SCI 132 locaux, 300M FCFA, SYCEBNL |

---

## 🌍 Pays UEMOA supportés

| Code | Pays | TVA | IS |
|------|------|-----|----|
| CI | Côte d'Ivoire | 18% | 25% |
| SN | Sénégal | 18% | 30% |
| ML | Mali | 18% | 30% |
| BF | Burkina Faso | 18% | 27.5% |
| GN | Guinée | 18% | 25% |
| TG | Togo | 18% | 27% |
| BJ | Bénin | 18% | 30% |
| NE | Niger | 19% | 30% |

---

## 🏗️ Simulation SCI (Demo)

La page **Demo SCI** lance une simulation complète d'une Société Civile Immobilière :

- **132 locaux commerciaux** à Abidjan
- **300 000 000 FCFA** de valeur totale
- Référentiel **SYCEBNL** (OHADA 2017)
- Génère automatiquement journaux, balance, compte de résultat et bilan

```python
# Lancer la simulation en ligne de commande
python simulation_sib_sci.py
```

---

## 🚀 Démarrage rapide

### Option 1 — GitHub Codespaces (recommandé)

1. Cliquez **Open in GitHub Codespaces** ci-dessus
2. Attendez l'installation automatique (~2 min)
3. L'application Streamlit s'ouvre sur le port 8501

### Option 2 — Local

```bash
git clone https://github.com/Tarawendesida/ohada-compta.git
cd ohada-compta
pip install -r requirements.txt
streamlit run webapp.py
# → http://localhost:8501
```

---

## 📁 Structure du projet

```
ohada-compta/
├── webapp.py                  # Application Streamlit principale (9 pages)
├── simulation_sib_sci.py      # Simulation SCI 132 locaux / 300M FCFA
├── requirements.txt           # streamlit, pandas, plotly
├── .devcontainer/
│   └── devcontainer.json      # Codespaces: Python 3.11 + auto-launch
└── src/
    ├── database.py            # SQLite — CRUD complet (écritures, comptes, journaux)
    └── data/
        ├── referentiels.py    # Pays UEMOA, formes juridiques, taux fiscaux
        └── plan_comptable.py  # Plan comptable SYSCOHADA + SYCEBNL complet
```

---

## 📐 Architecture comptable

```
Écriture
  └── Lignes (débit / crédit)
        └── Plan comptable (SYSCOHADA ou SYCEBNL)
              └── Classes 1–8 (Ressources, Actifs, Tiers, Trésorerie, Charges, Produits)
```

La base SQLite (`ohada_compta.db`) est créée automatiquement au premier lancement.

---

## 📊 Référentiels intégrés

- **SYSCOHADA** — Acte uniforme OHADA relatif au droit comptable (révisé 2017)
- **SYCEBNL** — Pour associations, ONG, fondations, SCI, entités non-lucratives
- **Formes juridiques** : SA, SARL, SAS, SNC, SCI, GIE, Association, ONG, Fondation
- **Régimes fiscaux** : Réel normal, Réel simplifié, Forfait, Microentreprise

---

## 🔗 Liens

- [OHADA.com — Textes officiels](https://www.ohada.com)
- [UEMOA — Zone franc CFA](https://www.uemoa.int)
- [BCEAO — Politique monétaire](https://www.bceao.int)
- [WASI Backend API](https://github.com/Tarawendesida/wasi-backend-api)
- [WASI Frontend](https://github.com/Tarawendesida/wasi-frontend)
