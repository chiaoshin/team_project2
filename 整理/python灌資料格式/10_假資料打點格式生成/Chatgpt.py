import pandas as pd

df = pd.read_csv("./全台chatgpt.csv", encoding="utf-8")
df.fillna('無', inplace=True)

result = "["

for index, row in df.iterrows():
    result += '["keyword"=>"{0}","respond"=>"{1}"]'.format(
        row["關鍵字"], row["回應"]
    )

    if index < df.shape[0] - 1:
        result += ","

result += "]"

print(result)
