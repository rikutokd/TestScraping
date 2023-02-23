import pandas as pd

# CSVファイル読み込み
df = pd.read_csv("test.csv")

# ソート（並べ替え）をして表示
kokugo = df.sort_values("国語", ascending=False)

# Excelファイル出力
kokugo.to_excel("csv_to_excel2.xlsx", index=False, sheet_name="国語でソート")