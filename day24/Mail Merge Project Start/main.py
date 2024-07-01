with open("Input/Names/invited_names.txt") as invites:
    invites = invites.read().split("\n")

with open("Input/Letters/starting_letter.txt") as letter_body:
    letter_body = letter_body.read()

for name in invites:
    letter = letter_body.replace("[name]", name)
    with open(f"Output/ReadyToSend/letter_to_{name}.txt", "w") as letter_to_person:
        letter_to_person.write(letter)
