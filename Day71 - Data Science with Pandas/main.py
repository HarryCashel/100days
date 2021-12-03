import pandas as pd
import pprint

df = pd.read_csv('salaries_by_college_major.csv')

# pprint.pprint(df.head())

# # check the format of the csv and print column names
# print(df.shape)
# print(df.columns)
#
# # check for rows that do not contain numbers and print the last 5 entries
# print(df.isna())
# print(df.tail())
#
# # clean our data of rows that have blank values
clean_data = df.dropna()
#
# print(clean_data.tail())
#
# # access a particular column from our data frame
#
# sms = clean_data['Starting Median Salary']
# print(sms)
#
# # find the max value in that column
# print(sms.max())
#
# # get row number/index with the largest value in specified column
# print(sms.idxmax())
#
# # get the value of a particular cell
# print(clean_data['Undergraduate Major'][sms.idxmax()])
# print(clean_data['Undergraduate Major'][43])
#
# # get an entire row
# print(clean_data.loc[43])

# challenge 1. What college major has the highest mid-career salary? How much do graduates with this major earn? (
# Mid-career is defined as having 10+ years of experience).

print(df.columns)
major = clean_data["Undergraduate Major"]
mid_career_top = clean_data["Mid-Career Median Salary"]
id_of_top_earner = (mid_career_top.idxmax())
print(major[id_of_top_earner])

# challenge 2. Which college major has the lowest starting salary and how much do graduates earn after university?

starting_med_salary = clean_data["Starting Median Salary"]
lowest_id = starting_med_salary.idxmin()
print(starting_med_salary[lowest_id], major[lowest_id])

# challenge 3. Which college major has the lowest mid-career salary and how much can people expect to earn with this
# degree?
lowest_mid_career_salary_id = clean_data.loc[clean_data["Mid-Career Median Salary"].idxmin()]
print(lowest_mid_career_salary_id)

# Create a new column into the data frame

spread_col = clean_data["Mid-Career 90th Percentile Salary"] - clean_data["Mid-Career 10th Percentile Salary"]
clean_data.insert(1, "Spread", spread_col)
print(clean_data.head())

# sort the data frame by a column

low_risk = clean_data.sort_values("Spread")
print(low_risk[["Undergraduate Major", "Spread"]].head())

# challenge 1. Using the .sort_values() method, can you find the degrees with the highest potential? Find the top 5
# degrees with the highest values in the 90th percentile

highest_potential = clean_data.sort_values("Mid-Career 90th Percentile Salary", ascending=False)
print("\n")
hp_top_5 = (highest_potential[["Undergraduate Major", "Mid-Career 90th Percentile Salary"]].head())
print(hp_top_5)
# for major in hp_top_5:
#     print(major)

# challenge 2. Find the degrees with the greatest spread in salaries. Which majors have the largest difference
# between high and low earners after graduation.

largest_spread = clean_data.sort_values("Spread", ascending=False)
ls_top_5 = largest_spread[["Undergraduate Major", "Spread"]].head()
print(ls_top_5)

# count function - count how many occurrences...

print(clean_data.groupby("Group").count())

# find the average salary of each group

print(clean_data.groupby("Group").mean())





