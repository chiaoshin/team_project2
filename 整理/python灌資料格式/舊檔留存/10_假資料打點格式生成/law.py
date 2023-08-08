import pandas as pd

df = pd.read_csv("./全台判決書.csv", encoding="utf-8")
df.fillna('null', inplace=True)

result = "["

for index, row in df.iterrows():
    result += '["ch_name"=>"{0}","business_id"=>"{1}","event"=>"{2}","directions"=>"{3}","url"=>"{4}","type"=>"{5}","store_id"=>"{6}","hotel_id"=>"{7}","shop_id"=>"{8}"]'.format(
        row["店家名"], row["統一編號"], row["事件"], row["說明"], row["連結"], row["類型"], row["店家編號"], row["背包客房編號"], row["用品店編號"]
    )

    if index < df.shape[0] - 1:
        result += ","

result += "]"

print(result)
