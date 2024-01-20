# Password Recovery Tool

This Python script serves as a password recovery tool, attempting to find a password that matches a given hash. It supports various hashing algorithms, including MD5, SHA-1, SHA-256, SHA-512, and SHA-3 256.

## Usage

1. **Load Common Passwords:**
   - Common passwords are loaded from a file named `mots.txt`. You can customize this file with a list of common passwords.

2. **Generate Password:**
   - The script generates a random password for testing. The password can either be a common one from the loaded list or a random combination of characters.

3. **Hash Password:**
   - The generated password is hashed using the specified algorithm (MD5, SHA-1, SHA-256, SHA-512, or SHA-3 256).

4. **Compare Hashes:**
   - The script then compares the hashed password with a target hash provided by the user. It iterates through various hashing algorithms until a match is found or the specified number of tests is reached.

## Getting Started

To use this password recovery tool:

1. Clone the repository:

   ```bash
   git clone link
   cd file
