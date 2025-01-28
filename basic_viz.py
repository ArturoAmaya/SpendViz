import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

fig, axes = plt.subplots(1,1)
data = pd.read_csv("data.csv")
data = data[data['Month']==12] # arbitrary for now
data['Amount'] = data["Amount"].str.replace('$', '')
data['Amount'] = pd.to_numeric(data["Amount"], downcast="float")
mean_value = data['Amount'].mean()
data = data.groupby(['Day']).agg(daily_spend=("Amount", "mean"))
sns.barplot(data=data, x="Day", y="daily_spend", estimator=sum, ax=axes)
axes.axhline(mean_value, color='red', linestyle='--', label=f"Average daily spending")
plt.show()