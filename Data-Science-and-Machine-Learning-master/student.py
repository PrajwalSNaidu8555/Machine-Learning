import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt 
import seaborn as sns

stud=pd.read_csv("StudentsPerformance.csv")
print("*****DATA HEADERS*****")
print(stud.head(10))
print("****DATA DESCRIPTION****")
stud.info()
stud.describe()
stud1 = stud.drop(['lunch','test preparation course'],axis=1)
stud1["parental level of education"] = stud1["parental level of education"].fillna("high school")
#print(stud1["parental level of education"])
stud1["race/ethnicity"]=stud1["race/ethnicity"].map({
    "group A":"Asian Students",
    "group B":"African Students",
    "group C":"Afro-Asian Students",
    "group D":"American Students",
    "group E":"European Students"
})
print(stud1.head(10))
ax = sns.countplot(hue="gender",x="test preparation course",data=stud,palette="Set1")
ax.set(title="Gender vs test preparation course",xlabel="Gender",ylabel="test preparation course")
plt.show()
ax = sns.countplot(hue="race/ethnicity",x="gender",data=stud1,palette="Set2")
ax.set(title="Gender vs Ethnicity",xlabel="Ethnicity",ylabel="Gender")
plt.show()
marks_intervals = [0,40,50,60,75]
categories = ['failed','second class','first class','distinction']
stud1['Marks_categories_math']=pd.cut(stud1.mathscore,marks_intervals,labels=categories)
ax = sns.countplot(x="Marks_categories_math",hue="gender",data=stud1,palette="Set1")
ax.set(title="Math vs gender",xlabel="Marks",ylabel="total")
plt.show()
stud1['Marks_categories_reading']=pd.cut(stud1.readingscore,marks_intervals,labels=categories)
ax = sns.countplot(x="Marks_categories_reading",hue="gender",data=stud1,palette="Set2")
ax.set(title="Reading vs gender",xlabel="Marks",ylabel="total")
plt.show()
stud1['Marks_categories_writing']=pd.cut(stud1.writingscore,marks_intervals,labels=categories)
ax = sns.countplot(x="Marks_categories_writing",hue="gender",data=stud1,palette="Set3")
ax.set(title="Writing vs gender",xlabel="Marks",ylabel="total")
plt.show()
