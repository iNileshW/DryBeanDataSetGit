import numpy as np
import pandas as pd
from sklearn.impute import KNNImputer
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder
from analytics.datasplitter import DataSplitter
from analytics.categorical_to_numerical import CategoricalColumnEncoder

# Reading data
#train = pd.read_csv('data/train.csv')
#test = pd.read_csv('data/test.csv')

#data splitter
#remove y column
df=pd.read_csv(r"C:\Users\Monicca2502\Documents\Nilesh\AI\Pandas\Projects\DryBeanDataSetProject\data\Dry_Bean_Dataset_csv.csv")

#convert categorical to int
encoder=CategoricalColumnEncoder(df)
df=encoder.fit_transform()

X = df.drop('Class', axis=1)  # Features
y = df['Class'] 
#split data
splitter = DataSplitter(dataframe=df, target_column='Class', test_size=0.2, random_state=42)
X_train = splitter.X_train
X_val = splitter.X_test
y_train = splitter.y_train
y_val = splitter.y_test
test = X_val

imputer = KNNImputer()

# Separate numeric and non-numeric columns
numeric_cols = X_train.select_dtypes(include=['int64', 'float64']).columns
non_numeric_cols = X_train.select_dtypes(exclude=['int64', 'float64']).columns

# Impute missing values for numeric columns using KNNImputer
imputer = KNNImputer()
X_train[numeric_cols] = imputer.fit_transform(X_train[numeric_cols])
X_val[numeric_cols] = imputer.transform(X_val[numeric_cols])
test[numeric_cols] = imputer.transform(test[numeric_cols])

# Impute missing values for non-numeric columns with the mode
for column in non_numeric_cols:
    X_train[column].fillna(X_train[column].mode()[0], inplace=True)
    X_val[column].fillna(X_val[column].mode()[0], inplace=True)
    test[column].fillna(test[column].mode()[0], inplace=True)


ohe = OneHotEncoder(drop='first', handle_unknown='ignore')

X_train = ohe.fit_transform(X_train)
X_val = ohe.transform(X_val)
test = ohe.transform(test)