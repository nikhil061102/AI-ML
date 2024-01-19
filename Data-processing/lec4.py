import pandas as pd
import seaborn as sns


# Create a sample DataFrame
data = {
    'Feature1': [1, 2, 3, 4, 5],
    'Feature2': [5, 4, 3, 2, 1],
    'Feature3': [2, 3, 1, 5, 4],
    'Feature4': [4, 5, 2, 1, 3]
}

df = pd.DataFrame(data)

import matplotlib.pyplot as plt
correlation_matrix = df.corr()

# Plot the correlation matrix using seaborn
plt.figure(figsize=(8, 6))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f", linewidths=0.5)
plt.title('Correlation Matrix')
plt.show()
