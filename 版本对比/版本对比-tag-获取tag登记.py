from collections import Counter

# ========== 配置区：可在此添加要排除的服务 ==========
EXCLUDE_SERVICES = {
    'ai-gateway',
    'broker-module-business-biz',
    # 可继续添加...
}
# ===================================================

pre_tag = '''
ai-gateway                     1.0.19
broker-agent-orch              20260113134226
broker-api-gateway             20260112094334
broker-api-orch                20260115111838
broker-business-backend-gateway 20260112094334
broker-business-backend-orch   20260121154317
broker-business-frontend-gateway 20260112094334
broker-business-frontend-orch  20260121134652
broker-common-cmb-client-biz   20251222092839
broker-common-condominium-module-biz 20251222092839
broker-common-condominium-orch-biz 20251222092839
broker-common-module-bank-dict-biz 20260112094334
broker-common-module-code-biz  20260112094334
broker-common-module-express-biz 20260112094334
broker-common-module-gateway   20260112094334
broker-common-module-log-biz   20260112094334
broker-common-module-operate-statistics-biz 20260112094334
broker-common-module-user-statistics-biz 20260112094334
broker-common-rgst-client-biz  20260112094334
broker-common-sub-account-module-biz 20251222092839
broker-common-sub-account-orch-biz 20251222092839
broker-common-transaction-manager-module-biz 20251222092839
broker-common-transaction-manager-orch-biz 20251222092839
broker-common-yunshang-client-biz 20251222092839
broker-module-agent-biz        20260112094334
broker-module-auth-biz         20260112094334
broker-module-base-biz         20260112094334
broker-module-listing-biz      20260112094334
broker-module-member-user-biz  20260121172529
broker-module-operate-user-biz 20260113085612
broker-module-operate-wallet-biz 20260121141919
broker-module-product-biz      20260112094334
broker-module-saas-platform-biz 20251022181010
broker-module-settlement-biz   20260121101843
broker-module-user-collect-biz 20260112094334
broker-open-api-gateway        20260112094334
broker-open-api-orch           20251229205618
broker-operate-gateway         20260112094334
broker-operate-orch            20260121103611
broker-portal-gateway          20260112094334
broker-portal-orch             20260112094334
broker-rgst-api-gateway        20260112094334
broker-rgst-api-orch           20260112094334
broker-saas-platform-gateway   20251020152955
broker-saas-platform-orch      20251020152955
broker-websocket-gateway       20260112094334
broker-websocket-orch          20260112094334
broker-websocket-scheduler     20260112094334
flink-web                      1.4
merchant-h5                    20260121143130
mysql                          8.0.22
nginx                          latest
python3                        3.12.11.4819260.v3
seata-server                   2.2.0
tdengine                       3.2.3.0
web-broker-admin               20260120110803
web-broker-saas-admin          20251022153622
web-lego-builder               20251022152357
web-merchant-backend-base      20260120151802
xxl-job-admin                  2.3.1
zookeeper                      3.9.0
'''

prd_tag = '''
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
broker-module-member-user-biz  20260119204636
broker-module-operate-user-biz 20251222092839
broker-module-operate-wallet-biz 20260119204636
broker-module-product-biz      20251222092839
broker-module-saas-platform-biz 20251022181010
broker-module-settlement-biz   20251225101837
broker-module-user-collect-biz 20251222092839
broker-open-api-gateway        20251222092839
broker-open-api-orch           20251222092839
broker-operate-gateway         20251222092839
broker-operate-orch            20260116121918
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

# --- 解析并过滤排除项 ---
def parse_tag_block(tag_str, exclude_set=None):
    if exclude_set is None:
        exclude_set = set()
    mapping = {}
    for line in tag_str.strip().splitlines():
        parts = line.split()
        if len(parts) >= 2:
            tag = parts[-1]
            name = ' '.join(parts[:-1]).strip()
            if name in exclude_set:
                continue  # 跳过排除项
            mapping[name] = tag
    return mapping

pre_map = parse_tag_block(pre_tag, EXCLUDE_SERVICES)
prd_map = parse_tag_block(prd_tag, EXCLUDE_SERVICES)

# --- 排序函数：重复 tag 优先 ---
def sort_by_tag_frequency(pairs):
    if not pairs:
        return []
    value_count = Counter(v for v, _ in pairs)
    duplicates = []
    uniques = []
    for v, k in pairs:
        if value_count[v] >= 2:
            duplicates.append((v, k))
        else:
            uniques.append((v, k))
    duplicates.sort(key=lambda x: (x[0], x[1]))
    uniques.sort(key=lambda x: (x[0], x[1]))
    return duplicates + uniques

# --- 计算 pre 差异 ---
pre_diff = []
for svc in pre_map:
    if svc not in prd_map or pre_map[svc] != prd_map[svc]:
        pre_diff.append((pre_map[svc], svc))

# --- 排序 pre 并记录顺序 ---
sorted_pre = sort_by_tag_frequency(pre_diff)
pre_service_order = [svc for _, svc in sorted_pre]

# --- 构建 prd 差异字典（已过滤）---
prd_diff_map = {}
for svc in prd_map:
    if svc not in pre_map or prd_map[svc] != pre_map[svc]:
        prd_diff_map[svc] = prd_map[svc]

# --- 按 pre 顺序组织 prd 输出 ---
prd_output_ordered = []
prd_extra = []

for svc in pre_service_order:
    if svc in prd_diff_map:
        prd_output_ordered.append((prd_diff_map[svc], svc))

for svc, tag in prd_diff_map.items():
    if svc not in pre_service_order:
        prd_extra.append((tag, svc))

prd_extra.sort(key=lambda x: (x[0], x[1]))
sorted_prd = prd_output_ordered + prd_extra

# --- 输出 ---
if sorted_pre:
    print("pre")
    for tag, svc in sorted_pre:
        print(f"{tag}\t{svc}")

if sorted_prd:
    print("prd")
    for tag, svc in sorted_prd:
        print(f"{tag}\t{svc}")