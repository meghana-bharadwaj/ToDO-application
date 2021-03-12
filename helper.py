import MySQLdb

DB_PATH='./todo.db'
NOTSTARTED='Not Started'
INPROGRESS = 'In Progress'
COMPLETED = 'Completed'

def add_to_list(item):
    try:
        conn =  MySQLdb.connect(DB_PATH)
        c=conn.cursor()

        c.execute('INSERT INTO ITEMS(item,status) values(?,?)',(item,NOTSTARTED))

        conn.commit()
        return{"item":item,"status":NOTSTARTED}
    except Exception as e:
        print ('Error:',e)
        return None
