import matplotlib.pyplot as plt
import seaborn as sns

# print(sns.get_dataset_names())

df = sns.load_dataset("tips")
print(df.head())

# BOXPLOT
df.boxplot(by = "day", column = ["total_bill"], grid = False)
plt.show()
sns.boxplot(x='day', y='total_bill', data=df)
plt.show()
sns.boxplot(x='day', y='total_bill', data=df, hue='day')
plt.show()

# DISTPLOT
bill = df['total_bill']
sns.distplot(bill,bins=30,kde=False)
plt.show()

# REGPLOT
sns.regplot(x="total_bill", y="tip", data=df)
plt.show()