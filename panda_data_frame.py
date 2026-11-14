import pandas as pd

cities = {"City": ["Banaras","Amristar","Dharavi"],
          "State":["Up","Punjab","Mumbai"],
          "Population": [25000,40000,460000]}
df=(pd.DataFrame(cities))
print(df.shape)
print(df["Population"].mean())