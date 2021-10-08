import pandas

squirrel_data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")


# Using Python dictionary comprehension
colours = list(squirrel_data["Primary Fur Color"])

colours_dict = {
    "Gray": 0,
    "Cinnamon": 0,
    "Black": 0,
}

for colour in colours:
    # try:
    if colour in colours_dict.keys():
        colours_dict[colour] += 1
    # except KeyError:
    #     pass
data_dict = {
    "Fur Colour": [k for k in colours_dict.keys()],
    "Count": [v for v in colours_dict.values()]
}
# print(colours_dict)
print(data_dict)


# Using len function and pandas
colours = squirrel_data["Primary Fur Color"]
grey_squirrels = len(colours[colours == "Gray"])
red_squirrel = len(colours[colours == "Cinnamon"])
black_squirrel = len(colours[colours == "Black"])

data_dict = {
    "Fur Colour": ["Gray", "Cinnamon", "Black"],
    "Count": [grey_squirrels, red_squirrel, black_squirrel]
}

print(data_dict)

data = pandas.DataFrame(data_dict)

data.to_csv("furcount.csv")