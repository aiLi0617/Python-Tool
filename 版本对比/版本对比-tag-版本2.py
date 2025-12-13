import pprint
'''
kubectl get deployment,statefulset,daemonset -n dev-cicd -o jsonpath='{range .items[*]}{.spec.template.spec.containers[*].image}{"\n"}{end}' | awk -F'[/:]' '!seen[$(NF-1),$NF]++ {printf "%-30s %s\n", $(NF-1), $NF}' | sort
'''


pre_tag = '''
ai-gateway                     1.0.17
broker-agent-orch              20251118182313
broker-api-gateway             20251111090023
broker-api-orch                20251210095417
broker-business-backend-gateway 20251111090023
broker-business-backend-orch   20251211161251
broker-business-frontend-gateway 20251111090023
broker-business-frontend-orch  20251210095417
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
broker-module-base-biz         20251209114107
broker-module-listing-biz      20251209114107
broker-module-member-user-biz  20251124094548
broker-module-operate-user-biz 20251118182313
broker-module-operate-wallet-biz 20251210165653
broker-module-product-biz      20251210095417
broker-module-saas-platform-biz 20251022181010
broker-module-settlement-biz   20251211221234
broker-module-user-collect-biz 20251118182313
broker-open-api-gateway        20251111090023
broker-open-api-orch           20251211221234
broker-operate-gateway         20251111090023
broker-operate-orch            20251211161251
broker-portal-gateway          20251111090023
broker-portal-orch             20251210095417
broker-saas-platform-gateway   20251020152955
broker-saas-platform-orch      20251020152955
broker-websocket-gateway       20251111090023
broker-websocket-orch          20251118182313
broker-websocket-scheduler     20251118182313
flink-web                      1.4
merchant-h5                    20251211145351
mysql                          8.0.22
nginx                          latest
python3                        3.12.11.4819260.v3
seata-server                   2.2.0
tdengine                       3.2.3.0
web-broker-admin               20251211210458
web-broker-saas-admin          20251022153622
web-lego-builder               20251022152357
web-merchant-backend-base      20251211100503
xxl-job-admin                  2.3.1
zookeeper                      3.9.0
'''

prd_tag = '''
broker-agent-orch              20251118182313
broker-api-gateway             20251111090023
broker-api-orch                20251210095417
broker-business-backend-gateway 20251111090023
broker-business-backend-orch   20251211161251
broker-business-frontend-gateway 20251111090023
broker-business-frontend-orch  20251210095417
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
broker-module-base-biz         20251209114107
broker-module-business-biz     20250925175102
broker-module-listing-biz      20251209114107
broker-module-member-user-biz  20251124094548
broker-module-operate-user-biz 20251118182313
broker-module-operate-wallet-biz 20251210165653
broker-module-product-biz      20251210095417
broker-module-saas-platform-biz 20251022181010
broker-module-settlement-biz   20251211221234
broker-module-user-collect-biz 20251118182313
broker-open-api-gateway        20251111090023
broker-open-api-orch           20251211221234
broker-operate-gateway         20251111090023
broker-operate-orch            20251211161251
broker-portal-gateway          20251111090023
broker-portal-orch             20251210095417
broker-saas-platform-gateway   20251020152955
broker-saas-platform-orch      20251020152955
broker-websocket-gateway       20251111090023
broker-websocket-orch          20251118182313
broker-websocket-scheduler     20251118182313
flink-web                      1.4
merchant-h5                    20251211145351
mysql                          8.0.22
nginx                          latest
python3                        3.12.11.4819260.v3
seata-server                   2.2.0
tdengine                       3.2.3.0
web-broker-admin               20251211210458
web-broker-saas-admin          20251022153622
web-lego-builder               20251022152357
web-merchant-backend-base      20251211100503
xxl-job-admin                  2.3.1
zookeeper                      3.9.0
'''

doc_tag = '''
'''


pre_list = pre_tag.split()
pre_map = dict()
for i in range(0, len(pre_list), 2):
    pre_map[pre_list[i]] = pre_list[i+1]

prd_list = prd_tag.split()
prd_map = dict()
for i in range(0, len(prd_list), 2):
    prd_map[prd_list[i]] = prd_list[i + 1]

doc_list = doc_tag.split()
doc_map = dict()
for i in range(0, len(doc_list), 2):
    doc_map[doc_list[i+1]] = doc_list[i]

for i, val in doc_map.items():
    prd_map[i] = doc_map[i]

# print(prd_map - doc_map)
res = ""
for k, v in pre_map.items():
    if k not in prd_map:
        res+= "{}不在doc中".format(k)
        continue
    if pre_map[k] != prd_map[k]:
        res += ("pre {}: {} != prd {}: {} \n").format(k, pre_map[k], k,prd_map[k])
print(res)
