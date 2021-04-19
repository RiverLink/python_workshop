import pandas as pd

def align_data(dataframe, ser):

    for row in range(len(dataframe)):
        date = dataframe.iloc[row, 0]
        date = date[5:]
        dataframe.iloc[row, 0] = date

    dataframe = dataframe.set_index('Unnamed: 0')
    ser = pd.concat([ser, dataframe.stack()])

    return ser
