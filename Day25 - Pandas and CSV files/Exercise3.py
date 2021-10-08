import pandas

# Create a dataframe

data_dict = {
    "students": ["Amy", "James", "Angela"],
    "scores": [76, 56, 65]
}

data = pandas.DataFrame(data_dict)

print(data)

# CONVERT TO CSV

data.to_csv("newdata.csv")

