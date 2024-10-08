import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('datasets/WA_Fn-UseC_-HR-Employee-Attrition.csv')

# print(df.head())

#grafico em pizza para ver idade dos funcionarios
# df['Age'].value_counts().plot.pie()
# plt.show()

# grafico de barras para ver quem viaja frequentemente e quem viaja raramente
df['BusinessTravel'].value_counts().plot.bar()
plt.show()