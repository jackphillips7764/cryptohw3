import math


#define vars:
p = 499
q = 547
a = -57
b = 52
n = p*q

mes = int('10011100000100001100', 2)

print bin(mes)


def encrypt(mes):
    X0 = 159201
    k = int(math.floor(math.log(p*q,2)))
    h = int(math.floor(math.log(k,2)))
    blocks = len(bin(mes))/h
    x = X0
    msg = 0
    for i in range(blocks - 1 , -1, -1):
        mask = 1 << h
        mask = mask - 1
        x = pow(x, 2, n)
        number = mes >> (h * i)
        mi = number & mask
        pi = x & mask
        ci = pi ^ mi
        msg <<= h
        msg |= ci
    x = pow(x, 2, n)
    return msg, x

#cool func
def decrypt(cipher, x, t):
    k = int(math.floor(math.log(p*q,2)))
    h = int(math.floor(math.log(k,2)))
    d1 = pow(((p+1)/4), t+1, p-1)
    d2 = pow(((q+1)/4), t+1, q-1)
    u = pow(x, d1, p)
    v = pow(x, d2, q)
    x0 = (v*a*p + u*b*q) % n
    msg = 0
    x = x0
    for i in range(t - 1, -1, -1):
        mask = 1 << h
        mask = mask - 1
        x = pow(x, 2, n)
        number = cipher >> (h * i)
        ci = number & mask
        pi = x & mask
        mi = pi ^ ci
        msg <<= h
        msg |= mi
    return msg



cipher, x = encrypt(mes)
print len(bin(cipher))
print "Cipher Text`: (%s, %d)"%(bin(cipher)[2::],x)
msg = decrypt(cipher, x, 5)
print "Decrypted Text`: (%s)"%(bin(msg)[2::])

print "are equal?"
print msg == mes
