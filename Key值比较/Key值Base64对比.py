import base64
import yaml
import re

# ==============================
# 1. 明文配置（你的原始配置内容）
# ==============================
plaintext_config_str = """
operate-orch

# 中信基础配置
# 登结公钥
CITIC_REGISTRY_PUBLIC_KEY=MFkwEwYHKoZIzj0CAQYIKoEcz1UBgi0DQgAEDuKjusHb7k4s+2VRissr80Rc94yUDk7xYXXi6dm2VrbZplUh4alTAvS0l20+38hyDIIklCv7af/MmAj1rPCrpQ==
# 经纪商公钥
CITIC_CLIENT_PUBLIC_KEY=MFkwEwYHKoZIzj0CAQYIKoEcz1UBgi0DQgAE1t4X/YvO+yZnxmtLtyKvLqQpDFEn0UKoP53+R/P4Q88w1LnVoyLV0hog7hjEuxiNUKQkn0lXsPgxiC9CwIjGvw==
# 经纪商私钥
CITIC_CLIENT_PRIVATE_KEY=MIGTAgEAMBMGByqGSM49AgEGCCqBHM9VAYItBHkwdwIBAQQg9/L9ABBVXcA1m3rv6DFAiSjk2179ft/IExRUC3O1bwOgCgYIKoEcz1UBgi2hRANCAATW3hf9i877JmfGa0u3Iq8upCkMUSfRQqg/nf5H8/hDzzDUudWjItXSGiDuGMS7GI1QpCSfSVew+DGIL0LAiMa/
# 经纪商对称密钥
CITIC_SECRET_KEY=QRGXicognnkVStqf+wfr2g==
# 经纪商平台代码
CITIC_CLIENT_ID=000899
# 登结网关网址
CITIC_GATEWAY_URL=http://139.9.216.232:18080/services/rgst

# 中信资金银行配置
# 资金账号名称
CITIC_BANK_ACCOUNT_NAME=交易在途资金-B2B平台类
# 资金账号
CITIC_BANK_ACCOUNT_NO=7440110126501123568
# 固定
CITIC_BANK_NAME=中信银行深圳分行

# 通联账户配置
# 固定
CITIC_RGST_BANK_ACCOUNT_NAME=通联支付网络服务股份有限公司
# 固定
CITIC_RGST_BANK_NAME=通联支付网络服务股份有限公司
# 固定
CITIC_RGST_COMPANY_NAME=通联支付网络服务股份有限公司
# 固定
CITIC_RGST_COMPANY_CODE=91310000680985471T

# 中信云商账户配置
# 云商结算账号
RGST_YUNSHANG_ACCOUNT=0009000600
# 固定
RGST_YUNSHANG_ACCOUNT_NAME=中赋能云商科技有限责任公司
# 固定
RGST_YUNSHANG_BANK_NAME=中信银行深圳分行
# 云商平台分簿
RGST_YUNSHANG_BANK_ACCOUNT=744011012650116046500400000002
"""

