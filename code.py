import pandas as pd
df = pd.read_excel("Liver_Disease_WITH_Duplicates.xlsx")
print("Duplicates found:", df.duplicated().sum())
df = df.drop_duplicates()
print("Missing values:\n", df.isnull().sum())
df['Gender'] = df['Gender'].map({'Male': 1, 'Female': 0})  # Male = 1, Female = 0
df.to_excel("Liver_Disease_Cleaned.xlsx", index=False)
print("Cleaned Data:\n", df.head())