import pandas as pd
import numpy as np
df=pd.read_csv(r'01.Data Cleaning and Preprocessing.csv')
print("to print the columns : ",df.columns)
print("-------------------------------------------------------------")
#identify he missing value 
print("missing values : ")
print(df.isnull())
print("count the missing value in each column :")
print(df.isnull().sum())
print("fill the missing coulumn SulphidityL-4 by all method : ")
#fill the missing value
print("-------------------------------------------------------------")
print("1st fill with 0 for all missing value :")
df['SulphidityL-4 '].fillna(0 ,inplace=False)
print(df["SulphidityL-4 "])
print("2nd fill missing value with aggregate function:")
df['SulphidityL-4 '].fillna(df['SulphidityL-4 '].mean() ,inplace=False)
print("mean : \n",df["SulphidityL-4 "])
df['SulphidityL-4 '].fillna(df['SulphidityL-4 '].median() ,inplace=False)
print("median : \n",df["SulphidityL-4 "])
df['SulphidityL-4 '].fillna(df['SulphidityL-4 '].mode() ,inplace=False)
print("mode : \n",df["SulphidityL-4 "])
print("fill missing value with forward value :")
df['SulphidityL-4 '].fillna(method='ffill',inplace=False)
print("forward fill : \n",df["SulphidityL-4 "])
print("fill missing value with backward value :")
df['SulphidityL-4 '].fillna(method='bfill',inplace=True)
print("forward fill : \n",df["SulphidityL-4 "])
print("-------------------------------------------------------------")
#statistical function
print("basic statistic functions : \n",df.describe())
#IQR for SulphidityL-4 
q1=df["SulphidityL-4 "].quantile(0.25)
q3=df["SulphidityL-4 "].quantile(0.75)
iqr=q3-q1
print("The Interquartile Range : ",iqr)
print('median for sulphidityl-4 : ',df["SulphidityL-4 "].median())
print('mean for sulphidityl-4 : ',df["SulphidityL-4 "].mean())
print('mode for sulphidityl-4 : ',df["SulphidityL-4 "].mode())
print('standard deviation for sulphidityl-4 : ',df["SulphidityL-4 "].std())
print("-------------------------------------------------------------")