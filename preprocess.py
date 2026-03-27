import pandas as pd
import sys
import os
from sklearn.preprocessing import StandardScaler

print("Preprocessing started...")

file_path = sys.argv[1]
df = pd.read_csv(file_path)

df.replace("NA", pd.NA, inplace=True)


num_cols = df.select_dtypes(include=['number']).columns
df[num_cols] = df[num_cols].fillna(df[num_cols].mean())

cat_cols = df.select_dtypes(include=['object','string']).columns
for col in cat_cols:
    df[col] = df[col].fillna(df[col].mode()[0])

df.drop_duplicates(inplace=True)

df["Brand"] = df["Brand"].str.replace(r"-NA", "", regex=True).str.strip()


if 'Model' in df.columns:
    df.drop('Model', axis=1, inplace=True)

df['Price_Category'] = pd.cut(df['Price'], bins=3, labels=['Low', 'Medium', 'High'])

df['Registration'] = df['Registration'].astype(str).str.lower().map({'yes': 1, 'no': 0})

categorical_cols = ['Brand', 'Body', 'Engine Type', 'Price_Category']
df = pd.get_dummies(df, columns=categorical_cols, drop_first=True)


columns_to_scale = ['Price', 'Mileage', 'EngineV', 'Year']

scaler = StandardScaler()
df[columns_to_scale] = scaler.fit_transform(df[columns_to_scale])

df.to_csv("data_preprocessed.csv", index=False)

print("Saved data_preprocessed.csv")

os.system("python analytics.py data_preprocessed.csv")
