import pandas as pd
import matplotlib.pyplot as pyplot
import seaborn as sns

file1=pd.read_csv("test.csv",sep=",")
file2=pd.read_csv("train.csv",sep=",")
file3=pd.read_csv("sample_submission.csv",sep=",")

f=file2["text"].tolist()
for i in range(len(f)):
    f[i]=len(i)
    print(f)