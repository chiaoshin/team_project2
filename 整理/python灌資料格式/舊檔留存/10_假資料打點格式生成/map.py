import pandas as pd

df = pd.read_csv("./潛水地點.csv", encoding="utf-8")
df.fillna('無', inplace=True)

result = "["

for index, row in df.iterrows():
    result += '["ch_name"=>"{0}","area"=>"{1}","location"=>"{2}","address"=>"{3}","lat"=>"{4}","lng"=>"{5}","description"=>"{6}"]'.format(
        row["地點"], row["地區"], row["縣市"], row["地址"], row["緯度"], row["經度"], row["文字敘述"]
    )

    if index < df.shape[0] - 1:
        result += ","

result += "]"

print(result)
