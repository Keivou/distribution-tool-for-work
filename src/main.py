import sys
import argparse

import pandas as pd

from PySide6.QtWidgets import QApplication

from main_window import MainWindow
from main_widget import Widget

def read_excel(excel_file):
    # Create Dataframe
    df = pd.read_excel(excel_file)

    # Drop duplicates
    df.drop_duplicates(inplace=True)

    # Convert datetime objects to str
    try:
        df["FECHA"] = df["FECHA"].dt.strftime('%d/%m/%Y')
        return df
    except AttributeError:
        return df
    
    


def transform_df_to_dict(df):
    """
    First, create a dates dictionary with unique dates and where the keys are tuples of the rest of the data inside a list -> {date: [(data1, data2, data3), (...), (...)]}.

    Then, create a second dictionary, where the keys are unique well identifiers, and the values are the dates inside the dates dict that correspond to each well id
    """
    date_dict = {}
    for row in df.iterrows():
        date = row[1].iloc[1]
        cape_id = row[1].iloc[2]
        top_num = row[1].iloc[3]
        base_num = row[1].iloc[4]
        data_tuple = (cape_id, top_num, base_num)
        try:
            date_dict[date].append(data_tuple)
        except KeyError:
            date_dict[date] = [data_tuple]
        
    wells_dict = {}
    for row in df.iterrows():
        well_id = row[1].iloc[0]
        date = row[1].iloc[1]
        try:
            wells_dict[well_id][date] = date_dict[date]
        except KeyError:
            wells_dict[well_id] = {date: date_dict[date]}

    return wells_dict


if __name__ == "__main__":
    # # Read excel file and get data
    # options = argparse.ArgumentParser()
    # options.add_argument("-f", "--file", type=str, required=True)
    # args = options.parse_args()
    # df = read_excel(args.file)
    # data_dict = transform_df_to_dict(df)

    # # print(data_dict)
    # new_df = pd.DataFrame(data_dict)
    # new_df.to_excel("./data/parsed_test2.xlsx")


    # QtApp
    app = QApplication(sys.argv)

    widget = Widget()

    window = MainWindow(widget)
    window.resize(800, 600)
    window.show()

    sys.exit(app.exec())