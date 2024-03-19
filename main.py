import pandas


nato_data_frame = pandas.read_csv("nato_phonetic_alphabet.csv")

nato_dict = {row.letter: row.code for (index, row) in nato_data_frame.iterrows()}

user_input = input("Enter a word: ")

result = [nato_dict[letter.upper()] for letter in user_input]

print(result)

