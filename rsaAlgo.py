from typing import runtime_checkable
from datetime import datetime as dt

def modularval(e,z) :
    d = 2
    while d < z:
        if ((d*e) % z)==1:
            return d
        d += 1
    return d
def encrypt(msg) :
    f= open(r'C:\\Users\\user\\OneDrive\\Desktop\\Final Project\\Encryption\\rsaAlgo\\encryptedfile.log','a')
    p = 1049
    q = 8677
    n = p*q
    tf = (p-1)*(q-1)
    e = 14983
    d = modularval(e,tf)
    cipher = ""
    for c in msg :
        m = ord(c)
        cipher += str(pow(m,e,n))+" "
    date = dt.now().strftime("%Y_%m_%d-%I:%M:%S_%p")
    f.write(msg+"---"+cipher+"--->"+date+"\n\n")
    # decrypt(d,n,cipher)
    # return cipher

# def decrypt(d,n,enc) :
#     msg = ""
#     p = enc.split()
#     for i in p :
#         if i :
#             c = int(i)
#             msg += chr(pow(c,d,n))
#     print(msg)

    

    
