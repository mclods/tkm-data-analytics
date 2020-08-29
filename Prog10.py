import pandas as pd
import seaborn as sns

df=pd.read_csv('data.csv')

heatmap1_data=df.pivot('country','year','gdpPercap')
print(heatmap1_data)
sns.heatmap(heatmap1_data).get_figure().savefig('heatmap1.png')
