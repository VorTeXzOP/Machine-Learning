import pandas as pd

data = pd.read_csv("students_raw.csv")
print(data.shape)
print(data.head(3))
print(data.tail(2))