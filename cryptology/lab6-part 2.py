
import random
from sympy import isprime, mod_inverse, primitive_root

def generate_prime(bits):
    while True:
        prime_candidate = random.getrandbits(bits)
        if isprime(prime_candidate):
            return prime_candidate

def keygen(bits):
    p = generate_prime(bits)
    alpha = primitive_root(p)
    a = random.randint(2, p-2)
    beta = pow(alpha, a, p)
    return (p, alpha, beta), (p, alpha, a)

def sign(message, priv_key):
    p, alpha, a = priv_key
    while True:
        k = random.randint(2, p-2)
        if isprime(k):
            if mod_inverse(k, p-1) is not None:
                break
    r = pow(alpha, k, p)
    k_inv = mod_inverse(k, p-1)
    s = ((message - a * r) * k_inv) % (p - 1)
    return r, s

def verify(message, signature, pub_key):
    p, alpha, beta = pub_key
    r, s = signature
    return pow(beta, r, p) * pow(r, s, p) % p == pow(alpha, message, p)

# 生成密钥对
pub_key, priv_key = keygen(512)

print(f"Public key: p={pub_key[0]} alpha={pub_key[1]} beta={pub_key[2]}")
print(f"Private key: p={priv_key[0]} alpha={priv_key[1]} a={priv_key[2]}")

# 读取消息并生成签名
m = int(input("Enter message m (as a decimal string): "))
signature = sign(m, priv_key)
print(f"Signature: r={signature[0]} s={signature[1]}")

# 验证签名
is_valid = verify(m, signature, pub_key)
print("Verify r, s of m:", "valid" if is_valid else "invalid")

# 伪造消息和签名进行验证
fake_message = random.randint(1, pub_key[0] - 1)
is_valid_fake_message = verify(fake_message, signature, pub_key)
print("Verify r, s of m':", "valid" if is_valid_fake_message else "invalid")

fake_signature = (random.randint(1, pub_key[0] - 1), random.randint(1, pub_key[0] - 1))
is_valid_fake_signature = verify(m, fake_signature, pub_key)
print("Verify r', s' of m:", "valid" if is_valid_fake_signature else "invalid")
