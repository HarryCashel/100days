"""Program to encode and decode strings"""
from alphabet import alphabet

# function to decode

# function to encode

# function to take user input


def user_init():
    """Initialise program with user input"""
    choice = input("Type 'decode' to decrypt or 'encode' to encrypt\n").lower()
    return choice


def user_text():
    """Takes user string to encode/decode"""
    text = input("Type your message: ").lower()
    return text


def user_shift():
    """Takes the shift number from the user"""
    shift = int(input("Enter the shift number: "))
    return shift


def encode():
    """Encrypts a string"""
    # Split string into individual words
    string = user_text().split()
    shift = user_shift()
    encoded_str = ""
    # Loop through each letter in word
    # for i in list(string):
    #     # Checks the position of current letter in alphabet
    #     for pos in range(len(alphabet)):
    #         # Shifts letter by the user declared shift amount
    #         # Using modulo to prevent index error
    #         if alphabet[pos] == i:
    #             encoded_word += alphabet[(pos + shift) % 26]

    # This is much cleaner and more efficient code
    # Loops through each word in string
    for word in string:
        encoded_word = ""
        # Loops through each letter in word
        for letter in word:
            # Check if letter in alphabet - If not simply add to encoded word
            if letter in alphabet:
                # Finds the index of the letter in our list alphabet - assign to variable pos
                pos = alphabet.index(letter)
                # Assigns new position to variable new_pos - Using modulo to avoid an IndexError
                new_pos = (pos + shift) % 26
                # Add new letter to our encoded word
                encoded_word += alphabet[new_pos]
            else:
                encoded_word += letter
        # Adds encoded word to encoded string
        encoded_str += encoded_word + " "
    return encoded_str.strip()


def decode():
    """Decrypts a string"""
    encrypted_string = user_text().split()
    shift = user_shift()
    decrypted_str = ""

    # Loops through each word in the encoded message
    for word in encrypted_string:
        decoded_word = ""
        # Loops through each letter in word
        for letter in word:

            # Check if letter in alphabet - If not add character to decoded word in position
            if letter in alphabet:
                # Finds index of the letter in the alphabet list - assign to variable pos
                pos = alphabet.index(letter)
                # Assigns new position to variable new_pos - Using modulo to avoid possible IndexError
                new_pos = (pos - shift) % 26

                # Add new letter to decoded_word
                decoded_word += alphabet[new_pos]
            else:
                decoded_word += letter
        # As each word is completed, add to decrypted string
        decrypted_str += decoded_word + " "
    return decrypted_str.strip()


def run_again():
    ask = input("Would you like to run the program again?\n")
    if 'y'.lower() in ask:
        return True
    return False


def run():
    run_program = True
    while run_program:
        prompt = user_init()
        if prompt == 'encode':
            print(encode())
            if not run_again():
                run_program = False
        elif prompt == 'decode':
            print(decode())
            if not run_again():
                run_program = False


run()
