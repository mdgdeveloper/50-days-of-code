import sqlite3

# Connection towards the database
con = sqlite3.connect("movies.db")
cur = con.cursor()

# Process to create the Table
cur.execute("DROP TABLE movie")
cur.execute("CREATE TABLE movie(year, title, genre)")
cur.execute("""
INSERT INTO movie values (2009,'Brothers','Drama'),(2002,'Spider Man','Sci-fi'),(2009, 'Watchmen', 'Drama'),(2010,'Inception','Sci-fi'),(2009,'Avatar','Fantasy')
""")
con.commit()

# a) Run SQL query to see all the movies in your table
res = cur.execute("SELECT * FROM movie")
print(res.fetchall())

# b) Select only the movie Brothers
res = cur.execute("SELECT * FROM movie WHERE title='Brothers'")
print(res.fetchone())

# c) Select movies released in 2009
res = cur.execute("SELECT * FROM movie WHERE year=2009")
print(res.fetchall())

# d) Select movies in the fantasy and drama genre
res = cur.execute("SELECT * FROM movie WHERE genre='Drama' OR genre='Fantasy'")
print(res.fetchall())

# e) Delete all contents of the table
res = cur.execute("DELETE FROM movie")
res = cur.execute("SELECT * FROM movie")
print(res.fetchall())
