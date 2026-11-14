import pandas as pd
data = pd.Series([340,285,410,190],index=["Mon", "Tue", "Wed", "Thu"])
print(data)
print("WEDNESDAY: ",data["Wed"])
print("Data Mean: ",data.mean())
print("Data Max: ",data.max())