import pandas as pd
import sys
import matplotlib.pyplot as plt
import seaborn as sns
import os

print("Visualization started...")

file_path = sys.argv[1]
df = pd.read_csv(file_path)

plt.figure(figsize=(15,10))

# Histogram
plt.subplot(2,2,1)
df.select_dtypes(include=['number']).iloc[:,0].hist()
plt.title("Histogram")

# Heatmap
plt.subplot(2,2,2)
corr = df.corr()
sns.heatmap(corr, annot=True)
plt.title("Correlation Heatmap")

# Boxplot
plt.subplot(2,2,3)
sns.boxplot(data=df.select_dtypes(include=['number']))
plt.title("Boxplot")

plt.tight_layout()
plt.savefig("summary_plot.png")

print("Saved summary_plot.png")

os.system("python cluster.py data_preprocessed.csv")
