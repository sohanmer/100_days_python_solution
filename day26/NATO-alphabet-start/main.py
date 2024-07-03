import pandas

nato_phonetic_alphabet_df = pandas.read_csv("nato_phonetic_alphabet.csv")
#TODO 1. Create a dictionary in this format:
nato_phonetic_alphabet = { row.letter:row.code for idx, row in nato_phonetic_alphabet_df.iterrows()}


#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
user_input = input("Enter a word: ").upper()
nato_conversion = [nato_phonetic_alphabet[letter] for letter in user_input ]

print(nato_conversion)
