from mysql.connector import MySQLConnection, Error
from mysql_dbconfig import read_db_config
 
 
def insert_wallet(pubkey,privkey):
    """ Connect to MySQL database """
    query = "INSERT INTO vertcoin_wallet(pubkey,privkey) " \
            "VALUES(%s,%s)" 
    args = (pubkey, privkey)

    try:
	db_config = read_db_config()
        conn = MySQLConnection(**db_config)
 
        if conn.is_connected():
            print('connection established.')
	        cursor = conn.cursor()
    	    cursor.execute(query, args)
	        conn.commit()

        else:
            print('connection failed.')
 
    except Error as error:
        print(error)
 
    finally:
        conn.close()
        print('Connection closed.')
 
 
if __name__ == '__main__':
    connect()