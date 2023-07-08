import hashlib
import logging
import random
import string
import time
from tqdm import tqdm


def load_common_passwords(file_path):
    with open(file_path, 'r') as file:
        common_passwords = [line.strip() for line in file]
    return common_passwords


common_passwords = load_common_passwords('mots.txt')


def generate_password():
    length = random.randint(4, 12)
    characters = string.ascii_letters + string.digits + string.punctuation
    password = random.choice(common_passwords) if random.randint(0, 10) < 3 else ''.join(random.choice(characters) for _ in range(length))
    return password


def hash_password(password, algorithm):
    if algorithm == 'md5':
        hashed_password = hashlib.md5(password.encode()).hexdigest()
    elif algorithm == 'sha1':
        hashed_password = hashlib.sha1(password.encode()).hexdigest()
    elif algorithm == 'sha256':
        hashed_password = hashlib.sha256(password.encode()).hexdigest()
    elif algorithm == 'sha512':
        hashed_password = hashlib.sha512(password.encode()).hexdigest()
    elif algorithm == 'sha3_256':  # Algorithme SHA-3 256
        hashed_password = hashlib.sha3_256(password.encode()).hexdigest()
    else:
        raise ValueError('Invalid algorithm specified')
    return hashed_password


def compare_hashes(num_tests, target_hash):
    logging.basicConfig(filename='./logs.log', level=logging.INFO,
                        format='%(asctime)s - %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S')
    logger = logging.getLogger()

    start_time = time.time()
    found = False
    with tqdm(total=num_tests) as pbar:
        for _ in range(num_tests):
            password = generate_password()
            algorithms = ['md5', 'sha1', 'sha256', 'sha512', 'sha3_256']
            log_message = f"Testing password: {password} with algorithm: {algorithms}"
            logger.info(log_message)
            for algorithm in algorithms:
                hashed_password = hash_password(password, algorithm)
                if str(hashed_password) == target_hash:
                    found = True
                    break
            if found:
                break
            #pbar.set_postfix({'Password': password})
            pbar.update(1)

    if found:
        print(f"\nFound matching password: {password}")
    else:
        print("\nNo matching password found.")


# Exemple d'utilisation des fonctions
if __name__ == '__main__':
    num_tests = int(input("Combien de mots de passe souhaitez-vous tester ? "))
    target_hash = input("Entrez l'empreinte à comparer : ")
    compare_hashes(num_tests, str(target_hash))
