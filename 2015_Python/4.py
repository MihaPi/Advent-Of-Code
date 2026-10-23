import hashlib

print("Enter secret key:")
secret_key = input()
i = 0

while True:
    secret_key_plus = secret_key + str(i)
    hash = hashlib.md5(secret_key_plus.encode()).hexdigest()

    if (hash.startswith("00000")):
        break

    i += 1

print("Answer:" + str(i))
