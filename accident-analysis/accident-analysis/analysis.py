import pandas as pd
df = pd.read_csv("accident.csv")
print(df.shape)
print(df.head())
print(df.info())
print(df.isna().sum())
print(df.nunique())
print(df["Age"].describe())
print(df["Speed_of_Impact"].describe())
import matplotlib.pyplot as plt
#simple histogram
df["Age"].hist(bins=20)
plt.title("Age Distribution")
plt.show()  #Graph of age
df["Speed_of_Impact"].hist(bins=20)
plt.title("Speed of Impact Distribution")
plt.show()   #graph of speed 
#gender and outcome relationship
print(df["Gender"].value_counts()) #male female separation
#male/female +ve outcome?
print(df.columns)
print(df.groupby("Gender")["Survived"].mean())
print(df.groupby("Seatbelt_Used")["Survived"].mean())
#categorical colums (yes/no)
yes_no_cols = [c for c in df.columns if df[c].dtype == "object" and set(df[c].unique()) <= {"Yes","No"}]
for col in yes_no_cols:
    print(col)
    print(df[col].value_counts())
#numerical colums(correlation)
print(df.corr(numeric_only=True))
import seaborn as sns
#make plots look better
sns.set(style="whitegrid")
print("Shape of datasets:",df.shape)
#basic info and summery
df.info()
df.describe()
#correlation heat map
plt.figure(figsize=(8,6))
sns.heatmap(df.corr(numeric_only=True),annot=True,cmap="coolwarm")
plt.title("Correlation Heatmap")
plt.show()
# %%
import pandas as pd

# %%
df = pd.read_csv("accident.csv")
df.head()
# %%
df.describe()
# %%
print(df.columns)
print(df.groupby("Gender")["Survived"].mean())
print(df.groupby("Seatbelt_Used")["Survived"].mean())
# %%
yes_no_cols = [c for c in df.columns if df[c].dtype == "object" and set(df[c].unique()) <= {"Yes","No"}]
for col in yes_no_cols:
    print(col)
    print(df[col].value_counts())
# %%
#basic info and summery
df.info()
df.describe()
# %%

# %%
import seaborn as sns
#make plots look better
#make plots look better
sns.set(style="whitegrid")
print("Shape of datasets:",df.shape)

# %%
import matplotlib.pyplot as plt
# %%
#correlation heat map
plt.figure(figsize=(8,6))
sns.heatmap(df.corr(numeric_only=True),annot=True,cmap="coolwarm")
plt.title("Correlation Heatmap")
plt.show()
# %%
#simple histogram
df["Age"].hist(bins=20)
plt.title("Age Distribution")
plt.show()  #Graph of age
df["Speed_of_Impact"].hist(bins=20)
plt.title("Speed of Impact Distribution")
plt.show()   #graph of speed 
# %%
#numerical colums(correlation)
print(df.corr(numeric_only=True))
# %%
#categorical colums (yes/no)
yes_no_cols = [c for c in df.columns if df[c].dtype == "object" and set(df[c].unique()) <= {"Yes","No"}]
for col in yes_no_cols:
    print(col)
    print(df[col].value_counts())

