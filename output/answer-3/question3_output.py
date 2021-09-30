import pandas as pd
csvData = pd.read_csv("/content/drive/MyDrive/bungee/internship-test2-master/input/question-3/main.csv")
df=csvData[['Team', 'Yellow Cards', 'Red Cards']]
df.groupby(['Red Cards'])
df.sort_values(["Yellow Cards"], axis=0,ascending=[False], inplace=True)
df.sort_values(["Red Cards"], axis=0,ascending=[False], inplace=True)
df.to_csv('/content/drive/MyDrive/bungee/internship-test2-master/output/answer-3/main.csv')