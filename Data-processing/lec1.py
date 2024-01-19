import seaborn as sns

df = sns.load_dataset("titanic")
# print(df.head())
print(df.isnull().sum())

# replace missing values with mean
# df["age"] = df["age"].fillna(df['age'].mean())
# # replace missing values with mode
# df['deck'] = df['deck'].fillna(df['deck'].mode()[0])
# # # Replace missing values with median
# df["age"] = df["age"].fillna(df['age'].median())

# print(df.isnull().sum())

# simple imputer for "missing" category 
from sklearn.impute import SimpleImputer
import numpy as np
# strategy default=’mean’
# The imputation strategy.
# If “mean”, then replace missing values using the mean along each column. Can only be used with numeric data.
# If “median”, then replace missing values using the median along each column. Can only be used with numeric data.
# If “most_frequent”, then replace missing using the most frequent value along each column. Can be used with strings or numeric data. If there is more than one such value, only the smallest is returned.
# If “constant”, then replace missing values with fill_value. Can be used with strings or numeric data.

numeric_imputer = SimpleImputer(strategy="mean")
df[['age']] = numeric_imputer.fit_transform(df[['age']])

# Instantiate SimpleImputer with strategy='most_frequent' for categorical columns
categorical_imputer = SimpleImputer(strategy='most_frequent')
df[['embarked', 'deck', 'embark_town']] = categorical_imputer.fit_transform(df[['embarked', 'deck', 'embark_town']])
print(df.isnull().sum())