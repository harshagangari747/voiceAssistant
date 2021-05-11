from typing import runtime_checkable

def modularval(e,z) :
    d = 2
    while d < z:
        if ((d*e) % z)==1:
            return d
        d += 1
    return d
def encrypt(msg) :
    f= open('encryptedfile.log','a')
    p = 1049
    q = 8677
    n = p*q
    tf = (p-1)*(q-1)
    e = 14983
    d = modularval(e,tf)
    print(d)
    cipher = ""
    for c in msg :
        m = ord(c)
        cipher += str(pow(m,e,n))+" "
    f.write(msg+"\t"+cipher)
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

    

    
