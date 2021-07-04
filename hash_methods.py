import hashlib
def md5_hasher(string):
    h=hashlib.md5(string.encode('utf-8'))
    hash=h.hexdigest()
    return hash
def sha256_hasher(string):
    h=hashlib.sha256(string.encode('utf-8'))
    hash=h.hexdigest()
    return hash

def sha1_hasher(string):
    h=hashlib.sha1(string.encode('utf-8'))
    hash=h.hexdigest()
    return hash
def salted_hash(algo,string,salt,iterations):
    h=hashlib.pbkdf2_hmac(algo,string.encode('utf-8'),salt.encode('utf-8'),iterations)
    return h.hex()
