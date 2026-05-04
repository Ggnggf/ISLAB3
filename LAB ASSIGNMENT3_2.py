# Curve params
a, p = 2, 97
O = (None, None)

def inv(x): return pow(x, -1, p)

def add(P, Q):
    if P == O: return Q
    if Q == O: return P
    x1,y1 = P; x2,y2 = Q

    if P == Q:
        m = (3*x1*x1 + a) * inv(2*y1) % p
    else:
        if x1 == x2: return O
        m = (y2-y1) * inv(x2-x1) % p

    x = (m*m - x1 - x2) % p
    y = (m*(x1 - x) - y1) % p
    return (x,y)

def mul(k, P):
    R = O
    while k:
        if k & 1: R = add(R, P)
        P = add(P, P)
        k >>= 1
    return R

# Keys
G = (3,6)
priv = 5
pub = mul(priv, G)

# Encrypt
msg = 10
k = 7
C1 = mul(k, G)
C2 = (msg + mul(k, pub)[0]) % p

# Decrypt
dec = (C2 - mul(priv, C1)[0]) % p

print("Public:", pub)
print("Encrypted:", C1, C2)
print("Decrypted:", dec)