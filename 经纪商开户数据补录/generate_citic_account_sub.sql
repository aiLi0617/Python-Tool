-- 初始化变量
SET @ID = (SELECT IFNULL(MAX(id), 0) FROM broker4operate_wallet.citic_account_sub);

SET @CUSTOMER_NAME = '深圳市数元信息技术有限公司';
SET @TENANT_ID = (SELECT id FROM broker4operate_v2.opt_tenant WHERE `name` = @CUSTOMER_NAME);

SET @ID = @ID + 1;
INSERT INTO `broker4operate_wallet`.`citic_account_sub` (
  `id`, `tenant_id`, `customer_name`, `cust_no`, `settl_acc`, `pay_appl_id`,
  `account_name`, `account_no`, `amount`, `logic_balance`, `status`, `reason`,
  `serial_no`, `trade_time`, `account_opening_status`, `account_opening_trade_time`,
  `biz_status`, `account_opening_serial_no`, `creator`, `create_time`, `updater`,
  `update_time`, `deleted`
) VALUES (
  @ID, @TENANT_ID, @CUSTOMER_NAME, '0887076925', '08870769250600', '1454563260819968000',
  @CUSTOMER_NAME, NULL, 0.00000000, 0.00000000, 0, NULL,
  NULL, NULL, 1, '2025-12-27',
  0, 'af401bf08ee74bb1a199f6be105d46eb', NULL, NOW(), NULL, NOW(), b'0'
);

SET @CUSTOMER_NAME = '深圳市兆芯微电子有限公司';
SET @TENANT_ID = (SELECT id FROM broker4operate_v2.opt_tenant WHERE `name` = @CUSTOMER_NAME);

SET @ID = @ID + 1;
INSERT INTO `broker4operate_wallet`.`citic_account_sub` (
  `id`, `tenant_id`, `customer_name`, `cust_no`, `settl_acc`, `pay_appl_id`,
  `account_name`, `account_no`, `amount`, `logic_balance`, `status`, `reason`,
  `serial_no`, `trade_time`, `account_opening_status`, `account_opening_trade_time`,
  `biz_status`, `account_opening_serial_no`, `creator`, `create_time`, `updater`,
  `update_time`, `deleted`
) VALUES (
  @ID, @TENANT_ID, @CUSTOMER_NAME, '3609180213', '36091802130600', '1454563263537876992',
  @CUSTOMER_NAME, NULL, 0.00000000, 0.00000000, 0, NULL,
  NULL, NULL, 1, '2025-12-27',
  0, '6f939d84df824a23a512933e66dce3b7', NULL, NOW(), NULL, NOW(), b'0'
);

SET @CUSTOMER_NAME = '普柏家具（深圳）有限公司';
SET @TENANT_ID = (SELECT id FROM broker4operate_v2.opt_tenant WHERE `name` = @CUSTOMER_NAME);

SET @ID = @ID + 1;
INSERT INTO `broker4operate_wallet`.`citic_account_sub` (
  `id`, `tenant_id`, `customer_name`, `cust_no`, `settl_acc`, `pay_appl_id`,
  `account_name`, `account_no`, `amount`, `logic_balance`, `status`, `reason`,
  `serial_no`, `trade_time`, `account_opening_status`, `account_opening_trade_time`,
  `biz_status`, `account_opening_serial_no`, `creator`, `create_time`, `updater`,
  `update_time`, `deleted`
) VALUES (
  @ID, @TENANT_ID, @CUSTOMER_NAME, '0106157072', '01061570720600', '1454563270009688064',
  @CUSTOMER_NAME, NULL, 0.00000000, 0.00000000, 0, NULL,
  NULL, NULL, 1, '2025-12-27',
  0, '2ad0f79e540f44e8a05b2d9a624ca98e', NULL, NOW(), NULL, NOW(), b'0'
);

SET @CUSTOMER_NAME = '上海祎邦仁商贸有限公司';
SET @TENANT_ID = (SELECT id FROM broker4operate_v2.opt_tenant WHERE `name` = @CUSTOMER_NAME);

