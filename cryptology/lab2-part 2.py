#Part 2
def columnar_transposition(column_count, key, plaintext):
    # 将明文转换为大写并去除空格
    plaintext = plaintext.replace(" ", "").upper()

    # 计算每列的长度
    col_length = len(plaintext) // column_count
    if len(plaintext) % column_count != 0:
        col_length += 1

    # 创建一个二维列表来存储列
    columns = [''] * column_count
    for i in range(len(plaintext)):
        columns[i % column_count] += plaintext[i]

    # 根据密钥重新排列列
    ciphertext = ''
    for k in key:
        ciphertext += columns[k - 1]

    return ciphertext


# 读取输入
column_count = int(input("输入列数: "))
key = list(map(int, input("输入密钥（以空格分隔）: ").split()))
plaintext = input("输入明文: ")

# 执行列式换位加密
ciphertext = columnar_transposition(column_count, key, plaintext)
print("密文: ", ciphertext)
