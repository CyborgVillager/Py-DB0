# import pydb
try:
    from pydb import *
except ImportError:
    print('Unable to import pydb.')



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
    print(row)

    connection.commit()
    connection.close()