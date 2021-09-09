deciphered = input()
encrypted_message = ""

for ch in deciphered:
    encrypted_message += chr(ord(ch) + 3)

print(encrypted_message)

