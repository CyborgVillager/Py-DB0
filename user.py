# Try to import source file from the source folder, else notify the user of the issue
try:
    from tk_source import *
except ImportError:
    print('Unable to import tk_source, make sure you have made the source folder classified as source' + '\n' +
          'Thank you')


root = Tk()
# width & height
root.geometry('500x400')


# Aquire information from demo.py for user_name, user's age, and the users address / state
def get_data(user_name, user_age, user_addr):
    try:
        connection = psycopg2.connect(dbname='postgres',
                                      user='postgres',
                                      password='pass123',
                                      host='localhost',
                                      port='5433')
        cursor = connection.cursor()
        print('Connection to DB is successful!')


    # Error if connecting to cursor is unable to process
    except ConnectionError:
        print('Unable to input data onto table, please check lines 52-62!' + '\n'
              + ' Thank you.')

    try:
        # Insert user data onto db table
        query = '''INSERT INTO student(NAME,AGE,ADDRESS) VALUES (%s,%s,%s);'''
        cursor.execute(query, (user_name, user_age, user_addr))

        print('The data has been inserted onto table ')
        connection.commit()
        connection.close()
        display_all()

    except ConnectionError:
        print('Unable to connect to DB ')


def search(id):
    try:
        connection = psycopg2.connect(dbname='postgres',
                                      user='postgres',
                                      password='pass123',
                                      host='localhost',
                                      port='5433')
        cursor = connection.cursor()
        print('Connection to DB is successful!')


        # Error if connecting to cursor is unable to process
    except ConnectionError:
        print('Unable to input data onto table, please check lines 52-62!' + '\n'
              + ' Thank you.')

# compare conditions for specific id from the db -> subistue a
# value from id/get the db(student) that ='s to id
    query = '''select * from student where id=%s'''
    #  hold the data
    cursor.execute(query, (id))
    row = cursor.fetchone()
    # aquire the input from row
    display_search(row)
    connection.commit()
    connection.close()

# input the information for display_search once row has been aquired
def display_search(row):
    listbox = Listbox(frame,width=20,height=5)
    listbox.grid(row=7,column=1)
    listbox.insert(END,row)

def display_all():
    try:
        connection = psycopg2.connect(dbname='postgres',
                                      user='postgres',
                                      password='pass123',
                                      host='localhost',
                                      port='5433')
        cursor = connection.cursor()
        print('Connection to DB is successful!')
        query = '''select * from student '''
        cursor.execute(query)
        row = cursor.fetchall()
# Allows the user to see the other users info
        listbox = Listbox(frame, width=20, height=5)
        listbox.grid(row=12, column=1)
        for x in row: listbox.insert(END, x)

        # Error if connecting to cursor is unable to process
    except ConnectionError:
        print('Unable to input data onto table, please check lines 52-62!' + '\n'
              + ' Thank you.')

# Canvas information
canvas = Canvas(root, height=500, width=200)
canvas.pack
# Frame information
frame = Frame()
frame.place(relx=.3, rely=.1, relwidth=.9, relheight=.8)
# Label to inform the user on what to do
label = Label(frame, text='Add user information here:')
label.grid(row=0, column=1)

# username
label = Label(frame, text='Username')
label.grid(row=1, column=0)
# Username input box
entry_username = Entry(frame)
entry_username.grid(row=1, column=1)

# User age
label = Label(frame, text='Age')
label.grid(row=2, column=0)
# User age input box
entry_user_age = Entry(frame)
entry_user_age.grid(row=2, column=1)

# User State
label = Label(frame, text='State')
label.grid(row=3, column=0)
# user's state input box
entry_user_stateloc = Entry(frame)
entry_user_stateloc.grid(row=3, column=1)

# Submit Button
button = Button(frame, text='Submit', command=lambda: get_data(entry_username.get(),
                                                               entry_user_age.get(),
                                                               entry_user_stateloc.get()
                                                               ))
# Submit button Location
button.grid(row=4, column=1)

# Search Feature
label = Label(frame, text='Search User ID')
label.grid(row=5, column=1)

# Search input box
entry_user_search = Entry(frame)
entry_user_search.grid(row=6, column=1)

label = Label(frame, text='Search: ')
label.grid(row=6, column=0)




# Submit Search Button
button = Button(frame, text='Submit', command=lambda: search(entry_user_search.get()))
# Submit Search button Location
button.grid(row=6, column=2)

display_all()
root.mainloop()
