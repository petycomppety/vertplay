from bitcoinrpc.authproxy import AuthServiceProxy, JSONRPCException
from database import insert_wallet
import vertcoin_config

def connect():
    global rpc_connection
    username, password = vertcoin_config.read_vertcoin_config()
    rpc_connection = AuthServiceProxy("http://%s:%s@127.0.0.1:5888"%(username, password))
    

def create_wallet():
    wallet = rpc_connection.getnewaddress()
    privkey = rpc_connection.dumpprivkey(wallet)
    print "Your new wallet is:" + wallet
    print "Your privkey is" + privkey
    insert_wallet(wallet, privkey)

def balance():
    print "Your balance is %f" % (rpc_connection.getbalance())
    print "Your other balance is %f" % (rpc_connection.getreceivedbyaddress("VrR8YGqcGVt4F9ZKPYKBpiAviLfgoByr49"))


def main():
    connect()
    create_wallet()
 
if __name__ == '__main__':
    main()


