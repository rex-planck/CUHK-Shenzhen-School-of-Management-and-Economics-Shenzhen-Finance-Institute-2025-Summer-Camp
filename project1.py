from Crypto.Cipher import DES3
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes

# 生成24字节的密钥
key = DES3.adjust_key_parity(get_random_bytes(24))

# 创建3DES加密器
cipher_encrypt = DES3.new(key, DES3.MODE_ECB)

# 明文
plaintext = b'8787878787878787'

# 填充明文
padded_plaintext = pad(plaintext, DES3.block_size)

# 加密
ciphertext = cipher_encrypt.encrypt(padded_plaintext)

print(f'加密后的密文: {ciphertext.hex()}')

# 创建3DES解密器
cipher_decrypt = DES3.new(key, DES3.MODE_ECB)

# 解密
decrypted_padded_text = cipher_decrypt.decrypt(ciphertext)

# 去除填充
decrypted_text = unpad(decrypted_padded_text, DES3.block_size)

print(f'解密后的明文: {decrypted_text.hex()}')