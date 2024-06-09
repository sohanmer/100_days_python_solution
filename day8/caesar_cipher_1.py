alphabet = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
    'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
]

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


#TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.
def encrypt(text, shift):
    cipher_text = ''
    for letter in text:
        if shift + alphabet.index(letter) > 25:
            idx = shift + alphabet.index(letter) - 26
        else:
            idx = alphabet.index(letter) + shift
        cipher_text += alphabet[idx]
    print(f"The encoded text is {cipher_text}")
    
encrypt(text, shift)
