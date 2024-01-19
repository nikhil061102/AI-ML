"""
Encoding types - 
    Hot Encoding
    Label Encoding
    Ordinal Encoding
""" 
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

df = sns.load_dataset("exercise")
print(df.head())
print(df['time'].value_counts())
print(df['kind'].value_counts())
print(df['diet'].value_counts())

# Basic Encoding
time_mapping = {'1 min': 1, '15 min': 15, '30 min': 30}
df['time'] = df['time'].map(time_mapping)
print(df.head())

# Hot Encoding
df = pd.get_dummies(df,columns=['time'])
print(df.head())

from sklearn.preprocessing import OneHotEncoder
encoder = OneHotEncoder()
encoded_data = encoder.fit_transform(df[['time']])
encoded_df = pd.DataFrame(encoded_data.toarray(), columns=encoder.get_feature_names_out(['time']))
df = pd.concat([df, encoded_df], axis=1)
print(df.head())

# Label Encoding
from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()
df['time'] = le.fit_transform(df['time'])
print(df.head())

# Ordinal Encoding
from sklearn.preprocessing import OrdinalEncoder
ordinal_data = df[['diet', 'kind']]
ordinal_encoder = OrdinalEncoder()
encoded_data = ordinal_encoder.fit_transform(ordinal_data)
df[['diet', 'kind']] = encoded_data
print(df.head())