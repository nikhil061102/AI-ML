# feature scaling
import seaborn as sns
import pandas as pd

df = sns.load_dataset("iris")
print(df.describe())
# print(df.head())

# Min-Max Scaling
from sklearn.preprocessing import MinMaxScaler
scaler = MinMaxScaler()
df[["sepal_width"]] = scaler.fit_transform(df[["sepal_width"]])
print(df.head())

features = df.drop('species', axis=1)
scaler = MinMaxScaler()
scaled_features = scaler.fit_transform(features)
df_scaled = pd.DataFrame(scaled_features, columns=features.columns)
df = pd.concat([df_scaled, df['species']], axis=1)
print(df.describe())


# Normalization
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
df[["sepal_width"]] = scaler.fit_transform(df[["sepal_width"]])
print(df.describe())

features = df.drop('species', axis=1)
scaler = StandardScaler()
scaled_features = scaler.fit_transform(features)
df_scaled = pd.DataFrame(scaled_features, columns=features.columns)
df = pd.concat([df_scaled, df['species']], axis=1)
print(df.describe())