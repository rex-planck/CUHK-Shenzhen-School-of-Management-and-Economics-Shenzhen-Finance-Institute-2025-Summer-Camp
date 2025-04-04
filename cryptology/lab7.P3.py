import hashlib
import os
import base64
# 生成盐值并通过scrypt哈希算法加密密码
def hash_password(password):
    # 生成一个新的盐值
    salt = os.urandom(16)  # 16字节盐值
    # 将密码转换为字节数组并使用scrypt算法生成哈希值
    password_bytes = password.encode('utf-8')
    hashed_password = hashlib.scrypt(password_bytes, salt=salt, n=16384, r=8, p=1, dklen=64)
    # 将盐值和哈希值一起返回，存储时以base64编码格式存储
    return base64.b64encode(salt + hashed_password).decode('utf-8')


# 验证输入的密码是否与存储的哈希值匹配
def verify_password(stored_hash, input_password):
    # 解码存储的哈希值
    stored_hash_bytes = base64.b64decode(stored_hash)
    # 从存储的哈希中提取盐值和哈希值
    salt = stored_hash_bytes[:16]  # 盐值的长度为16字节
    stored_password_hash = stored_hash_bytes[16:]  # 后面的部分是密码的哈希值

    # 对输入密码进行相同的加密过程
    input_password_bytes = input_password.encode('utf-8')
    input_password_hash = hashlib.scrypt(input_password_bytes, salt=salt, n=16384, r=8, p=1, dklen=64)

    # 比较计算出的哈希值和存储的哈希值是否相同
    return input_password_hash == stored_password_hash


# 用户注册模拟
def register_user():
    password = input("请输入密码进行注册: ")
    # 将密码哈希化存储
    stored_hash = hash_password(password)
    print(f"注册成功！您的密码已加密存储。")

    return stored_hash


# 用户登录模拟
def login_user(stored_hash):
    input_password = input("请输入密码进行登录: ")
    # 验证输入密码
    if verify_password(stored_hash, input_password):
        print("登录成功！")
    else:
        print("密码错误，登录失败。")


# 主程序
def main():
    # 模拟注册过程
    stored_hash = register_user()

    # 模拟登录过程
    login_user(stored_hash)


if __name__ == "__main__":
    main()
