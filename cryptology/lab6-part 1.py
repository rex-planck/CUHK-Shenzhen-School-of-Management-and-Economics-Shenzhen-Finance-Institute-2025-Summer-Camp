import random
from sympy import isprime, mod_inverse

def generate_prime(bits):
    while True:
        prime_candidate = random.getrandbits(bits)
        if isprime(prime_candidate):
            return prime_candidate

def keygen(bits):
    p = generate_prime(bits // 2)
    q = generate_prime(bits // 2)
    N = p * q
    phi = (p - 1) * (q - 1)
    e = random.randint(2, phi - 1)
    while isprime(e) or e == p or e == q or mod_inverse(e, phi) == 0:
        e = random.randint(2, phi - 1)
    d = mod_inverse(e, phi)
    return (N, e), (N, d)

def sign(message, priv_key):
    N, d = priv_key
    return pow(message, d, N)

def verify(message, signature, pub_key):
    N, e = pub_key
    return message == pow(signature, e, N)

# 生成密钥对
pub_key, priv_key = keygen(1024)

print(f"Public key: N={pub_key[0]} e={pub_key[1]}")
print(f"Private key: N={priv_key[0]} d={priv_key[1]}")

# 读取消息并生成签名
m = int(input("Enter message m (as a decimal string): "))
signature = sign(m, priv_key)
print(f"Signature: s={signature}")

# 验证签名
is_valid = verify(m, signature, pub_key)
print("Verify s of m:", "valid" if is_valid else "invalid")

# 伪造消息和签名进行验证
fake_message = random.randint(1, pub_key[0] - 1)
is_valid_fake_message = verify(fake_message, signature, pub_key)
print("Verify s of m':", "valid" if is_valid_fake_message else "invalid")

fake_signature = random.randint(1, pub_key[0] - 1)
is_valid_fake_signature = verify(m, fake_signature, pub_key)
print("Verify s' of m:", "valid" if is_valid_fake_signature else "invalid")
