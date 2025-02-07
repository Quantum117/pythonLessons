import sqlite3
from helper_functions import create_table, insert_to_db, populate_db, close_connection, update_name


# Connect to DB and create a cursor
conn = sqlite3.connect('roster.db')

# Create cursor
cursor = conn.cursor()

#Create table Roster
create_table(cursor)

#Inserting data to table
populate_db(cursor)

#updating name
update_name(conn, cursor)

# commiting changes and closing connection
close_connection(conn)
