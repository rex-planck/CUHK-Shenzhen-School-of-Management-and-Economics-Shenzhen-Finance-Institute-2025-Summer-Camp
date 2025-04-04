import hashlib
def generate_scrypt_hash(password, salt_hex):
    # 将密码转换为字节数组，使用utf-8编码
    password_bytes = password.encode('utf-8')

    # 将盐值转换为字节数组，使用fromhex()方法将十六进制字符串转换为字节数组
    salt_bytes = bytes.fromhex(salt_hex)

    # 使用scrypt方法计算哈希值，参数为n=4, r=8, p=16
    # n = 4, r = 8, p = 16 为scrypt算法的参数
    # 输出是一个字节数组
    scrypt_hash = hashlib.scrypt(password_bytes, salt=salt_bytes, n=4, r=8, p=16, dklen=64)

    # 返回结果的十六进制字符串表示
    return scrypt_hash.hex()


# 示例输入
password = "Thi$ i$ my passw0rd!"
salt_hex = "477d15cb740ca1da08f6d851361b3c80"

# 调用生成scrypt哈希值的函数
output_hash = generate_scrypt_hash(password, salt_hex)

# 输出结果
print("Example Output:")
print(output_hash)
