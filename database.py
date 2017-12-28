from mysql.connector import MySQLConnection, Error
from mysql_dbconfig import read_db_config
 
 
def mysql_connect(query, args):
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

def insert_wallet(pubkey,privkey):
    query = "INSERT INTO vertcoin_wallet(pubkey,privkey) " \
            "VALUES(%s,%s)" 
    args = (pubkey, privkey)
    mysql_connect(query, args)

   
def read_wallets():
    query = "SELECT * from vertcoin_wallet"
    try:
	    db_config = read_db_config()
        conn = MySQLConnection(**db_config)
        if conn.is_connected():
            print('connection established.')
	        cursor.execute(query)
            for (pubkey, privkey) in cursor:
                print("Pubkey: {} Privkey: {}".format(pubkey, privkey))
        else:
            print('connection failed.')
 
    except Error as error:
        print(error)
 
    finally:
        conn.close()
        print('Connection closed.')