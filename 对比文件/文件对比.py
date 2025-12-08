import hashlib
import os

# ==============================
# 配置区：只需修改这两个文件名 👇
# ==============================
FILE1 = "PRD.xlsx"
FILE2 = "pre.xlsx"
# ==============================

def calculate_md5(file_path, chunk_size=8192):
    if not os.path.isfile(file_path):
        raise FileNotFoundError(f"文件不存在: {file_path}")
    hash_md5 = hashlib.md5()
    with open(file_path, "rb") as f:
        for chunk in iter(lambda: f.read(chunk_size), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()

def main():
    # 自动在当前目录下拼接路径
    file1 = os.path.join(os.getcwd(), FILE1)
    file2 = os.path.join(os.getcwd(), FILE2)

    try:
        print(f"正在对比当前目录下的文件：")
        print(f"  - {FILE1}")
        print(f"  - {FILE2}\n")

        md5_1 = calculate_md5(file1)
        md5_2 = calculate_md5(file2)

        print("--- MD5 值 ---")
        print(f"{FILE1}: {md5_1}")
        print(f"{FILE2}: {md5_2}")
        print("--------------")

        if md5_1 == md5_2:
            print("✅ 内容相同")
        else:
            print("❌ 内容不同")

    except Exception as e:
        print(f"❌ 错误: {e}")

if __name__ == "__main__":
    main()