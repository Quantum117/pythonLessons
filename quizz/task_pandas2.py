import pandas as pd

df = pd.read_csv("TestMax.csv")
# it should be boolean value to sort df
#df_sorted = df[df['Max1'],df['Max2'], df['Max3']]

# we need two lists one for years and other for max values of three table from each row
max_values = []
years = df['Year1']
for i in range(len(df)):
    max_values.append(int(max(df['Max1'][i],df['Max2'][i],df['Max3'][i])))
res_df = pd.DataFrame({'Years':years, 'MaxValues':max_values})
print(res_df)