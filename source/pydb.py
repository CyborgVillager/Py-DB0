try :
    import psycopg2
except ImportError:
    print('Cannot import psycopg2, please check source/pydb.py line 2 for more information' + '\n'
          + 'Thank you.')