SET @ID = @ID + 1;
INSERT INTO `broker4operate_wallet`.`citic_account_sub` (
  `id`, `tenant_id`, `customer_name`, `cust_no`, `settl_acc`, `pay_appl_id`,
  `account_name`, `account_no`, `amount`, `logic_balance`, `status`, `reason`,
  `serial_no`, `trade_time`, `account_opening_status`, `account_opening_trade_time`,
  `biz_status`, `account_opening_serial_no`, `creator`, `create_time`, `updater`,
  `update_time`, `deleted`
) VALUES (
  @ID, @TENANT_ID, @CUSTOMER_NAME, '2912146468', '29121464680600', '1454563272840843264',
  @CUSTOMER_NAME, NULL, 0.00000000, 0.00000000, 0, NULL,
  NULL, NULL, 1, '2025-12-27',
  0, '8fffe89d266a4922a8ae47845da5e56d', NULL, NOW(), NULL, NOW(), b'0'
);

SET @CUSTOMER_NAME = '北京慧思智联健康科技有限公司';
SET @TENANT_ID = (SELECT id FROM broker4operate_v2.opt_tenant WHERE `name` = @CUSTOMER_NAME);

SET @ID = @ID + 1;
INSERT INTO `broker4operate_wallet`.`citic_account_sub` (
  `id`, `tenant_id`, `customer_name`, `cust_no`, `settl_acc`, `pay_appl_id`,
  `account_name`, `account_no`, `amount`, `logic_balance`, `status`, `reason`,
  `serial_no`, `trade_time`, `account_opening_status`, `account_opening_trade_time`,
  `biz_status`, `account_opening_serial_no`, `creator`, `create_time`, `updater`,
  `update_time`, `deleted`
) VALUES (
  @ID, @TENANT_ID, @CUSTOMER_NAME, '5692970062', '56929700620600', '1454563275621666816',
  @CUSTOMER_NAME, NULL, 0.00000000, 0.00000000, 0, NULL,
  NULL, NULL, 1, '2025-12-27',
  0, '65eaadb2d256438dae36ec43aa1661a0', NULL, NOW(), NULL, NOW(), b'0'
);

SET @CUSTOMER_NAME = '鄂尔多斯市江科咨询服务有限责任公司';
SET @TENANT_ID = (SELECT id FROM broker4operate_v2.opt_tenant WHERE `name` = @CUSTOMER_NAME);

SET @ID = @ID + 1;
INSERT INTO `broker4operate_wallet`.`citic_account_sub` (
  `id`, `tenant_id`, `customer_name`, `cust_no`, `settl_acc`, `pay_appl_id`,
  `account_name`, `account_no`, `amount`, `logic_balance`, `status`, `reason`,
  `serial_no`, `trade_time`, `account_opening_status`, `account_opening_trade_time`,
  `biz_status`, `account_opening_serial_no`, `creator`, `create_time`, `updater`,
  `update_time`, `deleted`
) VALUES (
  @ID, @TENANT_ID, @CUSTOMER_NAME, '8259884051', '82598840510600', '1454563278180192256',
  @CUSTOMER_NAME, NULL, 0.00000000, 0.00000000, 0, NULL,
  NULL, NULL, 1, '2025-12-27',
  0, '638a94eda14e4db292121e85051b5150', NULL, NOW(), NULL, NOW(), b'0'
);

SET @CUSTOMER_NAME = '深圳家联网贸易有限公司';
SET @TENANT_ID = (SELECT id FROM broker4operate_v2.opt_tenant WHERE `name` = @CUSTOMER_NAME);

SET @ID = @ID + 1;
INSERT INTO `broker4operate_wallet`.`citic_account_sub` (
  `id`, `tenant_id`, `customer_name`, `cust_no`, `settl_acc`, `pay_appl_id`,
  `account_name`, `account_no`, `amount`, `logic_balance`, `status`, `reason`,
  `serial_no`, `trade_time`, `account_opening_status`, `account_opening_trade_time`,
  `biz_status`, `account_opening_serial_no`, `creator`, `create_time`, `updater`,
  `update_time`, `deleted`
) VALUES (
  @ID, @TENANT_ID, @CUSTOMER_NAME, '0684191793', '06841917930600', '1454563280604499968',
  @CUSTOMER_NAME, NULL, 0.00000000, 0.00000000, 0, NULL,
  NULL, NULL, 1, '2025-12-27',
  0, '94f331a2a2ed4dd0a79ab62aaef01eba', NULL, NOW(), NULL, NOW(), b'0'
);

