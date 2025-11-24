alphabet = 'abcdefghijklmnopqrstuvwxyz'
shift = 5
shifted_alphabet = alphabet[shift:] + alphabet[:shift]
translation_table = str.maketrans(alphabet, shifted_alphabet)
print(translation_table)
    if not encrypt:
        shift = - shift

    shifted_alphabet = alphabet[shift:] + alphabet[:shift]
    translation_table = str.maketrans(alphabet + alphabet.upper(), shifted_alphabet + shifted_alphabet.upper())
    encrypted_text = text.translate(translation_table)
    return encrypted_text
def encrypt(text, shift):
    return caesar(text, shift)  
def decrypt(text, shift):
    return caesar(text, shift, encrypt=False)
def decrypt(text, shift):
    return caesar(text, shift, encrypt=False)
encrypted_text = 'Pbhentr vf sbhaq va hayvxryl cynprf.'
print(encrypted_text)
decrypted_text = decrypt(encrypted_text, 13)
print(decrypted_text)
def decrypt(text, shift):
    return caesar(text, shift, encrypt=False)
encrypted_text = 'Pbhentr vf sbhaq va hayvxryl cynprf.'
print(encrypted_text)
decrypted_text = decrypt(encrypted_text, 13)
print(decrypted_text)
def decrypt(text, shift):
    return caesar(text, shift, encrypt=False)
encrypted_text = 'Pbhentr vf sbhaq va hayvxryl cynprf.'

print(encrypted_text)
decrypted_text = decrypt(encrypted_text, 13)
print(decrypted_text)

def decrypt(text, shift):
    return caesar(text, shift, encrypt=False)
encrypted_text = 'Pbhentr vf sbhaq va hayvxryl cynprf.'
print(encrypted_text)
decrypted_text = decrypt(encrypted_text, 13)
print(decrypted_text)
def decrypt(text, shift):
    return caesar(text, shift, encrypt=False)