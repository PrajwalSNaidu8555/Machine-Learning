import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt 
import seaborn as sns

bf=pd.read_csv("BlackFriday.csv")
bf.drop(['User_ID','Product_ID','Stay_In_Current_City_Years'],axis=1,inplace=True)
bf["City_Category"] = bf["City_Category"].fillna("A")
bf["City_Category"] = bf["City_Category"].map({
    "A":"Metro cities",
    "B":"Small Cities",
    "C":"Village Cities"
})
bf["Marital_Status"] = bf["Marital_Status"].map({
    0:"Married",
    1:"Single"
})
bf.rename(columns={"Product_Category_1":"Baseball Caps","Product_Category_2":"Wine tumblers","Product_Category_3":"Pet Raincoats"},inplace=True)
print(bf.head(10))
ax=sns.countplot(hue="Gender",x="Baseball Caps",data=bf,palette="Set1")
ax.set(title="Gender vs Baseball Caps",xlabel="Gender",ylabel="Baseball caps")
plt.show()
ax=sns.countplot(hue="Gender",x="Wine tumblers",data=bf,palette="Set2")
ax.set(title="Gender vs Wine tumblers",xlabel="Gender",ylabel="Wine tumblers")
plt.show()
ax=sns.countplot(x="City_Category",hue="Gender",data=bf,palette="Set3")
ax.set(title="City categories vs Gender",xlabel="Categories",ylabel="Total")
plt.show()


