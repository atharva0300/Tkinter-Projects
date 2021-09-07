from tkinter import *
import sqlite3

root = Tk() 
root.title("Talk")
root.iconbitmap('C:/Users/windows/Desktop/Python_Projects/Tkinter/talk.ico')
# Using databases for tkinter and python 
#Create a database or connect to one 
conn = sqlite3.connect('Address_book.db')

# creating a cursor
c = conn.cursor()

# create a table 
c.execute("""CREATE TABLE addresses (
    first_name text, 
    last_name text,
    address text,
    city text,
    state text,
    zipcode integers
    )""")

# commit chages 
conn.commit()

# the connection automatically closses 
# But to try it to do it manually 
# Here's how to do it 
conn.close()


root.mainloop()