# ==============================
# 2. Kubernetes Secret YAML
# ==============================
secret_yaml_str = """
kind: Secret
apiVersion: v1
metadata:
  name: encryption.key
  namespace: pre-cicd
data:
  CITIC_BANK_ACCOUNT_NAME: 5Lqk5piT5Zyo6YCU6LWE6YeRLUIyQuW5s+WPsOexuw==
  CITIC_BANK_ACCOUNT_NO: NzQ0MDExMDEyNjUwMTEyMzU2OA==
  CITIC_BANK_NAME: 5Lit5L+h6ZO26KGM5rex5Zyz5YiG6KGM
  CITIC_CLIENT_ID: MDAwODk5
  CITIC_CLIENT_PRIVATE_KEY: TUlHVEFnRUFNQk1HQnlxR1NNNDlBZ0VHQ0NxQkhNOVZBWUl0Qkhrd2R3SUJBUVFnOS9MOUFCQlZYY0ExbTNydjZERkFpU2prMjE3OWZ0L0lFeFJVQzNPMWJ3T2dDZ1lJS29FY3oxVUJnaTJoUkFOQ0FBVFczaGY5aTg3N0ptZkdhMHUzSXE4dXBDa01VU2ZSUXFnL25mNUg4L2hEenpEVXVkV2pJdFhTR2lEdUdNUzdHSTFRcENTZlNWZXcrREdJTDBMQWlNYS8=
  CITIC_CLIENT_PUBLIC_KEY: TUZrd0V3WUhLb1pJemowQ0FRWUlLb0VjejFVQmdpMERRZ0FFMXQ0WC9Zdk8reVpueG10THR5S3ZMcVFwREZFbjBVS29QNTMrUi9QNFE4OHcxTG5Wb3lMVjBob2c3aGpFdXhpTlVLUWtuMGxYc1BneGlDOUN3SWpHdnc9PQ==
  CITIC_GATEWAY_URL: aHR0cDovLzEzOS45LjIxNi4yMzI6MTgwODAvc2VydmljZXMvcmdzdA==
  CITIC_REGISTRY_PUBLIC_KEY: TUZrd0V3WUhLb1pJemowQ0FRWUlLb0VjejFVQmdpMERRZ0FFRHVLanVzSGI3azRzKzJWUmlzc3I4MFJjOTR5VURrN3hZWFhpNmRtMlZyYlpwbFVoNGFsVEF2UzBsMjArMzhoeURJSWtsQ3Y3YWYvTW1BajFyUENycFE9PQ==
  CITIC_RGST_BANK_ACCOUNT_NAME: 6YCa6IGU5pSv5LuY572R57uc5pyN5Yqh6IKh5Lu95pyJ6ZmQ5YWs5Y+4
  CITIC_RGST_BANK_NAME: 6YCa6IGU5pSv5LuY572R57uc5pyN5Yqh6IKh5Lu95pyJ6ZmQ5YWs5Y+4
  CITIC_RGST_COMPANY_CODE: OTEzMTAwMDA2ODA5ODU0NzFU
  CITIC_RGST_COMPANY_NAME: 6YCa6IGU5pSv5LuY572R57uc5pyN5Yqh6IKh5Lu95pyJ6ZmQ5YWs5Y+4
  CITIC_SECRET_KEY: UVJHWGljb2dubmtWU3RxZit3ZnIyZz09
type: Opaque
"""

# ==============================
# 3. 解析明文配置（忽略注释、空行、无效行）
# ==============================
def parse_plaintext_config(config_str):
    config = {}
    for line in config_str.strip().splitlines():
        line = line.strip()
        # 跳过空行、注释、或不含 '=' 的行（如 "operate-orch"）
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, value = line.split("=", 1)
        config[key.strip()] = value.strip()
    return config

# ==============================
# 4. Base64 编码函数
# ==============================
def to_base64(s: str) -> str:
    return base64.b64encode(s.encode('utf-8')).decode('ascii')

# ==============================
# 5. 主比对逻辑
# ==============================
def main():
    # 解析明文
    plaintext = parse_plaintext_config(plaintext_config_str)
    # 解析 Secret
    secret_data = yaml.safe_load(secret_yaml_str)['data']

    print("🔍 开始比对明文配置与 Kubernetes Secret...\n")
    all_match = True

    # 检查明文中每个 key 是否在 Secret 中匹配
    for key, plain_val in plaintext.items():
        if key not in secret_data:
            print(f"❌ 明文中的键 {key} 在 Secret 中缺失！")
            all_match = False
            continue

        expected_b64 = to_base64(plain_val)
        actual_b64 = secret_data[key]

        if expected_b64 == actual_b64:
            print(f"✅ {key}: 匹配")
        else:
            print(f"❌ {key}: 不匹配")
            print(f"   明文: {plain_val}")
            print(f"   预期 Base64: {expected_b64}")
            print(f"   实际 Base64: {actual_b64}")
            all_match = False

    # 检查 Secret 中是否有明文未覆盖的 key（可选）
    extra_in_secret = set(secret_data.keys()) - set(plaintext.keys())
    if extra_in_secret:
        print(f"\nℹ️  注意：Secret 中存在未在明文中定义的 key: {sorted(extra_in_secret)}")

    print("\n" + ("🟢 所有明文字段在 Secret 中匹配成功！" if all_match else "🔴 存在不匹配或缺失字段！"))

if __name__ == "__main__":
    main()