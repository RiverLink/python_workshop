import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
from support import align_data

# 読み込みデータの指定
excel_file = './Python_workshop_02/code_sample/Asahibashi_2015.xlsx'
river_name = 'asahibashi'

data = pd.DataFrame() # 空のデータフレームを用意
ss = pd.Series() # 空の配列を用意

df = pd.read_excel(excel_file, sheet_name='1月')

ss = align_data(df, ss) # 1列の配列に並べる
data[river_name] = ss # 配列をデータフレームに入れる

print(data)

data.plot()
plt.savefig('./Python_workshop_02/code_sample/sample_graph.png')
