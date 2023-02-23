import pandas as pd

# Excelファイル読み込み
df = pd.read_excel("csv_to_excel3.xlsx")
print(df)
df = pd.read_excel("csv_to_excel3.xlsx", sheet_name="国語のデータ")
print(df)