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