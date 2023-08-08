import pandas as pd

df = pd.read_csv("./全台背包客房.csv", encoding="utf-8")
df.fillna('null', inplace=True)

result = "["

for index, row in df.iterrows():
    result += '["ch_name"=>"{0}","en_name"=>"{1}","area"=>"{2}","location"=>"{3}","address"=>"{4}","lat"=>"{5}","lng"=>"{6}","url"=>"{7}","work_start_from"=>"{8}","work_end_to"=>"{9}","checkin_start_from"=>"{10}","checkin_end_to"=>"{11}","checkout_start_from"=>"{12}","checkout_end_to"=>"{13}","transform_note"=>"{14}"]'.format(
        row["店家名"], row["店家名(英)"], row["地區"],  row["縣市"], row["地址"], row["緯度"], row["經度"], row["連結"], row["營業時間(起)"], row[
            "營業時間(迄)"], row["入住時間(起)"], row["入住時間(迄)"], row["退房時間(起)"], row["退房時間(迄)"], row["交通建議"],
    )

    if index < df.shape[0] - 1:
        result += ","

result += "]"

print(result)
