# import pandas lib as pd
import pandas as pd
import xlrd
import openpyxl


dataframe1 = pd.read_excel('Financial Sample.xlsx')
df = pd.read_excel("Financial Sample.xlsx", sheet_name="Sheet1")
df = df[["Segment", "Profit"]]
print(df)
