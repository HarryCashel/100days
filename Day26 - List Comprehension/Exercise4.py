"""Dictionary Comprehension"""

# Create a dictionary from the sentence where the key is the word and the value is the number of letters
sentence = "What is the Airspeed Velocity of an Unladen Swallow?"

# list_words = sentence.replace("?", "").split()
# for i in list_words:
#     print(len(i))

letter_count = {word: len(word) for word in sentence.replace("?", "").split()}
print(letter_count)

weather_c = {
    "Monday": 12,
    "Tuesday": 14,
    "Wednesday": 15,
    "Thursday": 14,
    "Friday": 18,
    "Saturday": 21,
    "Sunday": 22
}


def conv_f(celsius):
    return celsius * 9 / 5 + 32


weather_f = {day: conv_f(temp) for day, temp in weather_c.items()}

print(weather_f)
