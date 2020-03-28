import requests
from lxml import html

pageContent=requests.get('https://krsw.5ch.net/test/read.cgi/gamesm/1582467356')
tree = html.fromstring(pageContent.content)

xpath1 = "/html/body/div[@class='container container_body mascot']/div[@class='thread']/div/div[@class='meta']/text()"
xpath2 = "/html/body/div[@class='container container_body mascot']/div[@class='thread']//div[@class='meta']/span/text()"

# data0=tree.xpath("/html/body/div[@class='container container_body mascot']/div[@class='thread']//div[@class='meta']/span/text()")
data0=tree.xpath(xpath2)

msg = ""
for data in data0:
    if "1001" in data:
        break

    if "ID:" in data:
        msg += str(data) + "\n"
    else:
        msg += str(data) + ", "

f = open("5ch_data.csv", "w")
f.write(msg)
f.close()

print(msg)

