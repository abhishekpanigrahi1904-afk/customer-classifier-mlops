import pandas as pd

df = pd.read_excel("data/raw/online_retail_II.xlsx", sheet_name="Year 2010-2011")
print(df.shape)
print(df.head())