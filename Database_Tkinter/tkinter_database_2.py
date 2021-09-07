from tkinter import *
import sqlite3

root = Tk() 
root.title("Database Manager")
root.iconbitmap('C:/Users/windows/Desktop/Python_Projects/Tkinter/talk.ico')

# addig studd to the table 
# Address_book.db

conn =sqlite3.connect('Address_book.db')

# create cursor 
c= conn.cursor()

#create text boxes 
f_name = Entry (root, width=30)
f_name.grid(row =0 , column=1 , padx=20)

l_name = Entry (root, width=30)
l_name.grid(row =1 , column=1)

address = Entry (root, width=30)
address.grid(row =2 , column=1)

city = Entry (root, width=30)
city.grid(row =3 , column=1)

state = Entry (root, width=30)
state.grid(row =4 , column=1)

zipcode = Entry(root, width=30)
zipcode.grid(row=5, column =1)

delete_box = Entry(root, width = 30)
delete_box.grid(row=9 , column =1)

# cREATE TEXT BOX labels 
f_name_label = Label(root, text = "First name")
f_name_label.grid(row=0 , column=0,pady=(10,0) )

l_name_label = Label(root, text = "Last name")
l_name_label.grid(row=1 , column=0)

address_label = Label(root, text = "address")
address_label.grid(row=2 , column=0)

city_label = Label(root, text = "city")
city_label.grid(row=3 , column=0)

state_label = Label(root, text = "State")
state_label.grid(row=4 , column=0)

zipcode_label = Label(root, text = "Zip code")
zipcode_label.grid(row=5 , column=0)

delete_box_label = Label(root, text="Delete ID")
delete_box_label.grid(row=9 ,column=0)

# Create an update function 
def update()  :
    # addig studd to the table 
    # Address_book.db
    conn =sqlite3.connect('Address_book.db')

    # create cursor 
    c= conn.cursor()

    record_id = delete_box.get()

    c.execute("""UPDATE addresses SET 
            first_name = :first,
            last_name = :last,
            address = :address,
            city = :city,
            state = :state,
            zipcode = :zipcode

            WHERE oid = :oid""",
            {   
                'first' : f_name_editor.get(),
                'last': l_name_editor.get(),
                'address' : address_editor.get(),
                'city' : city_editor.get(),
                'state' : state_editor.get(),
                'zipcode' : zipcode_editor.get(),
                'oid' : record_id
            })

    # addig studd to the table 
    # Address_book.db
    conn =sqlite3.connect('Address_book.db')

    # create cursor 
    c= conn.cursor()



# Defining edit function 
def edit(): 
    editor = Tk() 
    editor.title("Edit Record")
    editor.iconbitmap('C:/Users/windows/Desktop/Python_Projects/Tkinter/talk.ico')

    # Creating global varialbes for text box name 
    global f_name_editor
    global l_name_editor
    global address_editor
    global city_editor
    global state_editor
    global zipcode_editor

    #create text boxes 
    f_name_editor = Entry (editor, width=30)
    f_name_editor.grid(row =0 , column=1 , padx=20)

    l_name_editor = Entry (editor, width=30)
    l_name_editor.grid(row =1 , column=1)

    address_editor = Entry (editor, width=30)
    address_editor.grid(row =2 , column=1)

    city_editor = Entry (editor, width=30)
    city_editor.grid(row =3 , column=1)

    state_editor = Entry (editor, width=30)
    state_editor.grid(row =4 , column=1)

    zipcode_editor = Entry(editor, width=30)
    zipcode_editor.grid(row=5, column =1)

    # CREATE TEXT BOX labels 
    f_name_label = Label(editor, text = "First name")
    f_name_label.grid(row=0 , column=0,pady=(10,0) )

    l_name_label = Label(editor, text = "Last name")
    l_name_label.grid(row=1 , column=0)

    address_label = Label(editor, text = "address")
    address_label.grid(row=2 , column=0)

    city_label = Label(editor, text = "city")
    city_label.grid(row=3 , column=0)

    state_label = Label(editor, text = "State")
    state_label.grid(row=4 , column=0)

    zipcode_label = Label(editor, text = "Zip code")
    zipcode_label.grid(row=5 , column=0)

    # create a save button to save edited records 
    edit_button = Button(editor, text="Save Record" ,command = update)
    edit_button.grid(row =6, column=0 ,columnspan=2 ,padx=10 , pady=10 , ipadx=137)

    # addig studd to the table 
    # Address_book.db
    conn =sqlite3.connect('Address_book.db')

    # create cursor 
    c= conn.cursor()

    record_id = delete_box.get()
    # Query the database 
    c.execute("SELECT * FROM addresses WHERE oid = " + record_id)
    records = c.fetchall()

    #Loop through results 
    for item in records: 
        f_name_editor.insert(0,item[0])
        l_name_editor.insert(0,item[1])
        address_editor.insert(0,item[2])
        city_editor.insert(0,item[3])
        state_editor.insert(0,item[4])
        zipcode_editor.insert(0,item[5])


