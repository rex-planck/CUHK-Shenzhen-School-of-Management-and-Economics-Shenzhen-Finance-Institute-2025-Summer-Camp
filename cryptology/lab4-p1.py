import random
from sympy import isprime, mod_inverse


def generate_prime(bits):
    while True:
        p = random.getrandbits(bits)
        if isprime(p):
            return p


def KeyGen():
    p = generate_prime(512)
    q = generate_prime(512)
    N = p * q
    phi = (p - 1) * (q - 1)

    e = 65537  # 常用的公钥指数
    d = mod_inverse(e, phi)

    return (N, e), (N, d)


public_key, private_key = KeyGen()
print("Public Key:", public_key)
print("Private Key:", private_key)

def Encrypt(m, public_key):
    N, e = public_key
    if m < 0 or m >= N:
        raise ValueError("Invalid message")
    c = pow(m, e, N)
    return c

message = 3486284410881543027893588611481420466124210580619613445126242119795866173728846
5541172280522822644267285105893266043422314800759306377373320298160258654603531
1597026639261601072852231456662396738338177863450654319767641395509047260399024
50456522584204556470321705267433321819673919640632299889369457498214445

ciphertext = Encrypt(message, public_key)
print("Encrypted Message:", ciphertext)


def Decrypt(c, private_key):
    N, d = private_key
    m_prime = pow(c, d, N)
    return m_prime

decrypted_message = Decrypt(ciphertext, private_key)
print("Decrypted Message:", decrypted_message)

if message == decrypted_message:
    print("secure")
else:
    print("insecure")






