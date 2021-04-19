import pandas as pd

excel_file = './Python_workshop_02/code_sample/Asahibashi_2015.xlsx'

df = pd.read_excel(excel_file, sheet_name='1月')

print(df)