# create function to delete to a record 
def delete() : 
    # addig studd to the table 
    # Address_book.db

    conn =sqlite3.connect('Address_book.db')

    # create cursor 
    c= conn.cursor()

    # delete from a record 
    # deleting by oid - placeholder 
    c.execute("DELETE from addresses WHERE oid=" + delete_box.get())

    #Commiting the changes 
    conn.commit() 
    # Closing the database
    conn.close()

# submit fuction 
# create sumit fuction 
def submit() : 
    # addig studd to the table 
    # Address_book.db

    conn =sqlite3.connect('Address_book.db')

    # create cursor 
    c= conn.cursor()

    # Insert into Tabl e 
    c.execute("INSERT INTO addresses VALUES (:f_name , :l_name, :address , :city , :state, :zipcode)",
            {
                'f_name' : f_name.get(),
                'l_name' : l_name.get(),
                'address' : address.get(),
                'city' : city.get(),
                'state' : state.get(),
                'zipcode' : zipcode.get()
            })


    #Commiting the changes 
    conn.commit() 
    # Closing the database
    conn.close()

    # clear the text boxes 
    f_name.delete(0,END)
    l_name.delete(0,END)
    address.delete(0,END)
    city.delete(0,END)
    state.delete(0,END)
    zipcode.delete(0,END)

# Create a query function 
def query()  :
    # addig studd to the table 
    # Address_book.db

    conn =sqlite3.connect('Address_book.db')

    # create cursor 
    c= conn.cursor()

    # Query the database 
    c.execute("SELECT * , oid FROM addresses")
    records = c.fetchall() 
    print(records)

    # Loop through results 
    print_records=''
    # Creating a for loop 
    for item in records: 
        print_records = print_records+ str(item[0]) + ' ' + str(item[1]) + '\t' + str(item[6]) + '\n'

    query_label = Label(root, text=print_records)
    query_label.grid(row=12, columnspan=2 , pady=10)

    #Commiting the changes 
    conn.commit() 
    # Closing the database
    conn.close()

# Show records button
query_btn = Button(root, text="Show Records", command = query)
query_btn.grid(row=7, column=0 , columnspan =2 , pady = 10 , padx = 10 , ipadx =129)

# Create a Delete button 
delete_btn = Button(root, text="Delete Record", command = delete)
delete_btn.grid(row=10 , column=0 , columnspan =2 , pady = 10 , padx = 10 , ipadx =127)

# Create submit button 
submit_button = Button(root, text="Add record to Dataase" , command = submit)
submit_button.grid(row = 6 , column=0 , columnspan=2 , pady=10,padx=10,ipadx = 100)

# Update Button
update_button = Button(root, text="Edit record" ,command = edit)
update_button.grid(row =11, column=0 ,columnspan=2 ,padx=10 , pady=10 , ipadx=137)

#Commiting the changes 
conn.commit() 
# Closing the database
conn.close()


root.mainloop() 