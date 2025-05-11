# cipher.py

# --- Chiffrement de César ---
def caesar(text, shift):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    encrypted_text = ''

    for char in text.lower():
        if char == ' ':
            encrypted_text += char
        else:
            index = alphabet.find(char)
            if index != -1:
                new_index = (index + shift) % len(alphabet)
                encrypted_text += alphabet[new_index]
            else:
                encrypted_text += char  # Garde les caractères non alphabétiques
    return encrypted_text


# --- Chiffrement de Vigenère ---
def vigenere(message, key, direction=1):
    key_index = 0
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    final_message = ''

    for char in message.lower():
        if not char.isalpha():
            final_message += char
        else:
            key_char = key[key_index % len(key)]
            key_index += 1
            offset = alphabet.index(key_char)
            index = alphabet.find(char)
            new_index = (index + offset * direction) % len(alphabet)
            final_message += alphabet[new_index]
    return final_message


def encrypt_vigenere(message, key):
    return vigenere(message, key, direction=1)

def decrypt_vigenere(message, key):
    return vigenere(message, key, direction=-1)


# --- Test des deux algorithmes ---
def main():
    # Chiffrement de César
    text1 = "Hello Zaira"
    shift = 3
    cesar_result = caesar(text1, shift)
    print("=== Chiffrement de César ===")
    print("Texte original :", text1)
    print("Décalage :", shift)
    print("Texte chiffré :", cesar_result)

    # Chiffrement de Vigenère
    print("\n=== Chiffrement de Vigenère ===")
    encrypted_text = "mrttaqrhknsw ih puggrur"
    key = "python"
    print("Texte chiffré :", encrypted_text)
    print("Clé :", key)
    decrypted_text = decrypt_vigenere(encrypted_text, key)
    print("Texte déchiffré :", decrypted_text)

if __name__ == "__main__":
    main()
