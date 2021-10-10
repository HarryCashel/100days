import pandas

nato = pandas.read_csv("nato_phonetic_alphabet.csv")

# for index, row in nato.iterrows():
#     if row.letter == "A":
#         print(row.code)

nato_dict = {row.letter: row.code for index, row in nato.iterrows()}

print(nato_dict)

word = input("Give me a word: ")

# for letter in word.upper():
#     print(nato_dict[letter])

word_list = [nato_dict[letter] for letter in word.upper()]
print(word_list)