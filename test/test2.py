import requests
from lxml import etree
import pandas as pd



headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'
}
res = requests.get("http://lol.duowan.com/hero/",headers=headers).text

infos = etree.HTML(res).xpath('//div[@class="mod-pic-bd"]/ul/li')
items = []
for info in infos:
	item = {}
	item['url'] = info.xpath('.//a[@target="_blank"]/@href')[0]
	item['name'] = info.xpath('.//div[@class="champion_name"]/text()')[0]
	item['picture'] = info.xpath('.//a[@target="_blank"]/img/@src')[0]
	items.append(item)

urls = [info['url'] for info in items]
names = [info['name'] for info in items]
pictures = [info['picture'] for info in items]


df = pd.DataFrame({'name':names,'url':urls,'picture':pictures})
df = df.set_index('name')
#df.to_excel('../GitHub/Data-Set/hereos/origin-datas.xlsx')

for picture,name in zip(pictures,names):

    pic = requests.get(picture,headers=headers)
    f= open('..//GitHub/Data-Set/hereos/pictures/'+str(name)+".png", 'wb')#以二进制模式打开文件夹
    f.write(pic.content)
    f.close()



