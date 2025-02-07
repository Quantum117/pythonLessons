def create_table(curs):
    curs.execute("""CREATE TABLE Books(
                 Title text,
                 Author text,
                 Year_Published integer,
                 Genre text )
    """)


def insert_to_db (curs):
    # here we used named placeholders (:name) that uses dictionary  to prevent sql injection
    title = input('Enter the Title : ').strip()
    author = input('Author : ').strip()
    year = int(input('Year published : '))
    genre = input('Genre : ').strip()
    query ="INSERT INTO Books (Title, Author, Year_Published, Genre)  VALUES (:title, :author, :year, :genre)"
    params = {"title": title, "author": author, "year": year, "genre":genre}
    curs.execute(query, params)
    print("success, data inserted to db")