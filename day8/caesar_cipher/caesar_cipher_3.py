alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


def caesar(start_text, shift_amount, cipher_direction):
  result_text = ""
  if cipher_direction == "decode":
    shift_amount *= -1

  for char in start_text:
    if char in alphabet:
      position = alphabet.index(char)
      new_position = position + shift_amount
      result_text += alphabet[new_position]
    else:
      result_text += char
  print(f"The encoded text is {result_text}")


caesar(start_text=text, shift_amount=shift, cipher_direction=direction)
