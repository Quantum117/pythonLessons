import sqlite3
from helper import create_table, insert_to_db
conn = sqlite3.connect('library.db')
cursor = conn.cursor()

#creating the table
# create_table(cursor)

# inserting to db required data
# for i in range(3):
#   insert_to_db(cursor)


#Update data
'''Update the Year_Published of 1984 to 1950.'''

with sqlite3.connect('library.db') as con:
    query =""" 
        UPDATE Books
        SET Year_Published = ?
        WHERE Title = ?
    """
new_year = 1950
title = '1984'

cursor.execute(query,(new_year,title))

'''4.Retrieve and display the Title and Author of all books where the Genre is Dystopian.'''
query = """ 
          SELECT  Title, Author
          FROM Books
          WHERE Genre = ?
  """
genre = 'Dystopian'

cursor.execute(query, (genre,))

data = cursor.fetchall()

for row in data:
  print(f"Title : {row[0]}, Author: {row[1]}")



'''Remove all books published before the year 1950 from the table.'''

query =""" 
        DELETE 
        FROM Books
        WHERE Year_published < 1950
"""

cursor.execute(query)
con.commit()

'''Add a new column called Rating to the Books table and update the data with the following values:'''
with sqlite3.connect('library.db') as con:
    cursor = con.cursor()
    add =""" 
            ALTER TABLE Books
            ADD COLUMN Rating;
        """
    update = """        
            UPDATE Books
            SET Rating = ?
            Where Title = ?
    """

    title1 = "To Kill a Mockingbird"
    rating1 = 4.8

    title2 = "1984"
    rating2 = 4.7

    title3 = 'The Great Gatsby'
    rating3 = 4.5

    cursor.execute(add)

    cursor.execute(update,(rating1,title1))
    cursor.execute(update,(rating2,title2))
    cursor.execute(update,(rating3,title3))

    con.commit()
    cursor.close()
'''Retrieve all books sorted by their Year_Published in ascending order.'''

with sqlite3.connect('library.db') as con:
  cursor = con.cursor()

  query = """ 
        SELECT *
        FROM Books
        ORDER BY Year_Published
    """
  cursor.execute(query)

  books = cursor.fetchall()

  for book in books:
    title, author, year_published, genre, rating = book
    print(
      f"Title: {title}\nAuthor: {author}\nYear Published: {year_published}\nGenre: {genre}\nRating: {rating}\n{'-' * 30}")

  cursor.close()

conn.commit()
conn.close()