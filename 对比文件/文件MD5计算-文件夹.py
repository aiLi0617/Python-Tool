import hashlib


def calculate_md5(file_path):
    """计算文件的MD5值"""
    md5_hash = hashlib.md5()

    with open(file_path, "rb") as f:
        # 分块读取文件，避免大文件内存溢出
        for chunk in iter(lambda: f.read(4096), b""):
            md5_hash.update(chunk)

    return md5_hash.hexdigest()

import os

def list_only_files(path):
    res = []
    """只列出文件，不包括文件夹"""
    for item in os.listdir(path):
        full_path = os.path.join(path, item)
        if os.path.isfile(full_path):
            print(f"文件: {item} :{calculate_md5(full_path)}")
            res.append(full_path)
    return res


# 使用示例
source = list_only_files("./source")
target = list_only_files("./target")

source_set = set()
target_set = set()

for i in source:
    source_set.add(calculate_md5(i))

for i in target:
    target_set.add(calculate_md5(i))

print(source_set)
print(target_set)
print(source_set - target_set)
print(target_set - source_set)
# # 使用示例
# file_path = "gxht.pdf"
# md5_value = calculate_md5(file_path)
# print(f"{file_path},文件MD5值: {md5_value}")

# ea616c55263173fb1cfa3b58bd099d2a/ea616c55263173fb1cfa3b58bd099d2a
# ea616c55263173fb1cfa3b58bd099d2a
# ea616c55263173fb1cfa3b58bd099d2a


# fec5731d704232086c0a55261619ac4c
