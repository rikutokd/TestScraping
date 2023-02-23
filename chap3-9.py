import pandas as pd

# CSVファイル読み込み
df = pd.read_csv("test.csv")

# ソート（並べ替え）をして表示
kokugo = df.sort_values("国語", ascending=False)
print("国語の点数 降順\n", kokugo)