from hashlib import sha256 

def get_hash(texto):
    return sha256(texto.encode("ascii")).hexdigest()

def mine(num_block, transaction, hash_old, num_zero):
    nonce = 0
    while True:
        texto_hash = str(num_block) + transaction + hash_old + str(nonce)
        hash = get_hash(texto_hash)
        if(hash.startswith("0"*num_zero)):
            return nonce, hash
        nonce += 1

hash_old = ""
num_zero = 1
num_block = 1
transaction = '''
'''