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
        "customer_name": "深圳市数元信息技术有限公司",
        "request": '{"applId":"af401bf08ee74bb1a199f6be105d46eb","certInvalidDate":"2040-01-01","certValidDate":"2020-01-01","certcNo":"91440300306264631E","certcType":"6","clientId":"000900","conpName":"袁丽芳","custCls":"1","custName":"深圳市数元信息技术有限公司","handrCertInvalidDate":"2039-08-19","handrCertValidDate":"2019-08-19","handrCertcNo":"43030219900311328X","handrCertcType":"0","handrName":"颜书雅","legpCertInvalidDate":"2039-08-19","legpCertValidDate":"2019-08-19","legpCertcNo":"43030219900311328X","legpCertcType":"0","legpName":"颜书雅","mobile":"15813740307","tranDate":"20251227","tranTime":"195505","version":"2.0"}',
        "response": '{"code":"0000","msg":"结算账户[08870769250600]新增成功！","items":[{"payApplId":"1454563260819968000","custNo":"0887076925","settlAcc":"08870769250600"}]}'
    },
    {
        "customer_name": "深圳市兆芯微电子有限公司",
        "request": '{"applId":"6f939d84df824a23a512933e66dce3b7","certInvalidDate":"2040-01-01","certValidDate":"2020-01-01","certcNo":"91440300MA5EHRB64X","certcType":"6","clientId":"000900","conpName":"谢芳","custCls":"1","custName":"深圳市兆芯微电子有限公司","handrCertInvalidDate":"2036-04-09","handrCertValidDate":"2016-04-09","handrCertcNo":"429006198508210326","handrCertcType":"0","handrName":"谢芳","legpCertInvalidDate":"2035-04-11","legpCertValidDate":"2015-04-11","legpCertcNo":"110221198011117023","legpCertcType":"0","legpName":"王鑫","mobile":"18126100076","tranDate":"20251227","tranTime":"195506","version":"2.0"}',
        "response": '{"code":"0000","msg":"结算账户[36091802130600]新增成功！","items":[{"payApplId":"1454563263537876992","custNo":"3609180213","settlAcc":"36091802130600"}]}'
    },
    {
        "customer_name": "普柏家具（深圳）有限公司",
        "request": '{"applId":"2ad0f79e540f44e8a05b2d9a624ca98e","certInvalidDate":"2040-01-01","certValidDate":"2020-01-01","certcNo":"91440300MA5F5TXA8H","certcType":"6","clientId":"000900","conpName":"黄剑","custCls":"1","custName":"普柏家具（深圳）有限公司","handrCertInvalidDate":"2038-09-04","handrCertValidDate":"2018-09-04","handrCertcNo":"421124198604257053","handrCertcType":"0","handrName":"黄剑","legpCertInvalidDate":"2043-10-25","legpCertValidDate":"2023-10-25","legpCertcNo":"42118119920724623X","legpCertcType":"0","legpName":"刘林涛","mobile":"13510713226","tranDate":"20251227","tranTime":"195507","version":"2.0"}',
        "response": '{"code":"0000","msg":"结算账户[01061570720600]新增成功！","items":[{"payApplId":"1454563270009688064","custNo":"0106157072","settlAcc":"01061570720600"}]}'
    },
    {
        "customer_name": "上海祎邦仁商贸有限公司",
        "request": '{"applId":"8fffe89d266a4922a8ae47845da5e56d","certInvalidDate":"2040-01-01","certValidDate":"2020-01-01","certcNo":"91310105MAC2L0K37B","certcType":"6","clientId":"000900","conpName":"顾轶","custCls":"1","custName":"上海祎邦仁商贸有限公司","handrCertInvalidDate":"2041-08-17","handrCertValidDate":"2021-08-17","handrCertcNo":"320583198608127114","handrCertcType":"0","handrName":"顾轶","legpCertInvalidDate":"2041-08-17","legpCertValidDate":"2021-08-17","legpCertcNo":"320583198608127114","legpCertcType":"0","legpName":"顾轶","mobile":"18601751233","tranDate":"20251227","tranTime":"195508","version":"2.0"}',
        "response": '{"code":"0000","msg":"结算账户[29121464680600]新增成功！","items":[{"payApplId":"1454563272840843264","custNo":"2912146468","settlAcc":"29121464680600"}]}'
    },
    {
        "customer_name": "北京慧思智联健康科技有限公司",
        "request": '{"applId":"65eaadb2d256438dae36ec43aa1661a0","certInvalidDate":"2040-01-01","certValidDate":"2020-01-01","certcNo":"91110106MAEPR6XM9J","certcType":"6","clientId":"000900","conpName":"王一祎","custCls":"1","custName":"北京慧思智联健康科技有限公司","handrCertInvalidDate":"2041-12-22","handrCertValidDate":"2021-12-22","handrCertcNo":"410105199510060148","handrCertcType":"0","handrName":"王一祎","legpCertInvalidDate":"2030-03-09","legpCertValidDate":"2020-03-09","legpCertcNo":"410881200008186511","legpCertcType":"0","legpName":"翟志文","mobile":"13903831670","tranDate":"20251227","tranTime":"195509","version":"2.0"}',
        "response": '{"code":"0000","msg":"结算账户[56929700620600]新增成功！","items":[{"payApplId":"1454563275621666816","custNo":"5692970062","settlAcc":"56929700620600"}]}'
    },
    {
        "customer_name": "鄂尔多斯市江科咨询服务有限责任公司",
        "request": '{"applId":"638a94eda14e4db292121e85051b5150","certInvalidDate":"2040-01-01","certValidDate":"2020-01-01","certcNo":"91150691MACAT61763","certcType":"6","clientId":"000900","conpName":"乔涛","custCls":"1","custName":"鄂尔多斯市江科咨询服务有限责任公司","handrCertInvalidDate":"2038-11-29","handrCertValidDate":"2018-11-29","handrCertcNo":"152728198906123660","handrCertcType":"0","handrName":"乔涛","legpCertInvalidDate":"2028-01-04","legpCertValidDate":"2008-01-04","legpCertcNo":"152701197304174829","legpCertcType":"0","legpName":"缪美琴","mobile":"15048759395","tranDate":"20251227","tranTime":"195509","version":"2.0"}',
        "response": '{"code":"0000","msg":"结算账户[82598840510600]新增成功！","items":[{"payApplId":"1454563278180192256","custNo":"8259884051","settlAcc":"82598840510600"}]}'
    },
    {
        "customer_name": "深圳家联网贸易有限公司",
        "request": '{"applId":"94f331a2a2ed4dd0a79ab62aaef01eba","certInvalidDate":"2040-01-01","certValidDate":"2020-01-01","certcNo":"91440300MA5F5LGKXN","certcType":"6","clientId":"000900","conpName":"温振华","custCls":"1","custName":"深圳家联网贸易有限公司","handrCertInvalidDate":"2045-07-07","handrCertValidDate":"2025-07-07","handrCertcNo":"44162119951112731X","handrCertcType":"0","handrName":"温振华","legpCertInvalidDate":"2123-12-26","legpCertValidDate":"2023-12-26","legpCertcNo":"43082119630708007X","legpCertcType":"0","legpName":"杨万军","mobile":"13682507472","tranDate":"20251227","tranTime":"195510","version":"2.0"}',
        "response": '{"code":"0000","msg":"结算账户[06841917930600]新增成功！","items":[{"payApplId":"1454563280604499968","custNo":"0684191793","settlAcc":"06841917930600"}]}'
    },
    {
        "customer_name": "广州狮岭皮革皮具产业研究中心有限公司",
        "request": '{"applId":"f62548f473554eb2b6e6abefce478b21","certInvalidDate":"2040-01-01","certValidDate":"2020-01-01","certcNo":"914401146734915107","certcType":"6","clientId":"000900","conpName":"龙虹池","custCls":"1","custName":"广州狮岭皮革皮具产业研究中心有限公司","handrCertInvalidDate":"2039-04-30","handrCertValidDate":"2019-04-30","handrCertcNo":"422429197709218258","handrCertcType":"0","handrName":"罗杨","legpCertInvalidDate":"2039-04-30","legpCertValidDate":"2019-04-30","legpCertcNo":"422429197709218258","legpCertcType":"0","legpName":"罗杨","mobile":"15217635156","tranDate":"20251227","tranTime":"195511","version":"2.0"}',
        "response": '{"code":"0000","msg":"结算账户[30833336760600]新增成功！","items":[{"payApplId":"1454563283012030464","custNo":"3083333676","settlAcc":"30833336760600"}]}'
    },
    {
        "customer_name": "旭力欧（重庆）商贸有限公司",
        "request": '{"applId":"b72e2942750b4c1c9677484920d468db","certInvalidDate":"2040-01-01","certValidDate":"2020-01-01","certcNo":"91500116MA7LGNBE3K","certcType":"6","clientId":"000900","conpName":"杨倓杰","custCls":"1","custName":"旭力欧（重庆）商贸有限公司","handrCertInvalidDate":"2038-01-08","handrCertValidDate":"2018-01-08","handrCertcNo":"510282198211246222","handrCertcType":"0","handrName":"代贵宁","legpCertInvalidDate":"2038-01-08","legpCertValidDate":"2018-01-08","legpCertcNo":"510282198211246222","legpCertcType":"0","legpName":"代贵宁","mobile":"15002334460","tranDate":"20251227","tranTime":"195511","version":"2.0"}',
        "response": '{"code":"0000","msg":"结算账户[55286129450600]新增成功！","items":[{"payApplId":"1454563285461504000","custNo":"5528612945","settlAcc":"55286129450600"}]}'
    },
    {
        "customer_name": "竞采科技有限公司",
        "request": '{"applId":"a709662a554a46fc90f9bebe9cd1f520","certInvalidDate":"2040-01-01","certValidDate":"2020-01-01","certcNo":"91110108MA01FRMJ9B","certcType":"6","clientId":"000900","conpName":"王若钧","custCls":"1","custName":"竞采科技有限公司","handrCertInvalidDate":"2026-05-24","handrCertValidDate":"2016-05-24","handrCertcNo":"230221199302130211","handrCertcType":"0","handrName":"王宏勋","legpCertInvalidDate":"2026-05-24","legpCertValidDate":"2016-05-24","legpCertcNo":"230221199302130211","legpCertcType":"0","legpName":"王宏勋","mobile":"13522014371","tranDate":"20251227","tranTime":"195512","version":"2.0"}',
        "response": '{"code":"0000","msg":"结算账户[79864750220600]新增成功！","items":[{"payApplId":"1454563287915171840","custNo":"7986475022","settlAcc":"79864750220600"}]}'
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
            "SET @TENANT_ID = (SELECT id FROM broker4operate_v2.opt_tenant WHERE `name` = @CUSTOMER_NAME);")
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