import random
from .syllables import split_syllables, phonetic_mutate, syllable_structure, is_valid

import nltk
from nltk.corpus import words

# ----------------------------Prénom-------------------------------
def build_markov_model(corpus):
    model = {'__start__': [], '__end__': []}
    for name in corpus:
        syllables = split_syllables(name)
        if not syllables:
            continue
        model['__start__'].append(syllables[0])
        model.setdefault(syllables[-1], []).append('__end__')
        for i in range(len(syllables) - 1):
            model.setdefault(syllables[i], []).append(syllables[i + 1])
    for key in model:
        model[key] = list(set(model[key]))
    return model

def generate_from_model(model, max_syll=4):
    for _ in range(20):
        sylls = []
        current = random.choice(model['__start__'])
        sylls.append(current)
        while len(sylls) < max_syll:
            next_choices = model.get(current, [])
            if not next_choices:
                break
            next_syll = random.choice(next_choices)
            if next_syll == '__end__':
                break
            sylls.append(next_syll)
            current = next_syll
        if 2 <= len(sylls) <= max_syll:
            return ''.join(sylls).capitalize()
    return "Nameless"

def generate_name(model):
    target_structures = ["CVCV", "VCV", "CVVC", "CVCC"]
    for _ in range(50):
        name = generate_from_model(model)
        name = phonetic_mutate(name)
        struct = syllable_structure(name)
        if is_valid(name) and any(struct.startswith(ts) for ts in target_structures):
            return name
    return "Nameless"

# ----------------------------Nom famille-------------------------------
nltk.download('words', quiet=True)
english_words = set(words.words())

# Lire les données du fichier
with open("data/noms_famille.txt", "r") as f:
    base_surnames = [line.strip().capitalize() for line in f if line.strip()]

with open("data/prenoms_garcons.txt", "r") as f:
    first_names_m = [line.strip().capitalize() for line in f if line.strip()]

with open("data/prenoms_filles.txt", "r") as f:
    first_names_f = [line.strip().capitalize() for line in f if line.strip()]

# Suffixes et préfixes courants
suffixes = [
    'man', 'ton', 'wood', 'field', 'worth', 'well', 'white', 'brown',
    'er', 'smith', 'ham', 'ford', 'ley', 'brook', 'house', 'stone'
]
suffixes_son= [
    'es', 'ez', 'sen', 'son', 'is', 'os'
]
prefixes = [
    'Mac', "O'", 'Fitz', 'Mc',
    'Ap', 'De', 'Del', 'Van', 'Von', 'St.', 'La', 'Le', 'Al'
]

# Filtrer les noms de famille significatifs
meaningful_bases = [name for name in base_surnames if name.lower() in english_words]


def generate_surname():
    mode = random.choice(['meaning', 'suffix', 'prefix'])

    if mode == 'meaning':
        if meaningful_bases:
            return random.choice(meaningful_bases)
    elif mode == 'suffix':
        if meaningful_bases:
            return random.choice(meaningful_bases) + random.choice(suffixes)
    elif mode == 'prefix':
        base_name = random.choice(first_names_m + first_names_f)
        return random.choice(prefixes) + base_name
    elif mode == 'suffix_son':
        base_name = random.choice(first_names_m)
        return base_name + random.choice(suffixes_son)

    # Fallback 
    return random.choice(base_surnames)


