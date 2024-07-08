import pandas

nato_phonetic_alphabet_df = pandas.read_csv("nato_phonetic_alphabet.csv")
nato_phonetic_alphabet = { row.letter:row.code for idx, row in nato_phonetic_alphabet_df.iterrows()}

def generate_phonetic():
    user_input = input("Enter a word: ").upper()
    try:
        nato_conversion = [nato_phonetic_alphabet[letter] for letter in user_input]
    except KeyError:
        print("Sorry, only letters in the alphabet please.")
        generate_phonetic()
    else:
        print(nato_conversion)

generate_phonetic()
