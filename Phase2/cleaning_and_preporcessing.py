import pandas as pd 
import numpy as np

df=pd.read_excel(r"D:\abc\Documents\PROFESSIONAL DATA ANALYTICS WITH GEN AI\Majot Capstone Project\PlayerBehaviorExtensions.xlsx")
print(df.head())
df.info()
df.isnull().sum()