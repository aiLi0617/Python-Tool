import os
import json
import pandas as pd


def process_json_file(file_path):
    """
    读取单个 JSON 文件，提取 ntdmabalz 数据并转为 DataFrame
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)

        # 提取 ntdmabalz 列表
        records = data.get("response", {}).get("body", {}).get("ntdmabalz", [])

        if not records:
            print(f"⚠️ 警告: {file_path} 中未找到有效数据 (ntdmabalz 为空)")
            return None

        # 转为 DataFrame
        df = pd.DataFrame(records)
        return df

    except Exception as e:
        print(f"❌ 错误: 无法处理文件 {file_path} - {e}")
        return None


def main():
    # 👇 修改为你存放 JSON 文件的文件夹路径
    input_folder = "json_files"  # 假设你的 JSON 文件都在这个文件夹里
    output_excel = "output_accounts.xlsx"

    # 创建输出文件夹（如果不存在）
    os.makedirs(input_folder, exist_ok=True)

    # 获取所有 .json 文件
    json_files = [f for f in os.listdir(input_folder) if f.lower().endswith('.json')]

    if not json_files:
        print("❌ 没有找到任何 .json 文件，请检查路径。")
        return

    # 创建 Excel 写入器
    with pd.ExcelWriter(output_excel, engine='openpyxl') as writer:
        for filename in json_files:
            file_path = os.path.join(input_folder, filename)
            df = process_json_file(file_path)

            if df is not None:
                # 工作表名称不能超过 31 个字符，且不能包含特殊字符
                sheet_name = os.path.splitext(filename)[0][:31]
                df.to_excel(writer, sheet_name=sheet_name, index=False)
                print(f"✅ 已处理: {filename} -> Sheet: {sheet_name}")
            else:
                print(f"⏭️ 跳过: {filename}（无有效数据或解析失败）")

    print(f"\n🎉 所有文件已成功导出到: {os.path.abspath(output_excel)}")


if __name__ == "__main__":
    main()