import pandas as pd
import numpy as np
import sqlite3

conn = sqlite3.connect('../chinook.db')
cursor = conn.cursor()

df = pd.read_sql('SELECT * from albums', conn)
conn.close()

print(df.columns[0])  # Show first 5 rows

# df_filtered = df[df["ArtistId"] > 10]
# print(df_filtered)

df.to_csv("updated_people.csv", index=False)

