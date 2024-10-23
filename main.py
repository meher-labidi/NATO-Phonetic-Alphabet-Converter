
import pandas
data = pandas.read_csv("nato_phonetic_alphabet.csv")


Nato_phonetic = {row.letter: row.code for (index, row) in data.iterrows()}
print(Nato_phonetic)


def generate_phonetic():
    word = input("what is your word: ").upper()
    try:
        output_list = [Nato_phonetic[letter] for letter in word]
    except KeyError:
        print("Sorry, only letters in alphabet please.")
        generate_phonetic()
    else:
        print(output_list)

generate_phonetic()