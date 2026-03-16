from pathlib import Path

# ── Paths ────────────────────────────────────────────────────────────────────
BASE = #EDITED FOR SECURITY PURPOSES
RAW  = BASE / "data" / "raw"
PROC = BASE / "data" / "processed"

BPE_PATH    = RAW / "bpe"           / "BPE24" / "BPE24.csv"
FILO_PATH   = RAW / "filosofi"      / "base-cc-filosofi-2021-geo2025_csv" / "DS_FILOSOFI_CC_data.csv"
ACCESS_PATH = RAW / "accessibility" / "donnees-2024-reg11.parquet"
ADMIN_PATH  = RAW / "admin"         / "ADE-COG_4-0_GPKG_LAMB93_FXX-ED2025-01-01.gpkg"
CENSUS_PATH = RAW / "census"        /"base-ic-evol-struct-pop-2022_csv" / "base-ic-evol-struct-pop-2022.csv"

# ── Database ──────────────────────────────────────────────────────────────────
# Note: eai_score column in DB retains original name for consistency
# Display name is "Indice de proximité aux services (IPS)"
DB_URL = #EDITED FOR SECURITY PURPOSES

# ── IDF scope ─────────────────────────────────────────────────────────────────
IDF_DEPS = ['75', '77', '78', '91', '92', '93', '94', '95']
IDF_REG  = '11'

# ── Column mappings ───────────────────────────────────────────────────────────
BPE_RENAME = {
    'LAMBERT_X': 'X',
    'LAMBERT_Y': 'Y',
    'DEPCOM':    'insee_com',
    'DEP':       'dep',
    'TYPEQU':    'typequ'
}

FILO_RENAME = {
    'GEO':        'insee_com',
    'DEC_MED21':  'med_income_2021',
    'DEC_TP6021': 'poverty_rate',
    'DEC_D121':   'd1_income',
    'DEC_D921':   'd9_income',
    'DEC_GI21':   'gini'
}

CENSUS_KEEP = {
    'COM':         'insee_com',
    'P22_POP':     'pop_total',
    'P22_POP65P':  'pop_65plus',
    'P22_POP0014': 'pop_0014',
    'P22_POP_IMM': 'pop_immigrant',
    'P22_PMEN':    'pop_households'
}

ACCESS_KEEP = ['depcom', 'typeeq_id', 'duree', 'pop', 'domaine']

