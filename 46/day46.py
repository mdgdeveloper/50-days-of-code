# Create a Dataframe using pandas. You are going to create a
# code to put the following into a Dataframe. You will use the
# information in the table below. Basically, you are going to
# recreate this table using pandas. Use the information in the table
# to recreate the table.

import pandas

# First we create a dictionary
d = {'year': [2009, 2002, 2009, 2010, 2009], 'Title': ["Brothers", "Spider-Man", "WatchMen",
                                                       "Inception", "Avatar"], "genre": ["Drama", "Sci-fi", "Drama", "Sci-fi", "Fantasy"]}

# Create the dataframe
df = pandas.DataFrame(data=d)


# Test
print(df)
