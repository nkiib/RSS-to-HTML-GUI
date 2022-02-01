def time_split(date): # 時間の修正処理
    timex = date.split("T")
    timex2 = timex[1].split("+")
    datex = timex[0].split("-")
    publish = datex[0] + "/" + datex[1] + "/" + datex[2] + " " + timex2[0]
    return publish