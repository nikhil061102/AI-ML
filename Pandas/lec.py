import seaborn as sns
df = sns.load_dataset("exercise")
print(df.head())
print(df.head(9))
print(df.tail())
print(df.tail(7))
print(df.info())
print(df.describe())