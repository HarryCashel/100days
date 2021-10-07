import csv

# Create list of values from our weather data file
# data = [value.strip() for value in open("weather_data.csv")]
#
# print(data)
#
# for row in data:
#     print(row)

# using the csv library

# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     # for row in data:
#     temp = [int(row[1]) for row in data if row[1] != "temp"]
#     print(temp)


# Using pandas library
import pandas

data = pandas.read_csv("weather_data.csv")

print(data['temp'])

