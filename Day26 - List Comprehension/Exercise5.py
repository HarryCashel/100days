"""Iterate over pandas frame"""

student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]

}

import pandas

# Create pandas data frame
student_dict_frame = pandas.DataFrame(student_dict)

# Loop through keys
# for k, v in student_dict_frame.items():
    # print(k)

# loop through rows of a data frame

for (index, row) in student_dict_frame.iterrows():
    if row.score > 100:
        print(row.student)
