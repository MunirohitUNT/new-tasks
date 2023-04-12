import pandas as pd

df = pd.read_csv("annual-enterprise-survey-2021-financial-year-provisional-csv.csv")
df = df[["Year", "Units"]]
print(df)
