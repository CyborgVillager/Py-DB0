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
table_usernames = input('Type Usernames: ')
table_age = input('Type Age: ')
table_address = input('Type Address: ')

# Cursor/ table query creation
try:
    cursor = connection.cursor()
    cursor.execute('''
    CREATE TABLE student(
    ID SERIAL,
    table_name TEXT,
    table_age INT,
    table_address TEXT);''')

    # commit changes after connecting to cursor
    connection.commit()
    print('Table ' + table_name + ' is commited')
    connection.close()
    print('Table ' + table_name + ' is closed')
    # print successful result to connection
    print('Connection to ' + table_name + ' is successful!')

# error if connecting to cursor is unable to process
except ConnectionError:
    print('Unable to create table,' + table_name + ' please check lines 18-28!' + '\n'
          +' Thank you.')