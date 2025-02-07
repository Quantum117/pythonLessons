
def create_table(cursor):
    cursor.execute("""CREATE TABLE Roster (
                   Name text,
                   Species text,
                   Age integer
                   )""")

def insert_to_db (curs, name, species, age):
    # here we used named placeholders (:name) that uses dictionary  to prevent sql injection
    name = name.strip()
    species = species.strip()
    age = int(age)
    query ="INSERT INTO Roster (Name, Species, Age)  VALUES (:name, :species, :age)"
    params = {"name": name, "species": species, "age": age}
    curs.execute(query, params)


#create_table()r
def populate_db(cursor):
    insert_to_db(cursor,"Benjamin Sisko", 'Human', 40)
    insert_to_db(cursor,'Jadzia Dax', 'Trill', 300)
    insert_to_db(cursor,"Kira Nerys", 'Bajoran', 29)

def close_connection(connection):
    # saving changes to db
    connection.commit()
    #closing the connection
    connection.close()

# query = "Select * from Roster"
# data = cursor.execute(query)
# sample = data.fetchone()
#
# print(sample)
def update_name(conn, cursor):
    update_query = "UPDATE Roster SET name = :new_name WHERE age = :age"
    cursor.execute(update_query,{"new_name":"Ezri Dax","age":300 })
    close_connection(conn)
    search_query = "SELECT * from Roster WHERE name = :name"
    sample = cursor.execute(search_query, {"name":"Ezri Dax"}).fetchall()
    print(sample)

def add_bajoran (cursor):
    search_query = "SELECT * from Roster WHERE species = :species"
    sample = cursor.execute(search_query, {"species":"Bajoran"}).fetchall()
    print(sample)

def delete_ (conn, cursor):
    delete_query = "DELETE  from Roster WHERE age > 100 "
    cursor.execute(delete_query)
    close_connection(conn)

def add_ranks(cursor):
    query = 'ALTER TABLE Roster ADD COLUMN Rank TEXT'
    cursor.execute(query)
    names_tuple = cursor.execute('SELECT name from Roster ').fetchall()
    names = [name[0] for name in names_tuple]
    ranks = ['Captain', 'Lieutenant', 'Major']
    data = [{'rank':rank, 'name': name } for name, rank in zip(names, ranks)]

    cursor.executemany(
        'UPDATE Roster SET Rank = :rank WHERE name = :name ',
        data
    )