import os
import shutil

# === 配置区：在这里填写你的目标路径列表 ===
TARGET_PATHS = [
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


def get_source_file():
    """获取当前目录中唯一的非 .py 源文件"""
    files = [f for f in os.listdir('.')
             if os.path.isfile(f) and not f.endswith('.py')]

    if len(files) == 0:
        raise FileNotFoundError("未找到非 .py 的源文件！请放入一个如 .png / .pdf 等文件。")
    if len(files) > 1:
        raise ValueError(f"找到多个非 .py 文件，请只保留一个源文件！文件列表: {files}")

    return files[0]

def copy_to_paths(source_file, target_paths):
    for target_path in target_paths:
        target_dir = os.path.dirname(target_path)
        os.makedirs(target_dir, exist_ok=True)
        dest = os.path.join(target_dir, os.path.basename(target_path))
        shutil.copy2(source_file, dest)
        print(f"✅ 已复制: {source_file} → {dest}")

if __name__ == "__main__":
    try:
        source = get_source_file()
        print(f"📁 使用源文件: {source}")
        copy_to_paths(source, TARGET_PATHS)
        print("\n🎉 复制完成！")
    except Exception as e:
        print(f"❌ 错误: {e}")