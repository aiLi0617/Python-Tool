import pprint
'''
kubectl get deployment,statefulset,daemonset -n dev-cicd -o jsonpath='{range .items[*]}{.spec.template.spec.containers[*].image}{"\n"}{end}' | awk -F'[/:]' '!seen[$(NF-1),$NF]++ {printf "%-30s %s\n", $(NF-1), $NF}' | sort
'''


pre_tag = '''
ai-gateway                     1.0.19
broker-agent-orch              20251222092839
broker-api-gateway             20251222092839
broker-api-orch                20260106095911
broker-business-backend-gateway 20251222092839
broker-business-backend-orch   20260107165922
broker-business-frontend-gateway 20251222092839
broker-business-frontend-orch  20251222092839
broker-common-cmb-client-biz   20251222092839
broker-common-condominium-module-biz 20251222092839
broker-common-condominium-orch-biz 20251222092839
broker-common-module-bank-dict-biz 20251222092839
broker-common-module-code-biz  20251222092839
broker-common-module-express-biz 20251222092839
broker-common-module-gateway   20251222092839
broker-common-module-log-biz   20251222092839
broker-common-module-operate-statistics-biz 20251222092839
broker-common-module-user-statistics-biz 20251222092839
broker-common-rgst-client-biz  20251222174833
broker-common-sub-account-module-biz 20251222092839
broker-common-sub-account-orch-biz 20251222092839
broker-common-transaction-manager-module-biz 20251222092839
broker-common-transaction-manager-orch-biz 20251222092839
broker-common-yunshang-client-biz 20251222092839
broker-module-agent-biz        20251222092839
broker-module-auth-biz         20251222092839
broker-module-base-biz         20251222092839
broker-module-listing-biz      20251222092839
broker-module-member-user-biz  20260107175512
broker-module-operate-user-biz 20251222092839
broker-module-operate-wallet-biz 20260107092903
broker-module-product-biz      20251222092839
broker-module-saas-platform-biz 20251022181010
broker-module-settlement-biz   20251225101837
broker-module-user-collect-biz 20251222092839
broker-open-api-gateway        20251222092839
broker-open-api-orch           20251222092839
broker-operate-gateway         20251222092839
broker-operate-orch            20260107165922
broker-portal-gateway          20251222092839
broker-portal-orch             20251222092839
broker-rgst-api-gateway        20251222092839
broker-rgst-api-orch           20251222092839
broker-saas-platform-gateway   20251020152955
broker-saas-platform-orch      20251020152955
broker-websocket-gateway       20251222092839
broker-websocket-orch          20251222092839
broker-websocket-scheduler     20251222092839
flink-web                      1.4
merchant-h5                    20260106200922
mysql                          8.0.22
nginx                          latest
python3                        3.12.11.4819260.v3
seata-server                   2.2.0
tdengine                       3.2.3.0
web-broker-admin               20251230163024
web-broker-saas-admin          20251022153622
web-lego-builder               20251022152357
web-merchant-backend-base      20251230163024
xxl-job-admin                  2.3.1
zookeeper                      3.9.0
'''

prd_tag = '''
broker-agent-orch              20251222092839
broker-api-gateway             20251222092839
broker-api-orch                20251222134415
broker-business-backend-gateway 20251222092839
broker-business-backend-orch   20251227224957
broker-business-frontend-gateway 20251222092839
broker-business-frontend-orch  20251222092839
broker-common-cmb-client-biz   20251222092839
broker-common-condominium-module-biz 20251222092839
broker-common-condominium-orch-biz 20251222092839
broker-common-module-bank-dict-biz 20251222092839
broker-common-module-code-biz  20251222092839
broker-common-module-express-biz 20251222092839
broker-common-module-gateway   20251222092839
broker-common-module-log-biz   20251222092839
broker-common-module-operate-statistics-biz 20251222092839
broker-common-module-user-statistics-biz 20251222092839
broker-common-rgst-client-biz  20251222174833
broker-common-sub-account-module-biz 20251222092839
broker-common-sub-account-orch-biz 20251222092839
broker-common-transaction-manager-module-biz 20251222092839
broker-common-transaction-manager-orch-biz 20251222092839
broker-common-yunshang-client-biz 20251222092839
broker-module-agent-biz        20251222092839
broker-module-auth-biz         20251222092839
broker-module-base-biz         20251222092839
broker-module-business-biz     20250925175102
broker-module-listing-biz      20251222092839
broker-module-member-user-biz  20251224190317
broker-module-operate-user-biz 20251222092839
broker-module-operate-wallet-biz 20251222092839
broker-module-product-biz      20251222092839
broker-module-saas-platform-biz 20251022181010
broker-module-settlement-biz   20251225101837
broker-module-user-collect-biz 20251222092839
broker-open-api-gateway        20251222092839
broker-open-api-orch           20251222092839
broker-operate-gateway         20251222092839
broker-operate-orch            20251229151614
broker-portal-gateway          20251222092839
broker-portal-orch             20251222092839
broker-rgst-api-gateway        20251222092839
broker-rgst-api-orch           20251222092839
broker-saas-platform-gateway   20251020152955
broker-saas-platform-orch      20251020152955
broker-websocket-gateway       20251222092839
broker-websocket-orch          20251222092839
broker-websocket-scheduler     20251222092839
flink-web                      1.4
merchant-h5                    20260106200922
mysql                          8.0.22
nginx                          latest
python3                        3.12.11.4819260.v3
seata-server                   2.2.0
tdengine                       3.2.3.0
web-broker-admin               20251230163024
web-broker-saas-admin          20251022153622
web-lego-builder               20251022152357
web-merchant-backend-base      20251230163024
xxl-job-admin                  2.3.1
zookeeper                      3.9.0
'''

doc_tag = '''
20260107165922	broker-business-backend-orch
20260107165922	broker-operate-orch
20260106095911	broker-api-orch
20260107092903	broker-module-operate-wallet-biz
20260107175512	broker-module-member-user-biz
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
        res+= "{}不在doc中 \n".format(k)
        continue
    if pre_map[k] != prd_map[k]:
        res += ("pre {}: {} != prd {}: {} \n").format(k, pre_map[k], k,prd_map[k])

print(res)