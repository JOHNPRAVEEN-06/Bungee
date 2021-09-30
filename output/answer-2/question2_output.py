csvFile = pd.read_csv("/content/drive/MyDrive/bungee/internship-test2-master/input/question-2/main.csv")
out=csvFile.groupby('occupation').age.agg(['min', 'max'])
df = pd.DataFrame(out)
df.to_csv('/content/drive/MyDrive/bungee/internship-test2-master/output/answer-2/main.csv')
