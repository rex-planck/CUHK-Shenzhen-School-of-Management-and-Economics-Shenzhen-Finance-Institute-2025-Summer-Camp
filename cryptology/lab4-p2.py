import random
from sympy import isprime, primitive_root

def generate_large_prime(bits=512):
    while True:
        p = random.getrandbits(bits)
        if isprime(p):
            return p

def keygen():
    p = generate_large_prime()
    alpha = primitive_root(p)
    a = random.randint(2, p-2)
    beta = pow(alpha, a, p)
    return (p, alpha, a), (p, alpha, beta)

private_key, public_key = keygen()
print("私钥:", private_key)
print("公钥:", public_key)

def encrypt(m, public_key):
    p, alpha, beta = public_key
    k = random.randint(2, p-2)
    r = pow(alpha, k, p)
    t = (m * pow(beta, k, p)) % p
    return (r, t), k

m = 4137696876930090267522398697653550193405311689664069574322834683213199126531348263326633721504049779673544721298253021191958429503842792929508773630980912
encrypted_message, k = encrypt(m, public_key)
print("加密后的消息:", encrypted_message)
print("密钥 k:", k)

def decrypt(ciphertext, private_key):
    p, alpha, a = private_key
    r, t = ciphertext
    s = pow(r, a, p)
    m_prime = (t * pow(s, p-2, p)) % p
    return m_prime


decrypted_message = decrypt(encrypted_message, private_key)
print("解密后的消息:", decrypted_message)