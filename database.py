import pandas as pd

import sqlite3

# Read Excel file into a DataFrame

excel_file = './x.xlsx'

data_frame = pd.read_excel(excel_file)

# Connect to SQLite database (Change this to your database type)

conn = sqlite3.connect('hawks1.db')

# Iterate through DataFrame and insert data into database

for index, row in data_frame.iterrows():

# Assuming your table has columns 'column1', 'column2', ...

    query = f"INSERT INTO Test (Meal, Name, Calories) VALUES (?, ?, ...)"

    values = tuple(row) # Convert row data to tuple

# Execute the query

conn.execute(query, values)

# Commit changes and close connection

conn.commit()

conn.close()

print("Data imported successfully!")

#-------------------#-------------------#-------------------#-------------------#-------------------#-------------------

# import sqlite3
# import pandas as pd

# path = '/Users/jeronimo_laptop/Library/CloudStorage/OneDrive-Personal/Documentos/AQUINCY_HW/Programming/Segundo/SoftEngineerProject/DataScrappingCafe.xlsx'
# df = pd.read_excel('x.xlsx')
# conn = sqlite3.connect('test.db')

# c = conn.cursor()
# c.execute("CREATE TABLE IF NOT EXISTS test ({})".format(' ,'.join(df.columns)))