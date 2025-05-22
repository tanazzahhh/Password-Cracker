# Password Cracker

This project demonstrates basic password security concepts by using Python to hash a password and attempt to crack it using a dictionary-based attack. It is intended for learning and ethical research purposes only. 

---

## Project Features

- Hash a user-provided password using "MD5", "SHA-1", or "SHA-256"
- Crack a hashed password using a dictionary (wordlist)
- Measure time taken to crack passwords
- Learn how password strength and hashing algorithms impact security

---

## Learning Objectives

- Understand how different hashing algorithms work
- Use the 'hashlib' module in Python
- Explore the importance of strong passwords
- Experience how simple dictionary attacks operate

---

## Files Included

This project includes three main files:

- 'hash_generator.py': This script allows the user to enter a password and choose a hash algorithm. It then generates and displays the corresponding hash.
- 'password_cracker.py': This script attempts to crack a target hash by comparing it against hashes of passwords from a wordlist.
- 'wordlist.txt': A plain text file containing a list of common passwords used in the cracking attempt.

You can customize or replace the wordlist file to test different cracking scenarios.

---

## How to Use

1. Clone or Download the Project
If you plan to use version control:

git clone https://github.com/tanazzahhh/Password-Cracker

cd Password-Cracker

Or download the ZIP from GitHub and extract it locally.

### 2. Run the Hash Generator

python hash_generator.py

- Enter a password
- Choose a hash algorithm ('md5', 'sha1', or 'sha256')
- Copy the output hash

### 3. Crack the Hash
- Open 'cracker.py'
- Paste the copied hash into the 'target_hash' variable
- Run the script: python cracker.py
- It will search for the password in the `wordlist.txt` file

---

## Requirements

- Python 3.x
- Basic terminal/command-line interface
- A wordlist file (e.g., wordlist.txt', that is included or custom).

---

## Disclaimer

This project is intended strictly for educational purposes.  
Do not use it to target or compromise real-world systems without permission. Always act responsibly and ethically.

---

## Future Improvements

- Add GUI using tkinter or web framework
- Include more hash functions (e.g., bcrypt, PBKDF2)
- Implement hash cracking statistics (e.g., attempts per second)

---

## Author

**Tanazzah Shaikh**  
Cybersecurity Student & Enthusiast

---


