import hashlib
import time

# The SHA-256 hash you're trying to crack (copied from hash_generator.py)
target_hash = "b5692500175fad6bb2b306aa20ff58423c79b130ef310fb3caa924e0f28bc61d"

# Path to the wordlist file (same folder)
wordlist_path = "wordlist.txt"

start = time.time()

try:
    with open(wordlist_path, "r", encoding="utf-8") as file:
        for word in file:
            word = word.strip()
            hashed_word = hashlib.sha256(word.encode()).hexdigest()
            if hashed_word == target_hash:
                print(f"[+] Password found: {word}")
                break
        else:
            print("[-] Password not found in wordlist.")
except FileNotFoundError:
    print("[-] Wordlist file not found. Please make sure 'wordlist.txt' is in the project folder.")

end = time.time()
print(f"Time taken: {end - start:.2f} seconds")
