from pydb import *

# try to connect to db
try:
    connection = psycopg2.connect(dbname='postgres',
                                  user='postgres',
                                  password='pass123',
                                  host='localhost',
                                  port='5433')
    print('Connection is successful!')
# connection error to user, if an error occurs
except ConnectionError:
    print('Unable to connect to DB, please check line 6-9 for the issue' + '\n'
          + 'Thank you.')

# Basic input for DB creation
print('Basic table creation via terminal, can just type them out as well'
      + 'e.g -> NAME TEXT, AGE INT, ADDRESS TEXT, etc,etc.' + '\n' +
      'Figured to test out the inputs for DB creations as well (^_*)')
print('\n')
# ask user table name
table_name = input('Please type your table name: ')


# Cursor/ table query creation
def create_table():
    try:
        cursor = connection.cursor()
        cursor.execute('''
        CREATE TABLE student(
        ID SERIAL,
        NAME TEXT,
        AGE INT,
        ADDRESS TEXT);''')

        # commit changes after connecting to cursor
        connection.commit()
        print('Table ' + table_name + ' is commited')
        connection.close()
        print('Table ' + table_name + ' is closed')
        # print successful result to connection
        print('Connection to ' + table_name + ' is successful!')

    # error if connecting to cursor is unable to process
    except ConnectionError:
        print(
            'Unable to create table,' + table_name + ' please check function create_table() for more information!' + '\n'
            + ' Thank you.')


def insert_data():
    try:
        connection = psycopg2.connect(dbname='postgres',
                                      user='postgres',
                                      password='pass123',
                                      host='localhost',
                                      port='5433')

        # Enter user info
        user_name = input('What is the student name?:  ')

        # user age
        user_age = int(input('How old is the student?: '))


        # user address
        user_addr =  input('What is ' + user_name + ' state?: ')

        print('Connection to table ' + table_name + ' is a success ' + '\n')
        cursor = connection.cursor()

        # Insert user data onto db table
        query  = '''INSERT INTO ''' + table_name + '''(NAME,AGE,ADDRESS) VALUES (%s,%s,%s);'''
        cursor.execute(query,(user_name,user_age,user_addr))

        # commit changes after connecting to cursor
        connection.commit()
        print('Inserted data onto ' + table_name + ' it is now commited')
        print('Submitted info to DB, username is: ' + user_name + ' age is ' + str(user_age) + ' ' +
              user_name + ' addr is: ' + user_addr)
        print('\n')
        # Close connection
        connection.close()
        print('Inserted data onto ' + table_name + ' is now closed')
        # print successful result to connection
        print('Connection to ' + table_name + ' is successful!')

        # error if connecting to cursor is unable to process
    except ConnectionError:
        print('Unable to input data onto table,' + table_name + ' please check lines 52-62!' + '\n'
              + ' Thank you.')


def main():
    #create_table()
    insert_data()


main()
