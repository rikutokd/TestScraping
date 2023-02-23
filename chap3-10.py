import pandas as pd

# CSVファイル読み込み
df = pd.read_csv("test.csv")

# 行と列入れ替え
print("行と列を入れ替える\n", df.T)

# データをリスト化する
print("Pythonのリストデータ化\n", df.values)