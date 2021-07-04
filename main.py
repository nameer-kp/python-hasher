import hashlib
from hash_methods import *
def main():
    string=input("Enter String To Hash: ")
    hash_algorithm=input("Select Hashing Algorithm: \n1.MD5 \n2.SHA256 \n3.SHA1\n")
    is_salt_needed=input("Do You Want To Use Salting and Iterations (y/n)\n")
    if(is_salt_needed in ("y","Y")):
        salt=input("Enter Salt: ")
        try:
            iterations=int(input("Enter No.Of Iterations: "))
            if(hash_algorithm=='1'):
                print("MD5 Hash For "+string+" Is "+salted_hash('md5',string,salt,iterations))
            elif(hash_algorithm=='2'):
                print("SHA256 Hash For "+string+" Is "+salted_hash('sha256',string,salt,iterations))
            elif(hash_algorithm=='3'):
                print("SHA1 Hash For "+string+" Is "+salted_hash('sha1',string,salt,iterations))
        except:
            print("enter valid iteration")
    elif(is_salt_needed in ("n","N")):
        if(hash_algorithm=='1'):
                print("MD5 Hash For "+string+" Is "+md5_hasher(string))
        elif(hash_algorithm=='2'):
                print("SHA256 Hash For "+string+" Is "+sha256_hasher(string))
        elif(hash_algorithm=='3'):
                print("SHA1 Hash For "+string+" Is "+sha1_hasher(string))
    else:
        print("Choose Valid Option")


    repeat=input("Do You Want To Repeat (y/n)\n")
    if(repeat in ("Y",'y')):
        main()
    else:
        print("BYE")
main()
