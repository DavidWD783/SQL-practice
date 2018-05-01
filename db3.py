# Import packages
import pandas as pd
import numpy as np 
from sqlalchemy import create_engine

# Create engine to  to send queries to database
engine = create_engine('sqlite:///Chinook_Sqlite.sqlite')

# # Inspect tables in the database
table_names = engine.table_names()
print(table_names)

# Create connection to engine
con = engine.connect()

# Use rs to send queries to database
rs = con.execute("SELECT Title, COUNT(*) FROM Employee WHERE Title NOT LIKE 'Sales%' GROUP BY Title;")

# Turn rs object into DataFrame
df = pd.DataFrame(rs.fetchall())

# Set the column headers to the table headers
df.columns = rs.keys()

# Close the connection
con.close()

# Print the header of the dataframe
print(df.head())