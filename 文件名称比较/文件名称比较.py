import os

# 要排除的文件名（可扩展为多个）
EXCLUDE_FILES = {"文件名称比较.py"}  # 使用 set 提升查找效率

def get_all_files_recursive(exclude_set=None):
    """递归获取当前目录及子目录中所有文件的文件名，排除指定文件"""
    if exclude_set is None:
        exclude_set = set()
    all_files = set()
    for root, dirs, files in os.walk('.'):
        for file in files:
            if file not in exclude_set:
                all_files.add(file)
    return all_files


def compare_files_by_name(provided_paths, exclude_set=None):
    if exclude_set is None:
        exclude_set = set()

    current_filenames = get_all_files_recursive(exclude_set)
    provided_filenames = set(os.path.basename(p) for p in provided_paths)

    only_in_current = current_filenames - provided_filenames
    only_in_provided = provided_filenames - current_filenames
    in_both = current_filenames & provided_filenames

    # 打印当前文件列表 + 数量
    print(f"📁 当前目录及子目录中的所有文件名（已排除指定文件）：共 {len(current_filenames)} 个")
    for f in sorted(current_filenames):
        print(f"  {f}")

    print(f"\n📄 你提供的文件名：共 {len(provided_filenames)} 个")
    for f in sorted(provided_filenames):
        print(f"  {f}")

    print(f"\n❌ 仅在你提供的列表中（本地缺失）的文件名：共 {len(only_in_provided)} 个")
    if only_in_provided:
        for f in sorted(only_in_provided):
            print(f"  {f}")
    else:
        print("  （无）")

    print(f"\n✅ 两者都有的文件名：共 {len(in_both)} 个")
    if in_both:
        for f in sorted(in_both):
            print(f"  {f}")
    else:
        print("  （无）")

    print(f"\n⚠️ 仅在当前目录（含子目录）中存在的文件名：共 {len(only_in_current)} 个")
    if only_in_current:
        for f in sorted(only_in_current):
            print(f"  {f}")
    else:
        print("  （无）")

    # ---- 最后统一输出数量汇总 ----
    print("\n" + "="*50)
    print("📊 差异汇总统计：")
    print(f"  📁 当前本地文件总数（已排除）：{len(current_filenames)}")
    print(f"  📄 你提供的文件总数：       {len(provided_filenames)}")
    print(f"  ✅ 两者都有的文件数：        {len(in_both)}")
    print(f"  ❌ 你提供但本地缺失的文件数：{len(only_in_provided)}")
    print(f"  ⚠️ 本地有但你未提供的文件数：{len(only_in_current)}")
    print("="*50)

