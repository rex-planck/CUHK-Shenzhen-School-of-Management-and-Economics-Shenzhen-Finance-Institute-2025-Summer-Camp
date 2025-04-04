from Crypto.Cipher import DES3
from binascii import unhexlify, hexlify

# 输入数据
plaintext_hex = "8787878787878787"
key1_hex = "133457799bbcdff1"
key2_hex = "0e329232=ea6d0d73"
key3_hex = "133457799bbcdff1"

# 转换为字节
plaintext = unhexlify(plaintext_hex)
key1 = unhexlify(key1_hex)
key2 = unhexlify(key2_hex)
key3 = unhexlify(key3_hex)

# 3DES加密
cipher = DES3.new(key1 + key2 + key3, DES3.MODE_ECB)
ciphertext = cipher.encrypt(plaintext)

# 输出加密后的密文
print("Ciphertext:", hexlify(ciphertext).decode())

# 3DES解密
decipher = DES3.new(key1 + key2 + key3, DES3.MODE_ECB)
decrypted_plaintext = decipher.decrypt(ciphertext)

# 输出解密后的明文
print("Decrypted Plaintext:", hexlify(decrypted_plaintext).decode())