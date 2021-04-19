import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
from docx.shared import Inches
from docx import Document
import glob
from support import align_data

def FlowRate_df(river_name, excel_list):

    data = pd.DataFrame()

    for el in excel_list:

        ss = pd.Series() # 空の配列を用意

        yy = el[-9:-5] # 計測年の取得

        for i in range(12): # 1~12月の繰り返し計算

            month = i + 1

            df = pd.read_excel(el, sheet_name=str(month) + '月')

            ss = align_data(df, ss)

        data[str(yy)] = ss
    
    return data

def make_document(river_name):

    docx_file = './Python_workshop_02/word/流量データ_' + river_name + '.docx'

    document = Document()

    document.add_picture(
    './Python_workshop_02/fig/' + river_name + '_graph.png',
    width=Inches(3.6))

    document.save(docx_file)

def main():

    river_list = ['Asahibashi', 'Fushiko', 'Inou', 'Ishikarioohashi', 'Nagayama']

    for river_name in river_list:

        excel_list = glob.glob('./Python_workshop_02/Ishikari/*' + river_name + '_*.xlsx')

        river_df = FlowRate_df(river_name, excel_list)

        river_df.plot()
        plt.savefig('./Python_workshop_02/fig/' + river_name + '_graph.png')

        make_document(river_name)

if __name__ == '__main__':
    main()
