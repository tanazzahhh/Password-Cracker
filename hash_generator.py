# Creating a Hashed Password using SHA-256.

import hashlib

# Ask user for the password and hash type
password = input("Enter a password to hash: ")
print("Choose a hash type: md5, sha1, sha256")
hash_type = input("Hash type: ").lower()

# Hash the password based on the selected type
if hash_type == "md5":
    hashed = hashlib.md5(password.encode()).hexdigest()
elif hash_type == "sha1":
    hashed = hashlib.sha1(password.encode()).hexdigest()
elif hash_type == "sha256":
    hashed = hashlib.sha256(password.encode()).hexdigest()
else:
    print("Invalid hash type. Please choose md5, sha1, or sha256.")
    exit()

print(f"{hash_type.upper()} hash of the password: {hashed}")

# Note: Now save the hash printed here and paste it in "cracker.py" as the target hash.