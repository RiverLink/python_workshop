import sys
import read_data
import make_graph
import make_doc

# #--------------------------------------------------
# # read data
# #--------------------------------------------------
# def read_data():

#     print('read_data')

#     return 0

# #--------------------------------------------------
# # make graph
# #--------------------------------------------------
# def make_graph():

#     print('make_graph')

#     return 0

# #--------------------------------------------------
# # make doc
# #--------------------------------------------------
# def make_doc():

#     print('make_doc')

#     return 0

#--------------------------------------------------
# main fuction
#--------------------------------------------------
def main(f_conf):
    
    # 処理フローを記述

    # dataを読み込む
    if read_data.csv() != 0:
        print('error at read_data()')

    # グラフを作成する
    if make_graph.plot_xy() != 0:
        print('error at make_graph()')
    
    # wordに貼る
    if make_doc.paste_img() != 0:
        print('error at make_doc()')

    return 'ok'

if __name__ == '__main__':
    
    # 引数
    if len(sys.argv) == 1:
        print('ファイルを指定してください。')

    elif len(sys.argv) == 2:
        print('start : ' + sys.argv[0])
        print(main(sys.argv[1]))