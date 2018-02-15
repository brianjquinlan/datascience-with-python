import pandas as pd

class PandasFunctions:
    def __init__(self, json_data):
        # self.json_data = json_data
        self.df = pd.read_json(data)

    # def create_dataframe(self):
        # self.df = pd.read_csv(self.csv_file)
        # return self.df
        # pass

    def select_column(self, column_name):
        return self.df[column_name]
        
    def select_row(self, row):
        # for labeled data loc[row]
        return self.df.iloc[row] # or [row,:]
    
    def select_values(self, row_slice1, row_slice2, column_slice1, column_slice2):
        return self.df.iloc[slice(row_slice1, row_slice2), 
                slice(column_slice1, column_slice2)]

    def select_value(self, row, column):
        return self.df.iloc[row, column]
    
    def slice_row(self, start, stop):
        return self.df.iloc[start:stop]
    
    
    
