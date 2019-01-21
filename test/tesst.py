import numpy as np
import pandas as pd
from collections import Counter

#from pyecharts.engine import create_default_environment
#png = create_default_environment("png")

df = pd.read_excel('../GitHub/maoyan/datas.xlsx',index_col='index')
file = df.copy()

file['longt'] = file['longt'].str.strip('分钟').astype('int64')   #.str  因为类型是seris  所以要转为str
file['years'] = file['times'].str.split('-').str[0]
file['month'] = file['times'].str.split('-').str[1]
file['month'] = file['month'].fillna("07")       #设置缺省值


def cut(types):
	temps = []
	temp = types.split(',')
	temps.extend(temp)
	return temps
type_temp = []
type_list = file['style'].apply(cut)
for i in type_list.values:
	type_temp.extend(i)



dicts = Counter(type_temp)
attr = []
valu = []
for a,v in dicts.most_common(10):
	attr.append(a)
	valu.append(v)

perc = [int(100*int(v)/int(sum(valu)))/100 for a,v in zip(attr,valu)]

types = pd.DataFrame({'type':attr,'nums':valu,'perc':perc})
types = types.set_index('type')

#print(types.iloc[0].name)
from pyecharts import Pie,Style

pie = Pie("各类电影所占比重","热门类型",title_pos = 'center')
style = Style(width=1500,height=1000)
pie_style = style.add(label_pos='center',is_label_show=True,label_text_color=None)


for i in range(0,5):
	pie.add("",[types.iloc[i].name,"其它"],[types.iloc[i]['perc'],1-types.iloc[i]['perc']],center=[16.2*(i+1),30],radius=[18,23],legend_top="bottom",**pie_style)
#print(types.loc['剧情']['perc'])
#pie.add("",['剧情',''],[types.loc['剧情']['perc'],1-types.loc['剧情']['perc']],center=[10,30],radius=[18,24],**pie_style)
# pie.add("",['剧情',""],['47.5','52.5'],center=[10,30],radius=[18,24],**pie_style)
# pie.add("",['悬疑'],['32.4'],center=[30,50])
for i in range(5,10):
	pie.add("",[types.iloc[i].name,"其它"],[types.iloc[i]['perc'],1-types.iloc[i]['perc']],center=[16.2*(i-4),70],radius=[18,23],legend_top="bottom",**pie_style)


pie.render('qaaq.html')

