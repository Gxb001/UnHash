import hashlib
from faker import Faker
from tqdm import tqdm
import random
import string

def generer_mot():
    fake = Faker(['fr_FR', 'en_US'])

    if random.choices([True, False], weights=[1, 1])[0]:
        mot = fake.word()
    else:
        mot = fake.unique.word()

        if random.choices([True, False], weights=[1, 1])[0]:
            nombre = fake.random_int(0, 99)
            mot += str(nombre)

    return mot


def generer_mot_de_passe(longueur):
    fake = Faker(['fr_FR', 'en_US'])

    caracteres = string.ascii_letters + string.digits + string.punctuation

    mots = []
    mots.append(fake.unique.word())

    while len(''.join(mots)) < longueur:
        mot = fake.word()
        mots.append(mot)

        if random.choices([True, False], weights=[1, 1])[0]:
            nombre = fake.random_int(0, 99)
            mots.append(str(nombre))

    mot_de_passe = ''.join(mots)
    mot_de_passe = ''.join(random.sample(mot_de_passe, len(mot_de_passe)))  # Mélanger les caractères

    mot_de_passe = ''.join(random.choice(caracteres) if c.isalpha() else c for c in mot_de_passe)

    return mot_de_passe[:longueur]


def lire_mots_et_verifier_empreinte(mot, empreintes):
    algorithmes_hachage = ['md5', 'sha1', 'sha256']
    for algo, empreinte in empreintes.items():
        h = hashlib.new(algo)
        h.update(mot.encode('utf-8'))
        empreinte_calculée = h.hexdigest()
        if empreinte_calculée == empreinte:
            return (True, mot, algo)
    return (False, "", "")


def executer_generateur(n, hash):
    total_iterations = n
    progress_bar = tqdm(total=total_iterations, ncols=100)

    mots = set()
    empreintes = {}

    count = 0
    while count < total_iterations:
        if random.choices([True, False], weights=[1, 1])[0]:
            mot = generer_mot()
            ok = lire_mots_et_verifier_empreinte(mot, empreintes)
        else:
            rdm = random.randint(4, 12)
            mot_de_passe = generer_mot_de_passe(rdm)
            ok = lire_mots_et_verifier_empreinte(mot_de_passe, empreintes)

        count += 1
        progress_bar.update(1)
        progress_bar.set_description("Progression")
        if ok[0]:
            print(f"L'empreinte du mot '{ok[1]}' correspond à l'empreinte fournie avec l'algorithme {ok[2]}.")
            break
        elif count == total_iterations:
            print("Aucun mot n'a été trouvé pour cette empreinte.")
            break

    progress_bar.close()


def hasher_mot_de_passe(mot_de_passe):  # sha256
    hasher = hashlib.sha256()
    hasher.update(mot_de_passe.encode('utf-8'))
    mot_de_passe_hashe = hasher.hexdigest()
    return mot_de_passe_hashe


# Exemple d'exécution avec 5 générations
# print(hasher_mot_de_passe("hello71"))



empreintes = {
    'md5': hash,
    'sha1': hash,
    'sha256': hash
}
hash = input("Quel est le hash à tester : ")
nb = int(input("Combien de mots de passe voulez-vous tester : "))
executer_generateur(nb, empreintes)
#print(hasher_mot_de_passe("Uhgè7_"))
