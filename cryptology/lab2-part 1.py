#Part 1
def vigenere_encrypt(plaintext, key):
    #输入明文字符串和密匙
    ciphertext = []
    #初始化一个空列表用于存储加密后的字符
    for p, k in zip(plaintext, key):
        #zip函数使得明文和密钥的字符一一对应
        encrypted_char = chr(((ord(p) - ord('A') + ord(k) - ord('A')) % 26) + ord('A'))
        ciphertext.append(encrypted_char)
    return ''.join(ciphertext)

def vigenere_decrypt(ciphertext, key):
    decrypted_text = []
    for c, k in zip(ciphertext, key):
        decrypted_char = chr(((ord(c) - ord('A') - (ord(k) - ord('A'))) % 26) + ord('A'))
        decrypted_text.append(decrypted_char)
    return ''.join(decrypted_text)

plaintext = input("请输入明文: ")
key = input("请输入密钥: ")

ciphertext = vigenere_encrypt(plaintext, key)
print("密文:", ciphertext)

decrypted_text = vigenere_decrypt(ciphertext, key)
print("解密后的明文:", decrypted_text)




