import os
import shutil
import secrets
import string
from pathlib import Path

# ==============================
# 🔧 配置区
# ==============================

PDF_DIR = "receipts"  # PDF 所在目录

# 映射：原始文件名（必须存在于 PDF_DIR 中） => BANK_SERIAL_NO
FILE_TO_SERIAL = {
    # "old_name.pdf": "1453062851479605249",
    "b18db049d5a34a7d94ff1cc304cfa0d3.pdf": "1457375266916667392",
    "2e1cf3401b6f41aa8e1993f6a4a910f4.pdf": "1457375267671642112",
    "cac35e591fb243baa1e1096766ada0fe.pdf": "1457335001568907264",
    "de5ae7c6d54c49f7ae90e3a534ab7a61.pdf": "1455612150541324288",
    "efed4e0769aa43d5b176d70112033f19.pdf": "1455612151375990784",
    "1a09ea5eace5471ea94b14077515ecb2.pdf": "1455612152135159808",
    "e5ec21dfef8a41c5b6c01507741d1d85.pdf": "1455612152923688960",
    "7e24ffca70c84318bcda190ea6da7ae2.pdf": "1455612153708023808",
}

# ==============================
# ⚙️ 全局参数
# ==============================
BUCKET_NAME = "broker-cloud-prd-server"
PATH_PREFIX = "rgst-bank-receipt/202512/"
URL_BASE = f"https://{BUCKET_NAME}.obs.cn-south-1.myhuaweicloud.com:443/{PATH_PREFIX}"
QUERY_STRING = "AccessKeyId=SGHTWJV6RZGRUYH706N9&Expires=1766509248&Signature=ekvKW2UznDzMQ1JRE5rM1bI4gGI%3D"
CREATE_TIME = "2025-12-24 00:00:48"
MIME_TYPE = "application/pdf"

# ==============================
# 🛠 工具函数
# ==============================
def random_string(length=10):
    chars = string.ascii_letters + string.digits
    return ''.join(secrets.choice(chars) for _ in range(length))

# ==============================
# 🚀 主逻辑
# ==============================
def main():
    pdf_dir = Path(PDF_DIR)
    if not pdf_dir.is_dir():
        print(f"❌ PDF 目录不存在: {pdf_dir.absolute()}")
        return

    if not FILE_TO_SERIAL:
        print("❌ FILE_TO_SERIAL 为空，请配置映射。")
        return

    valid_items = []
    for orig_name, serial_no in FILE_TO_SERIAL.items():
        orig_path = pdf_dir / orig_name
        if not orig_path.is_file():
            print(f"⚠️ 警告：原始文件不存在 → {orig_path}")
            continue
        if orig_path.suffix.lower() != '.pdf':
            print(f"⚠️ 警告：非 PDF 文件 → {orig_path}")
            continue
        valid_items.append((orig_path, serial_no))

    if not valid_items:
        print("❌ 没有有效文件可处理。")
        return

    sql_lines = []
    sql_lines.append("-- 初始化最大ID和桶名")
    sql_lines.append("SET @ID = (SELECT MAX(id) FROM broker4infra.file_attachment);")
    sql_lines.append(f'SET @BUCKET_NAME = "{BUCKET_NAME}";')
    sql_lines.append("")

    for idx, (orig_file, bank_serial_no) in enumerate(valid_items, start=1):
        print(f"🔄 处理 [{idx}/{len(valid_items)}]: {orig_file.name}")

        # 生成两个随机文件名
        new_name_1 = random_string(10) + ".pdf"
        new_name_2 = random_string(10) + ".pdf"

        new_path_1 = pdf_dir / new_name_1
        new_path_2 = pdf_dir / new_name_2

        # 步骤1: 将原始文件重命名为 new_name_1（相当于 ownership=1 的文件）
        shutil.move(orig_file, new_path_1)
        print(f"   ➤ 原文件重命名为: {new_name_1}")

        # 步骤2: 从 new_path_1 复制出 new_name_2（ownership=0 的文件）
        shutil.copy2(new_path_1, new_path_2)
        print(f"   ➤ 复制副本为:     {new_name_2}")

        file_size = new_path_1.stat().st_size  # 两个文件大小相同

        var_1 = f"@FILE_{idx}_1"
        var_2 = f"@FILE_{idx}_2"

        # --- 第一条：ownership = 1 ---
        sql_lines.append(f"-- 原始文件 {orig_file.name} → {new_name_1} | ownership = 1")
        sql_lines.append(f"SET {var_1} = (@ID := @ID + 1);")
        sql_lines.append(f"SET @FILE_NAME = '{new_name_1}';")
        sql_lines.append(f"SET @BANK_SERIAL_NO = '{bank_serial_no}';")
        sql_lines.append(
            f"INSERT INTO `broker4infra`.`file_attachment` "
            f"(`id`, `name`, `path`, `url`, `type`, `size`, `creator`, `create_time`, `updater`, `update_time`, `deleted`, `status`, `bucket_name`) "
            f"VALUES ("
            f"{var_1}, "
            f"@FILE_NAME, "
            f"CONCAT('{PATH_PREFIX}', @FILE_NAME), "
            f"CONCAT('{URL_BASE}', @FILE_NAME, '?{QUERY_STRING}'), "
            f"'{MIME_TYPE}', {file_size}, NULL, '{CREATE_TIME}', NULL, '{CREATE_TIME}', b'0', 0, @BUCKET_NAME"
            f");"
        )
        sql_lines.append(
            f"UPDATE broker4settlement.transaction_flow_detail "
            f"SET receipt_file_id = {var_1} "
            f"WHERE bank_serial_no = @BANK_SERIAL_NO AND order_ownership = 1;"
        )
        sql_lines.append("")

        # --- 第二条：ownership = 0 ---
        sql_lines.append(f"-- 副本 {new_name_2} | ownership = 0")
        sql_lines.append(f"SET {var_2} = (@ID := @ID + 1);")
        sql_lines.append(f"SET @FILE_NAME = '{new_name_2}';")
        sql_lines.append(f"SET @BANK_SERIAL_NO = '{bank_serial_no}';")
        sql_lines.append(
            f"INSERT INTO `broker4infra`.`file_attachment` "
            f"(`id`, `name`, `path`, `url`, `type`, `size`, `creator`, `create_time`, `updater`, `update_time`, `deleted`, `status`, `bucket_name`) "
            f"VALUES ("
            f"{var_2}, "
            f"@FILE_NAME, "
            f"CONCAT('{PATH_PREFIX}', @FILE_NAME), "
            f"CONCAT('{URL_BASE}', @FILE_NAME, '?{QUERY_STRING}'), "
            f"'{MIME_TYPE}', {file_size}, NULL, '{CREATE_TIME}', NULL, '{CREATE_TIME}', b'0', 0, @BUCKET_NAME"
            f");"
        )
        sql_lines.append(
            f"UPDATE broker4settlement.transaction_flow_detail "
            f"SET receipt_file_id = {var_2} "
            f"WHERE bank_serial_no = @BANK_SERIAL_NO AND order_ownership = 0;"
        )
        sql_lines.append("")

    # 保存 SQL
    output_sql = "generated_files.sql"
    with open(output_sql, "w", encoding="utf-8") as f:
        f.write("\n".join(sql_lines))

    print(f"\n✅ 成功处理 {len(valid_items)} 个原始文件。")
    print(f"📁 原始文件已被重命名，所有新文件位于: {pdf_dir.absolute()}")
    print(f"📄 SQL 脚本已保存至: {output_sql}")

if __name__ == "__main__":
    main()