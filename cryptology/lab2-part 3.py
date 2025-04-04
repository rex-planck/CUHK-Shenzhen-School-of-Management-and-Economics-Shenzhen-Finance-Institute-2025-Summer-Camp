import base64
def vigenere_cipher_bytes(plaintext_hex, key_hex):
    # 将十六进制字符串解码为字节
    plaintext_bytes = bytes.fromhex(plaintext_hex)
    key_bytes = bytes.fromhex(key_hex)
    # 扩展密钥以匹配明文长度
    extended_key = (key_bytes * (len(plaintext_bytes) // len(key_bytes) + 1))[:len(plaintext_bytes)]
    # 执行Vigenère加密
    ciphertext_bytes = bytes([p ^ k for p, k in zip(plaintext_bytes, extended_key)])
    # 将密文字节转换为十六进制字符串
    ciphertext_hex = ciphertext_bytes.hex()
    # 将密文字节转换为Base64字符串
    ciphertext_base64 = base64.b64encode(ciphertext_bytes).decode()
    return ciphertext_hex, ciphertext_base64
# 读取输入
plaintext_hex = input("输入明文的十六进制字符串: ")
key_hex = input("输入密钥的十六进制字符串: ")
# 执行加密
ciphertext_hex, ciphertext_base64 = vigenere_cipher_bytes(plaintext_hex, key_hex)
# 输出结果
print("密文的十六进制字符串: ", ciphertext_hex)
print("密文的Base64字符串: ", ciphertext_base64)
