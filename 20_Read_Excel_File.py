import pandas as pd


file = pd.ExcelFile("/Users/tiarawilliams/Desktop/Python/sales.xlsx")

print(file.sheet_names)
['sales', 'customers']

sheet = file.parse('sales')
print(sheet)

type(sheet)

print(sheet.Date)

print(sheet.Amount.sum())

print(sheet.loc[0])

print(sheet.loc[0, "Amount"])

print(sheet.set_index("Customer", inplace = True))

print(sheet.loc["MMC Inc."])

sheet = sheet.reset_index()
sheet["Invoice"]

type(sheet["Invoice"])

print(sheet.loc[sheet["Amount"] > 2000])


print(sheet.loc[sheet["Amount"].idxmax()]["Customer"])
