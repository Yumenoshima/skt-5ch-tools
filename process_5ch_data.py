import csv
import pprint
import datetime

with open('5ch_data.csv') as f:
    reader = csv.reader(f)
    for row in reader:
        lists = [row for row in reader]

msg = ""
msg += "[\n"

for l in lists:
    msg += "["
    msg += "\"\","
    # id1
    msg += "\"" + str(l[0]) + "\","
    # id2
    msg += "\"" + str(l[0]) + "\","
    # date
    date_str = str(l[3]).strip()
    date_dt = datetime.datetime.strptime(date_str[:10], '%Y/%m/%d')
    msg += "\"" + datetime.date.strftime(date_dt, '%-m/%-d') + "\","
    # 年代
    msg += "\"" + "" + "\","
    # 性別
    msg += "\"" + "" + "\","
    # location
    loc_str = str(l[1]).strip()
    loc_str = loc_str.replace("(", "").replace(")", "")
    msg += "\"" + loc_str + "\","
    # 備考1
    msg += "\"" + "" + "\","
    # 備考2
    msg += "\"" + "" + "\""
    msg += "],\n"

msg += "]"

f = open("5ch_data.json", "w")
f.write(msg)
f.close()

print(msg)
