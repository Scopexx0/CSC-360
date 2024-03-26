import pandas as pd

archivo = './x.csv'

df = pd.read_csv(archivo)

# Heads first 5 elements
# print(df.head())
# Print the last '20' elements
# print(df.tail(20))

# filtering also could be like the example of the nuggets.
# print(df.loc[df['Filter'] == "PR"])

# Type of meal usr wants to pick.
lnch = df[(df['Meal'] == 'Lunch')]

# Searcher for something specific. (probably filtering also)
nugs = df[df['Name'].str.contains('Nuggets')]
print(nugs)

