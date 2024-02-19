from sklearn.model_selection import train_test_split
import pandas as pd

class DataSplitter:
    def __init__(self, dataframe, target_column, test_size=0.4, random_state=42):
        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(
            dataframe.drop(target_column, axis=1),
            dataframe[target_column],
            test_size=test_size,
            random_state=random_state
        )

    def split_dataframe_sequential(self, train_percentage=0.8):
        total_rows=self.data.shape[0]
        train_rows=int(total_rows*train_percentage)
        train_df=self.data.iloc[:train_rows,:]
        oos_df=self.data.iloc[train_rows:, :]
        return train_df, oos_df
    
    def split_by_last_date(self):
        last_date=self.data['date'].iloc[-1]
        prediction_set=self.x_data[self.x_data['date'>last_date]]
        return prediction_set