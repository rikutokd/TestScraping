import pandas as pd

# CSVファイル読み込み
df = pd.read_csv("test.csv")

# ソート（並べ替え）をして表示
kokugo = df.sort_values("国語", ascending=False)

kokugo.to_csv("export2.csv", index=False, header=False)