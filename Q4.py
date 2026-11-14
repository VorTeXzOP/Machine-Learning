import pandas as pd

d = pd.read_csv("students_raw.csv")
print(d.info())
print(d.isna().sum())

# we found 