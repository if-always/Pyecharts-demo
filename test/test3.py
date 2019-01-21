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

# a=file['areas'].value_counts()
# print(a)
def cut(value):
	if '中国' in value:
		return '中国'
	else:
		value = value.split(',')[0]
		return value
#file['areas'] = file['areas'].apply(cut)
#print(file['areas'].value_counts().index.tolist())
#print(file['areas'].value_counts().tolist())

print(file.columns.tolist())

def Bar():
	from pyecharts import Bar,Style

	def cut(value):
		if '中国' in value:
			return '中国'
		else:
			value = value.split(',')[0]
			return value
	file['areas'] = file['areas'].apply(cut)
	attr = file['areas'].value_counts().index.tolist()
	valu = file['areas'].value_counts().tolist()

	style = Style(
		title_pos = 'center',
		width = 900,
		height = 500,
		background_color = 'white')
	bar_style = style.add(
		legend_pos = 'bottom',
		label_color = ['yellow'],
		label_text_color ='blue',
		is_label_show=None,#显示图例  数据
		mark_point=['max'],
		mark_line=['average'])
	bar = Bar("地区分布:","",**style.init_style)#标题和副标题
	bar.add("",attr,valu,**bar_style)
	#is_convert = True 换x y轴
	bar.render('bar.html')
	#print(file['areas'].value_counts().sum())
def Pie():
	from pyecharts import Pie,Style

	def cut(value):
		if '中国' in value:
			return '中国'
		else:
			value = value.split(',')[0]
			return value
	file['areas'] = file['areas'].apply(cut)
	attr = file['areas'].value_counts().index.tolist()
	valu = file['areas'].value_counts().tolist()

	style = Style(
		title_pos = 'center',
		title_top = 'bottom',
		width = 900,
		height = 500,
		background_color = 'white')
	pie_style = style.add(
		legend_pos = 'center',
		#radius=[40, 75],
		label_color = [],
		label_text_color ='',
		is_label_show=True,#显示图例  数据
		)

	pie = Pie("areas:","",**style.init_style)
	pie.add("",attr,valu,**pie_style)
	pie.render('pie.html')
Pie()