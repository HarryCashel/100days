import pandas as pd

df = pd.read_csv("salaries_by_college_major_updated.csv")
pd.set_option("display.width", 7)
pd.set_option("display.max_columns", 10)

clean_data = df.dropna()

# early_career_top = clean_data['Early Career Pay']
# mid_career_top = clean_data['Mid-Career Pay']

# top 5 early career majors

highest_early_career = clean_data.sort_values('Early Career Pay', ascending=False)
highest_mid_career = clean_data.sort_values('Mid-Career Pay', ascending=False)
print(highest_early_career.head())
print(highest_mid_career.head())