# ── Facility types ─────────────────────────────────────────────────────────────
# Maps TYPEQU code → specific indicator name
# Where multiple codes share a name they are treated as one combined indicator
FACILITY_TYPES = {

    # ── Security ──────────────────────────────────────────────────────────────
    'A101': 'security',               # Police
    'A104': 'security',               # Gendarmerie

    # ── Food access ───────────────────────────────────────────────────────────
    'B104': 'supermarket_large',      # Hypermarché et grand magasin
    'B105': 'supermarket_large',      # Supermarché et magasin multi-commerce
    'B201': 'local_food_shop',        # Supérette
    'B202': 'local_food_shop',        # Épicerie
    'B207': 'boulangerie',            # Boulangerie-pâtisserie

    # ── Education: premier degré ───────────────────────────────────────────────
    'C107': 'school_maternelle',      # École maternelle
    'C108': 'school_primary',         # École primaire
    'C109': 'school_primary',         # École élémentaire

    # ── Education: second degré ────────────────────────────────────────────────
    'C201': 'college',                # Collège
    'C301': 'lycee_general',          # Lycée général et technologique
    'C302': 'lycee_pro',              # Lycée professionnel
    'C303': 'lycee_pro',              # Lycée technique agricole

    # ── Education: supérieur public ────────────────────────────────────────────
    'C401': 'higher_public',          # STS/CPGE
    'C403': 'higher_public',          # Formation commerce
    'C409': 'higher_public',          # Autre post-bac non universitaire
    'C410': 'higher_public',          # École formations sanitaires/sociales
    'C501': 'higher_public',          # UFR
    'C502': 'higher_public',          # Institut universitaire
    'C505': 'higher_public',          # École enseignement supérieur agricole
    'C509': 'higher_public',          # Autre enseignement supérieur
    'C602': 'vocational_training',    # GRETA
    'C604': 'vocational_training',    # Formation aux métiers du sport
    'C610': 'vocational_training',    # Organisme de formation en apprentissage

    # ── Education: supérieur privé ─────────────────────────────────────────────
    'C503': 'higher_private',         # École d'ingénieurs
    'C504': 'higher_private',         # Enseignement supérieur privé général

    # ── Health: core ──────────────────────────────────────────────────────────
    'D265': 'health_gp',              # Médecin généraliste
    'D307': 'health_pharmacy',        # Pharmacie
    'D106': 'health_urgences',        # Urgences

    # ── Health: complementary ─────────────────────────────────────────────────
    'D108': 'health_centre',          # Centre de santé
    'D113': 'health_msp',             # Maison de santé pluridisciplinaire
    'D277': 'health_dental',          # Chirurgien dentiste
    'D281': 'health_nurse',           # Infirmier
    'D302': 'health_lab',             # Laboratoire d'analyses
    'D107': 'health_maternity',       # Maternité
    'D115': 'health_pmi',             # Services santé maternelle et infantile

    # ── Social services ────────────────────────────────────────────────────────
    'D401': 'elderly_care',           # Personnes âgées hébergement
    'D502': 'childcare',              # Établissement accueil jeune enfant
    'D505': 'childcare_loisir',       # Accueil de loisir sans hébergement
    'D506': 'social_centre',          # Centres sociaux

    # ── Transport ─────────────────────────────────────────────────────────────
    'E107': 'train_national',         # Gare nationale
    'E108': 'train_regional',         # Gare régionale
    'E109': 'train_local',            # Gare locale

    # ── Sports ────────────────────────────────────────────────────────────────
    'F101': 'sport_pool',             # Bassin de natation
    'F103': 'sport_other',            # Tennis
    'F107': 'sport_outdoor',          # Athlétisme
    'F109': 'sport_outdoor',          # Parcours sportif/santé
    'F111': 'sport_outdoor',          # Plateaux et terrains de jeux extérieurs
    'F113': 'sport_outdoor',          # Terrains de grands jeux
    'F114': 'sport_other',            # Salles de combat
    'F120': 'sport_other',            # Salles de remise en forme
    'F121': 'sport_indoor',           # Salles multisports, gymnases

    # ── Culture ───────────────────────────────────────────────────────────────
    'F303': 'culture',                # Cinéma
    'F305': 'culture',                # Conservatoire
    'F307': 'culture',                # Bibliothèque
    'F315': 'culture',                # Arts du spectacle

    # ── Postal services ────────────────────────────────────────────────────────
    'A206': 'postal',                 # Bureau de poste
    'A207': 'postal',                 # Relais poste
    'A208': 'postal',                 # Agence postale
}

# ── Groupings for combined nearest-facility queries ───────────────────────────
# Used in Phase 5 when a single indicator spans multiple TYPEQU codes
SCHOOL_PRIMARY_TYPES   = ['C108', 'C109']
SCHOOL_SECONDARY_TYPES = ['C201', 'C301', 'C302', 'C303']
UNIVERSITY_PUBLIC      = ['C401', 'C403', 'C409', 'C410',
                           'C501', 'C502', 'C505', 'C509']
UNIVERSITY_PRIVATE     = ['C503', 'C504']
VOCATIONAL             = ['C602', 'C604', 'C610']
FOOD_LARGE             = ['B104', 'B105']
FOOD_LOCAL             = ['B201', 'B202']
SECURITY               = ['A101', 'A104']
POSTAL                 = ['A206', 'A207', 'A208']
SPORT_OUTDOOR          = ['F107', 'F109', 'F111', 'F113']
HEALTH_CORE            = ['D265', 'D307', 'D106']
HEALTH_COMPLEMENTARY   = ['D108', 'D113', 'D277', 'D281',
                           'D302', 'D107', 'D115']

