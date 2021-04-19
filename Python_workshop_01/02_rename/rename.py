import glob
import os

data_folder = './Python_workshop_01/02_rename/rename_folder'
flist = glob.glob(data_folder + '/北海道_石狩川_*.xlsx')

for fl in flist:
    new_file = fl.replace('北海道_石狩川', '北海道_石狩川水系_石狩川')
    os.rename(fl, new_file)
