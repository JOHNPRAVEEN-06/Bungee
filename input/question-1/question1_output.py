csvFile = pd.read_csv("/content/drive/MyDrive/bungee/internship-test2-master/input/question-1/main.csv")
df=csvFile.groupby((csvFile['Year']//10)*10).sum()
df=df[['Population','Violent','Property','Murder','Forcible_Rape','Robbery','Aggravated_assault','Burglary','Larceny_Theft','Vehicle_Theft']] 
df.to_csv('/content/drive/MyDrive/bungee/internship-test2-master/output/answer-1/main.csv')