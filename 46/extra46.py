# Create a code that extracts data from a website. You will extract a
# table from the website. And from that table you will extract columns
# about the data types in Python and their mutability. You will extract
# information from the following website:
# https://en.wikipedia.org/wiki/Python_(programming_language)
# The following table (next page) is what you will extract from the
# website.

# Once you extract this table, you will write a code that will extract
# the data types and their mutability (Two columns). Here is how
# your output should look:

import pandas
# Test

table = pandas.read_html(
    "https://en.wikipedia.org/wiki/Python_(programming_language)")

# We get the table we need
result = table[1]

# Remove not needed columns
result.drop(list(result)[2:], inplace=True, axis=1)
