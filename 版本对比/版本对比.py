pre_tag = '''
ai-gateway                     1.0.5
broker-agent-orch              20251118182313
broker-api-gateway             20251111090023
broker-api-orch                20251124134545
broker-business-backend-gateway 20251111090023
broker-business-backend-orch   20251127151809
broker-business-frontend-gateway 20251111090023
broker-business-frontend-orch  20251119151432
broker-common-cmb-client-biz   20251118182406
broker-common-condominium-module-biz 20251118182406
broker-common-condominium-orch-biz 20251118182406
broker-common-module-bank-dict-biz 20251118182313
broker-common-module-code-biz  20251118182313
broker-common-module-express-biz 20251118182313
broker-common-module-gateway   20251111090023
broker-common-module-log-biz   20251118182313
broker-common-module-operate-statistics-biz 20251118182313
broker-common-module-user-statistics-biz 20251118182313
broker-common-sub-account-module-biz 20251118182406
broker-common-sub-account-orch-biz 20251118182406
broker-common-transaction-manager-module-biz 20251118182406
broker-common-transaction-manager-orch-biz 20251118182406
broker-common-yunshang-client-biz 20251118182406
broker-module-agent-biz        20251118182313
broker-module-auth-biz         20251118182313
broker-module-base-biz         20251124094548
broker-module-listing-biz      20251121180307
broker-module-member-user-biz  20251124094548
broker-module-operate-user-biz 20251118182313
broker-module-operate-wallet-biz 20251118182313
broker-module-product-biz      20251118182313
broker-module-saas-platform-biz 20251022181010
broker-module-settlement-biz   20251126212940
broker-module-user-collect-biz 20251118182313
broker-open-api-gateway        20251111090023
broker-open-api-orch           20251118182313
broker-operate-gateway         20251111090023
broker-operate-orch            20251126215742
broker-portal-gateway          20251111090023
broker-portal-orch             20251118182313
broker-saas-platform-gateway   20251020152955
broker-saas-platform-orch      20251020152955
broker-websocket-gateway       20251111090023
broker-websocket-orch          20251118182313
broker-websocket-scheduler     20251118182313
flink-web                      1.4
merchant-h5                    20250919101545
mysql                          8.0.22
nginx                          latest
python3                        3.12.11.4819260.v3
seata-server                   2.2.0
tdengine                       3.2.3.0
web-broker-admin               20251126201157
web-broker-saas-admin          20251022153622
web-lego-builder               20251022152357
web-merchant-backend-base      20251126192011
xxl-job-admin                  2.3.1
zookeeper                      3.9.0
'''

doc_tag = '''
broker-agent-orch              20251118182313
broker-api-gateway             20251111090023
broker-api-orch                20251124134545
broker-business-backend-gateway 20251111090023
broker-business-backend-orch   20251127151809
broker-business-frontend-gateway 20251111090023
broker-business-frontend-orch  20251119151432
broker-common-cmb-client-biz   20251118182406
broker-common-condominium-module-biz 20251118182406
broker-common-condominium-orch-biz 20251118182406
broker-common-module-bank-dict-biz 20251118182313
broker-common-module-code-biz  20251118182313
broker-common-module-express-biz 20251118182313
broker-common-module-gateway   20251111090023
broker-common-module-log-biz   20251118182313
broker-common-module-operate-statistics-biz 20251118182313
broker-common-module-user-statistics-biz 20251118182313
broker-common-sub-account-module-biz 20251118182406
broker-common-sub-account-orch-biz 20251118182406
broker-common-transaction-manager-module-biz 20251118182406
broker-common-transaction-manager-orch-biz 20251118182406
broker-common-yunshang-client-biz 20251118182406
broker-module-agent-biz        20251118182313
broker-module-auth-biz         20251118182313
broker-module-base-biz         20251124094548
broker-module-business-biz     20250925175102
broker-module-listing-biz      20251121180307
broker-module-member-user-biz  20251124094548
broker-module-operate-user-biz 20251118182313
broker-module-operate-wallet-biz 20251118182313
broker-module-product-biz      20251118182313
broker-module-saas-platform-biz 20251022181010
broker-module-settlement-biz   20251126212940
broker-module-user-collect-biz 20251118182313
broker-open-api-gateway        20251111090023
broker-open-api-orch           20251118182313
broker-operate-gateway         20251111090023
broker-operate-orch            20251126215742
broker-portal-gateway          20251111090023
broker-portal-orch             20251118182313
broker-saas-platform-gateway   20251020152955
broker-saas-platform-orch      20251020152955
broker-websocket-gateway       20251111090023
broker-websocket-orch          20251118182313
broker-websocket-scheduler     20251118182313
flink-web                      1.4
merchant-h5                    20250919101545
mysql                          8.0.22
nginx                          latest
python3                        3.12.11.4819260.v3
seata-server                   2.2.0
tdengine                       3.2.3.0
web-broker-admin               20251126201157
web-broker-saas-admin          20251022153622
web-lego-builder               20251022152357
web-merchant-backend-base      20251126192011
xxl-job-admin                  2.3.1
zookeeper                      3.9.0
'''

pre_list = pre_tag.split()
pre_map = dict()
for i in range(0, len(pre_list), 2):
    pre_map[pre_list[i]] = pre_list[i+1]

doc_list = doc_tag.split()
doc_map = dict()
for i in range(0, len(doc_list), 2):
    # doc_map[doc_list[i+1]] = doc_list[i]
    doc_map[doc_list[i]] = doc_list[i+1]

print(pre_map)
print(doc_map)

pre_res = dict()
for key, value in pre_map.items():
    if key not in doc_map:
        pre_res[key] = "pre:{} , doc: null".format(value)
        continue
    if doc_map[key] != value:
        pre_res[key] = "pre: {}, doc: {}".format(value, doc_map[key])

doc_res = dict()
for key, value in doc_map.items():
    if key not in pre_map:
        doc_res[key] = "pre:null , doc: {}".format(value)
        continue
    if pre_map[key] != value:
        doc_res[key] = "pre: {}, doc: {}".format(pre_map[key], value)

print(pre_res)
print(doc_res)