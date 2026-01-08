-- 初始化变量
SET @ID = (SELECT IFNULL(MAX(id), 0) FROM broker4operate_wallet.citic_account_sub);

SET @CUSTOMER_NAME = 'esigntest中赋能云商科技有限责任公司测试73';
SET @TENANT_ID = (SELECT id FROM broker4operate_user_v2.opr_tenant WHERE `name` = @CUSTOMER_NAME COLLATE utf8mb4_0900_ai_ci);

SET @ID = @ID + 1;
INSERT INTO `broker4operate_wallet`.`citic_account_sub` (
  `id`, `tenant_id`, `customer_name`, `cust_no`, `settl_acc`, `pay_appl_id`,
  `account_name`, `account_no`, `amount`, `logic_balance`, `status`, `reason`,
  `serial_no`, `trade_time`, `account_opening_status`, `account_opening_trade_time`,
  `biz_status`, `account_opening_serial_no`, `creator`, `create_time`, `updater`,
  `update_time`, `deleted`
) VALUES (
  @ID, @TENANT_ID, @CUSTOMER_NAME, '7191198726', '71911987260600', '1451393737119895552',
  @CUSTOMER_NAME, NULL, 0.00000000, 0.00000000, 0, NULL,
  NULL, NULL, 1, '2025-12-19',
  0, 'ed4071822f9f4eea8af567e5e8364040', NULL, NOW(), NULL, NOW(), b'0'
);
