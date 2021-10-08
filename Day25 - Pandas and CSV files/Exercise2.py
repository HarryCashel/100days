# Using pandas library
import pandas

# A table is a dataframe in pandas
data = pandas.read_csv("weather_data.csv")


# A pandas series is essentially a python list
# Each column of a pandas dataframe is a series
# print(type(data['temp']))
#
#
# # Turn our table into a python dictionary
# data_dict = data.to_dict()
#
# # Convert a Dataframe column into a python list
# temp_list = data["temp"].to_list()
#
#
# # Find average temp in list
# average_temp = sum(temp_list) / len(temp_list)
# print(round(average_temp, 1))
#
# # Using pandas library
#
# print(round(data["temp"].mean(), 1))
#
# # maximum value
#
# print(data["temp"].max())
#
# # Get data in column
# print(data["condition"])
# print(data.condition)

# Get data in row
# print(data[data.day == "Monday"])

# Find the day that had the maximum temperature
# max_temp_day = data[data.temp == data["temp"].max()]
#
# print(max_temp_day)

# Monday temp in F

mon_data = data[data.day == "Monday"]
# mon_temp = mon_data["temp"]
mon_temp = mon_data.temp
mon_in_f = mon_temp * 9/5 + 32
print(mon_in_f)
# mon_in_f = mon_temp * 9/5 + 32
# print(mon_in_f)

# One line way to access the temperature for Monday
mon_data = data[data.day == "Monday"].temp
print(mon_data * 9/5 + 32)