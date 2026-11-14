import pandas as pd

CR = {"Player":['Rohit','Virat','Gill','Pant'],
      "Team":['MI','RCB','GT','DC'],
      "Runs":[4200,6100,2800,3100],
      "Average":[31.5,48.2,44.9,35.6]
      }
data = pd.DataFrame(CR)
print(data)
print(data.shape)
print(data.dtypes)