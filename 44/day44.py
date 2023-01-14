# Create a function called save_emails. This function takes no
# arguments but asks the user to input email, and it saves the
# emails in a CSV file. The user can input as many emails as they
# want. Once they hit ‘done’ the function saves the emails and
# closes the file. Create another function called open_emails.
# This function opens and reads the content of the CSV file. Each
# email must be in its line. Here is an example of how the emails
# must be saved:
# jj@gmail.com
# kate@yahoo.com
# and not like this:
# jj@gmail.comkate@yahoo.com


def save_emails():

    f = open("emails.csv", "a")
    email = input("Introduce an email: ")
    while (email != "done"):
        f.write(f"{email}\n")
        email = input("Introduce an email: ")
    f.close()


def open_emails():
    f = open("emails.csv", "r")
    content = f.read()
    print(content)
    f.close()


# Test
save_emails()
open_emails()