# ===== 使用示例 =====
if __name__ == "__main__":
    # 当前目录及子目录中的所有文件名
    # 替换为你自己的文件路径列表
    my_file_paths = [
        "agreement/product202510/8so3kIQk2W.png",
        "agreement/product202510/xYYuXSYjXw.png",
        "agreement/product202510/jsMUanGmA9.png",
        "agreement/product202510/JDiYrdfRBy.png",
        "agreement/product202510/scB0SP4lse.png",
        "agreement/product202510/LwzttFjDNd.png",
        "agreement/product202510/Ov0059wWTv.png",
        "agreement/product202510/AEK6Hn1nrz.png",
        "agreement/product202510/mPNLdiJOEh.png",
        "agreement/product202510/q2bIO1Y6Js.png",
        "agreement/product202510/tHbaXUEcGn.png",
        "agreement/product202510/7eduDSk12a.png",
        "agreement/product202510/F4UeFPpAVS.png",
        "agreement/product202510/oob1TvNGfu.png",
        "agreement/product202510/8rbWQoH99C.png",
        "agreement/product202510/WbPS1x6srQ.png",
        "agreement/product202510/xv4BEXUcdR.png",
        "agreement/product202510/2Ls4mIz1WW.png",
        "agreement/product202510/hJNl1DKht4.png",
        "agreement/product202510/GehR3U4IpO.png",
        "agreement/product202510/TOye88ODob.png",
        "agreement/product202510/vn89kMvz0b.png",
        "agreement/product202510/mqZnJ4RntP.png",
        "agreement/product202510/rtJ5l0X7RQ.png",
        "agreement/product202510/vJJjvKmyjc.png",
        "agreement/product202510/HuIYfQQBU6.png",
        "agreement/product202510/fkCU0B07hU.png",
        "agreement/product202510/xzDjiHjii9.png",
        "agreement/product202510/POCicuUqrd.png",
        "agreement/product202510/d5oCLn1kVC.png",
        "agreement/product202510/q8Q2AcX5o9.png",
        "agreement/product202510/c1si9RG8lE.png",
        "agreement/product202510/yVacfpZGZh.png",
        "agreement/product202510/a7hNv5BcTD.png",
        "agreement/product202510/gkX1hwNr00.png",
        "agreement/product202510/4SaIkbYHky.png",
        "agreement/product202510/78L8VbqJsZ.png",
        "agreement/product202510/FMzknELvEc.png",
        "agreement/product202510/IHBBQzacpi.png",
        "agreement/product202510/HIEcU53tjV.png",
        "agreement/product202510/RYxddLmKdS.png",
        "agreement/product202510/PBTX9jOwi5.png",
        "agreement/product202510/XplnXnvTuk.png",
        "agreement/product202510/f1QH4PRf6r.png",
        "agreement/product202510/lwmeELrAtn.png",
        "agreement/product202510/3JG9FTptT1.png",
        "agreement/product202510/tP4YBQcQbI.png",
        "agreement/product202510/RB9IoE9aGt.png",
        "agreement/product202510/1gYGlZ9GTr.png",
        "agreement/product202510/W5Zk1ReQIu.png",
        "agreement/product202510/2QJ42ezHPF.png",
        "agreement/product202510/Mi19X3W2QR.png",
        "agreement/product202510/Lz514m30WB.png",
        "agreement/product202510/k5SXucq6AB.png",
        "agreement/product202510/EYZSm7ZXuB.png",
        "agreement/product202510/iPHFTPAbHf.png",
        "agreement/product202510/aAUOoAZZxg.png",
        "agreement/product202510/nudN8E01IH.png",
        "agreement/product202510/W96KwMEBk3.png",
        "agreement/product202510/jbqbGCBJHR.png",
        "agreement/product202510/9CmKluyi9p.png",
        "agreement/product202510/mnLLdLcPuI.png",
        "agreement/product202510/omrhxSXWgp.png",
        "agreement/product202510/5j03ryBwi1.png",
        "agreement/product202510/r8fDhNoFzU.png",
        "agreement/product202510/xyanHV7Oyr.png",
        "agreement/product202510/YLLtziUtJD.png",
        "agreement/product202510/IPLeaFbkrx.png",
        "agreement/product202510/dYeTu8niPT.png",
        "agreement/product202510/6toggBLKfQ.png",
        "agreement/product202510/T4qQKb9RAE.png",
        "agreement/product202510/ZuAdE1BuvI.png",
        "agreement/product202510/gbWsjswdx8.png",
        "agreement/product202510/O4G7lLVfVE.png",
        "agreement/product202510/P1iKofDgJu.png",
        "agreement/product202510/bAFFjTF04v.png",
        "agreement/product202510/PuoDVvk3vJ.png",
        "agreement/product202510/0dc6syyQ85.png",
        "agreement/product202510/ENxiJaLF8N.png",
        "agreement/product202510/cOfknK0XDk.png",
        "agreement/product202510/OPdTTdBnSF.png",
        "agreement/product202510/3CTPsuXs9f.png",
        "agreement/product202510/OXgzuuLl6Z.png",
        "agreement/product202510/jPo2I4ahzC.png",
        "agreement/product202510/24aqjTYt6L.png",
        "agreement/product202510/D4WUUKcVmz.png",
        "agreement/product202510/UJdVzB9g0l.png",
        "agreement/product202510/KwQ4eFilWv.png"
    ]

    # 排除脚本自身及其他不想参与比较的文件
    exclude_list = {"文件名称比较.py", ".gitignore", "README.md"}  # 可按需添加

    compare_files_by_name(my_file_paths, exclude_set=set(exclude_list))