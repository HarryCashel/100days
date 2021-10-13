import pandas

nato = pandas.read_csv("nato_phonetic_alphabet.csv")

# for index, row in nato.iterrows():
#     if row.letter == "A":
#         print(row.code)

nato_dict = {row.letter: row.code for index, row in nato.iterrows()}


# def run_again():
#     again = input("Would you like to run again? (y/n)")
#     if again == "y":
#         return True
#     return False


def word_to_nato():
    word = input("Give me a word: ")

    try:
        word_list = [nato_dict[letter] for letter in word.upper()]
    except KeyError:
        print("Sorry, only letters in the alphabet are accepted.")
        word_to_nato()
    else:
        print(word_list)
        again = input("Would you like to run again? (y/n)")

        if again == "y":
            word_to_nato()
        else:
            print("Bye")



word_to_nato()
