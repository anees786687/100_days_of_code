"""
We can use loops to iterate over pandas data frame similar to looping though a dictionary

"""
import pandas as pd

student_dict ={
    'student': ['Angela','James','Lily'],
    'score': [56,76,98]
}

# looping thorugh a dict
# for (key,value) in student_dict.items():
#     print(key)

df = pd.DataFrame(student_dict)
# print(df)

# we can lopp through a df similar to dict
# for (k,v) in df.items():
#     print(k, v) # this is not particularly useful as it just loops though the names of the columns and the data inside each col

# pandas has inbuilt loop, it is a method call iterrows() which allows use to loop thorugh rows of data rather looping thoguh a column
# this way we can tap into a row and get the hold of the value uder a particular col by using the dot notaion
for (index, row) in df.iterrows():
    print(index, row.student)
    if row.student == 'Angela':
        print(row.score)