# ── Index dimensions ──────────────────────────────────────────────────────────
# Two-level hierarchy: dimension → list of specific indicator names
# Level 1 (dimension) = map toggle layer for end users
# Level 2 (indicator) = drill-down detail
#
# NOTE: Filosofi income/poverty data sits OUTSIDE this index as a
# correlation layer — it is not weighted into the EAI score.
# Its role is to answer: "does equipment access correlate with wealth?"

INDEX_DIMENSIONS = {
    'food_access': {
        'indicators': ['supermarket_large', 'local_food_shop', 'boulangerie'],
        'weight': 5,
        'indicator_weights': {'supermarket_large': 4, 'local_food_shop': 2, 'boulangerie': 1}
    },
    'health_core': {
        'indicators': ['health_gp', 'health_pharmacy', 'health_urgences'],
        'weight': 5,
        'indicator_weights': None  # equal weights
    },
    'health_complementary': {
        'indicators': ['health_centre', 'health_msp', 'health_dental',
                       'health_nurse', 'health_lab', 'health_maternity', 'health_pmi'],
        'weight': 2,
        'indicator_weights': None
    },
    'education_primary': {
        'indicators': ['school_maternelle', 'school_primary'],
        'weight': 4,
        'indicator_weights': None  # equal — maternelle and primary equally important
    },
    'education_secondary': {
        'indicators': ['college', 'lycee_general', 'lycee_pro'],
        'weight': 4,
        'indicator_weights': None
    },
    'education_higher': {
        'indicators': ['higher_public', 'higher_private'],
        'weight': 2,
        'indicator_weights': None
    },
    'social_services': {
        'indicators': ['elderly_care', 'childcare', 'childcare_loisir', 'social_centre'],
        'weight': 3,
        'indicator_weights': None
    },
    'transport': {
        'indicators': ['train_national', 'train_regional', 'train_local'],
        'weight': 4,
        'indicator_weights': None
    },
    'sports': {
        'indicators': ['sport_pool', 'sport_outdoor', 'sport_indoor', 'sport_other'],
        'weight': 3,
        'indicator_weights': None
    },
    'culture': {
        'indicators': ['culture'],
        'weight': 3,
        'indicator_weights': None
    },
    'public_services': {
        'indicators': ['security', 'postal'],
        'weight': 1,
        'indicator_weights': None
    },
}

# Aggregation methods per indicator group
AGGREGATION_METHODS = {
    # MIN across codes
    'security':          ('min', None),
    'supermarket_large': ('min', None),
    'local_food_shop':   ('min', None),
    'school_primary':    ('min', None),
    'lycee_pro':         ('min', None),
    'higher_private':    ('weighted_median', {'C503': 2, 'C504': 1}),
    'vocational_training': ('min', None),
    'sport_outdoor':     ('min', None),
    'postal':            ('min', None),
    # WEIGHTED MEDIAN
    'higher_public':     ('weighted_median', {
                            'C501': 4, 'C502': 4,
                            'C505': 2, 'C509': 2, 'C401': 2,
                            'C410': 1, 'C403': 1, 'C409': 1
                         }),
    'sport_other':       ('median', None),
    'culture': ('weighted_median', {'F307': 3, 'F303': 3, 'F315': 2, 'F305': 1}),
    # SINGLE CODE — no aggregation needed
    # everything else defaults to the single value
}

# Flat list of all unique indicator names — useful for looping in analysis
ALL_INDICATORS = list({v for v in FACILITY_TYPES.values()})

# Correlation layers — loaded and displayed alongside EAI but not scored into it
CORRELATION_INDICATORS = [
    'med_income_2021',
    'poverty_rate',
    'gini',
    'd1_income',
    'd9_income',
    'pop_total',
    'pop_65plus',
    'pop_0014',
]