from bitcoinrpc.authproxy import AuthServiceProxy

# Connect to local Bitcoin Core instance
rpc_user = "leodg"
rpc_password = "Leo.231987"
rpc_connection = AuthServiceProxy("http://%s:%s@192.168.15.12:8332" % (rpc_user, rpc_password))

# Get list of unconfirmed transactions
unconfirmed_txs = rpc_connection.getrawmempool()

# Print the memory pool
# print(unconfirmed_txs)

# Print the number of unconfirmed transactions
print("Number of unconfirmed transactions:", len(unconfirmed_txs))