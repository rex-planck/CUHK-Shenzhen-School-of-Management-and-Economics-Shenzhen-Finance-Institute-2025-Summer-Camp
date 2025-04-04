import hashlib
import base64
def hash_input(input_hex):
    # 将十六进制字符串转换为字节数组
    input_bytes = bytes.fromhex(input_hex)

    # 计算MD5摘要并转换为十六进制字符串
    md5_digest = hashlib.md5(input_bytes).hexdigest()
    # 计算MD5摘要并转换为Base64字符串
    md5_base64 = base64.b64encode(hashlib.md5(input_bytes).digest()).decode('utf-8')

    # 计算SHA256摘要并转换为十六进制字符串
    sha256_digest = hashlib.sha256(input_bytes).hexdigest()
    # 计算SHA256摘要并转换为Base64字符串
    sha256_base64 = base64.b64encode(hashlib.sha256(input_bytes).digest()).decode('utf-8')

    # 输出结果
    print("MD5 digest of the input:")
    print(md5_digest)
    print(md5_base64)
    print("SHA256 digest of the input:")
    print(sha256_digest)
    print(sha256_base64)


# 示例输入1
input1 = "d131dd02c5e6eec4693d9a0698aff95c2fcab58712467eab4004583eb8fb7f8955ad340609f4b30283e488832571415a085125e8f7cdc99fd91dbdf280373c5bd8823e3156348f5bae6dacd436c919c6dd53e2b487da03fd02396306d248cda0e99f33420f577ee8ce54b67080a80d1ec69821bcb6a8839396f9652b6ff72a70"
# 示例输入2
input2 = "d131dd02c5e6eec4693d9a0698aff95c2fcab50712467eab4004583eb8fb7f8955ad340609f4b30283e4888325f1415a085125e8f7cdc99fd91dbd7280373c5bd8823e3156348f5bae6dacd436c919c6dd53e23487da03fd02396306d248cda0e99f33420f577ee8ce54b67080280d1ec69821bcb6a8839396f965ab6ff72a70"

# 调用函数进行摘要计算
print("Example Output 1")
hash_input(input1)
print("\nExample Output 2")
hash_input(input2)
