import json


def format_tran_date(tran_date_str):
    """将 '20251227' 转为 '2025-12-27'"""
    return f"{tran_date_str[:4]}-{tran_date_str[4:6]}-{tran_date_str[6:8]}"


def generate_sql_for_record(customer_name, request_json_str, response_json_str):
    req = json.loads(request_json_str)
    resp = json.loads(response_json_str)
    item = resp["items"][0]

    cust_no = item["custNo"]
    settl_acc = item["settlAcc"]
    pay_appl_id = item["payApplId"]
    appl_id = req["applId"]
    account_opening_trade_time = format_tran_date(req["tranDate"])

    # 注意：account_opening_serial_no = applId（来自请求）
    # status = 0, account_opening_status = 1, biz_status = 0

    insert_sql = (
        f"INSERT INTO `broker4operate_wallet`.`citic_account_sub` (\n"
        f"  `id`, `tenant_id`, `customer_name`, `cust_no`, `settl_acc`, `pay_appl_id`,\n"
        f"  `account_name`, `account_no`, `amount`, `logic_balance`, `status`, `reason`,\n"
        f"  `serial_no`, `trade_time`, `account_opening_status`, `account_opening_trade_time`,\n"
        f"  `biz_status`, `account_opening_serial_no`, `creator`, `create_time`, `updater`,\n"
        f"  `update_time`, `deleted`\n"
        f") VALUES (\n"
        f"  @ID, @TENANT_ID, @CUSTOMER_NAME, '{cust_no}', '{settl_acc}', '{pay_appl_id}',\n"
        f"  @CUSTOMER_NAME, NULL, 0.00000000, 0.00000000, 0, NULL,\n"
        f"  NULL, NULL, 1, '{account_opening_trade_time}',\n"
        f"  0, '{appl_id}', NULL, NOW(), NULL, NOW(), b'0'\n"
        f");"
    )
    return insert_sql


# ====== 主数据输入区 ======
# 每条记录包含：客户名、请求JSON、响应JSON
records = [
    {
        "customer_name": "esigntest中赋能云商科技有限责任公司测试73",
        "request": '{"applId":"ed4071822f9f4eea8af567e5e8364040","certInvalidDate":"2040-01-01","certValidDate":"2020-01-01","certcNo":"913020202503116961","certcType":"6","clientId":"000899","conpName":"汪敏","custCls":"1","custName":"esigntest中赋能云商科技有限责任公司测试73","handrCertInvalidDate":"2039-08-02","handrCertValidDate":"2019-08-02","handrCertcNo":"421081198909042477","handrCertcType":"0","handrName":"汪敏","legpCertInvalidDate":"2039-08-02","legpCertValidDate":"2019-08-02","legpCertcNo":"421081198909042477","legpCertcType":"0","legpName":"汪敏","mobile":"15071256260","tranDate":"20251219","tranTime":"020032","version":"2.0"}',
        "response": '{"code":"0000","msg":"结算账户[71911987260600]新增成功！","items":[{"payApplId":"1451393737119895552","custNo":"7191198726","settlAcc":"71911987260600"}]}'
    },
    # 可在此添加更多记录，例如：
    # {
    #     "customer_name": "云南国创电采科技有限公司",
    #     "request": '...',
    #     "response": '...'
    # }
]

# ====== 生成 SQL 内容 ======
sql_lines = []

# 初始 SET（只在开头出现一次）
sql_lines.append("-- 初始化变量")
sql_lines.append("SET @ID = (SELECT IFNULL(MAX(id), 0) FROM broker4operate_wallet.citic_account_sub);")
sql_lines.append("")

current_customer = None

for record in records:
    customer_name = record["customer_name"]

    # 如果客户名变化，重新设置 @CUSTOMER_NAME 和 @TENANT_ID
    if customer_name != current_customer:
        sql_lines.append(f"SET @CUSTOMER_NAME = '{customer_name}';")
        sql_lines.append(
            "SET @TENANT_ID = (SELECT id FROM broker4operate_user_v2.opr_tenant WHERE `name` = @CUSTOMER_NAME COLLATE utf8mb4_0900_ai_ci);")
        sql_lines.append("")
        current_customer = customer_name

    # 自增 ID
    sql_lines.append("SET @ID = @ID + 1;")

    # 生成 INSERT
    insert_sql = generate_sql_for_record(
        customer_name=customer_name,
        request_json_str=record["request"],
        response_json_str=record["response"]
    )
    sql_lines.append(insert_sql)
    sql_lines.append("")  # 空行分隔

# ====== 输出到文件或打印 ======
output_sql = "\n".join(sql_lines)

# 写入文件
with open("generate_citic_account_sub.sql", "w", encoding="utf-8") as f:
    f.write(output_sql)

print("✅ SQL 文件已生成：generate_citic_account_sub.sql")
print("\n预览前 500 字符：")
print(output_sql[:500] + "..." if len(output_sql) > 500 else output_sql)