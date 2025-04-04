from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import base64

def encrypt(plaintext, key, iv):
    cipher = AES.new(key, AES.MODE_CBC, iv)
    padded_data = pad(plaintext.encode('utf-8'), AES.block_size)
    encrypted = cipher.encrypt(padded_data)
    return base64.b64encode(encrypted).decode('utf-8')

def decrypt(ciphertext, key, iv):
    cipher = AES.new(key, AES.MODE_CBC, iv)
    encrypted_data = base64.b64decode(ciphertext)
    decrypted_data = unpad(cipher.decrypt(encrypted_data), AES.block_size)
    return decrypted_data.decode('utf-8')

# 输入数据
plaintext = "I don't like deadbeef. 你呢？"
key = base64.b64decode("1U07ZnmwcT7KtScS2hAZV+aZ1Gk95HPK1EqcXT6rqoU=")
iv = base64.b64decode("6GXIzJOGD/76WkTtgmaDYQ==")

# 加密
encrypted_text = encrypt(plaintext, key, iv)
print(f"Encrypted: {encrypted_text}")

# 解密
decrypted_text = decrypt(encrypted_text, key, iv)
print(f"Decrypted: {decrypted_text}")