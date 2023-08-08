import pandas as pd

df = pd.read_csv("./全台潛店.csv", encoding="utf-8")

df.fillna('null', inplace=True)

result = "["

for index, row in df.iterrows():
    result += '["ch_name"=>"{0}","en_name"=>"{1}","area"=>"{2}","location"=>"{3}","address"=>"{4}","lat"=>"{5}","lng"=>"{6}","work_start_from"=>"{7}","work_end_to"=>"{8}","checkin_start_from"=>"{9}","checkin_end_to"=>"{10}","checkout_start_from"=>"{11}","checkout_end_to"=>"{12}","transform_note"=>"{13}","landscape"=>"{14}","url"=>"{15}"]'.format(
        row["店家名"], row["店家名(英)"], row["地區"],  row["縣市"], row["地址"], row["緯度"], row["經度"], row["營業時間(起)"], row["營業時間(迄)"], row["入住時間(起)"], row["入住時間(迄)"], row["退房時間(起)"], row["退房時間(迄)"], row["交通建議"], row["周遭潛點"], row["連結"]
    )

    if index < df.shape[0] - 1:
        result += ","

result += "]"

# result.replace('"null"', 'null')

# "null"替代null
# "url"的null改成"無"

print(result)
