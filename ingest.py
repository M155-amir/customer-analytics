import pandas as pd
import sys
import os

print("Script started")

file_path = sys.argv[1]

print("Reading file...")

df = pd.read_csv(file_path)

print("Data loaded successfully!")

df.to_csv("data_raw.csv", index=False)

print("Saved data_raw.csv")

os.system("python preprocess.py data_raw.csv")