SET @CUSTOMER_NAME = '广州狮岭皮革皮具产业研究中心有限公司';
SET @TENANT_ID = (SELECT id FROM broker4operate_v2.opt_tenant WHERE `name` = @CUSTOMER_NAME);

SET @ID = @ID + 1;
INSERT INTO `broker4operate_wallet`.`citic_account_sub` (
  `id`, `tenant_id`, `customer_name`, `cust_no`, `settl_acc`, `pay_appl_id`,
  `account_name`, `account_no`, `amount`, `logic_balance`, `status`, `reason`,
  `serial_no`, `trade_time`, `account_opening_status`, `account_opening_trade_time`,
  `biz_status`, `account_opening_serial_no`, `creator`, `create_time`, `updater`,
  `update_time`, `deleted`
) VALUES (
  @ID, @TENANT_ID, @CUSTOMER_NAME, '3083333676', '30833336760600', '1454563283012030464',
  @CUSTOMER_NAME, NULL, 0.00000000, 0.00000000, 0, NULL,
  NULL, NULL, 1, '2025-12-27',
  0, 'f62548f473554eb2b6e6abefce478b21', NULL, NOW(), NULL, NOW(), b'0'
);

SET @CUSTOMER_NAME = '旭力欧（重庆）商贸有限公司';
SET @TENANT_ID = (SELECT id FROM broker4operate_v2.opt_tenant WHERE `name` = @CUSTOMER_NAME);

SET @ID = @ID + 1;
INSERT INTO `broker4operate_wallet`.`citic_account_sub` (
  `id`, `tenant_id`, `customer_name`, `cust_no`, `settl_acc`, `pay_appl_id`,
  `account_name`, `account_no`, `amount`, `logic_balance`, `status`, `reason`,
  `serial_no`, `trade_time`, `account_opening_status`, `account_opening_trade_time`,
  `biz_status`, `account_opening_serial_no`, `creator`, `create_time`, `updater`,
  `update_time`, `deleted`
) VALUES (
  @ID, @TENANT_ID, @CUSTOMER_NAME, '5528612945', '55286129450600', '1454563285461504000',
  @CUSTOMER_NAME, NULL, 0.00000000, 0.00000000, 0, NULL,
  NULL, NULL, 1, '2025-12-27',
  0, 'b72e2942750b4c1c9677484920d468db', NULL, NOW(), NULL, NOW(), b'0'
);

SET @CUSTOMER_NAME = '竞采科技有限公司';
SET @TENANT_ID = (SELECT id FROM broker4operate_v2.opt_tenant WHERE `name` = @CUSTOMER_NAME);

SET @ID = @ID + 1;
INSERT INTO `broker4operate_wallet`.`citic_account_sub` (
  `id`, `tenant_id`, `customer_name`, `cust_no`, `settl_acc`, `pay_appl_id`,
  `account_name`, `account_no`, `amount`, `logic_balance`, `status`, `reason`,
  `serial_no`, `trade_time`, `account_opening_status`, `account_opening_trade_time`,
  `biz_status`, `account_opening_serial_no`, `creator`, `create_time`, `updater`,
  `update_time`, `deleted`
) VALUES (
  @ID, @TENANT_ID, @CUSTOMER_NAME, '7986475022', '79864750220600', '1454563287915171840',
  @CUSTOMER_NAME, NULL, 0.00000000, 0.00000000, 0, NULL,
  NULL, NULL, 1, '2025-12-27',
  0, 'a709662a554a46fc90f9bebe9cd1f520', NULL, NOW(), NULL, NOW(), b'0'
);
