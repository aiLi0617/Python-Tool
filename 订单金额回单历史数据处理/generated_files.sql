-- 初始化最大ID和桶名
SET @ID = (SELECT MAX(id) FROM broker4infra.file_attachment);
SET @BUCKET_NAME = "broker-cloud-prd-server";

-- 原始文件 b18db049d5a34a7d94ff1cc304cfa0d3.pdf → u2fi98JiEw.pdf | ownership = 1
SET @FILE_1_1 = (@ID := @ID + 1);
SET @FILE_NAME = 'u2fi98JiEw.pdf';
SET @BANK_SERIAL_NO = '1457375266916667392';
INSERT INTO `broker4infra`.`file_attachment` (`id`, `name`, `path`, `url`, `type`, `size`, `creator`, `create_time`, `updater`, `update_time`, `deleted`, `status`, `bucket_name`) VALUES (@FILE_1_1, @FILE_NAME, CONCAT('rgst-bank-receipt/202512/', @FILE_NAME), CONCAT('https://broker-cloud-prd-server.obs.cn-south-1.myhuaweicloud.com:443/rgst-bank-receipt/202512/', @FILE_NAME, '?AccessKeyId=SGHTWJV6RZGRUYH706N9&Expires=1766509248&Signature=ekvKW2UznDzMQ1JRE5rM1bI4gGI%3D'), 'application/pdf', 96612, NULL, '2025-12-24 00:00:48', NULL, '2025-12-24 00:00:48', b'0', 0, @BUCKET_NAME);
UPDATE broker4settlement.transaction_flow_detail SET receipt_file_id = @FILE_1_1 WHERE bank_serial_no = @BANK_SERIAL_NO AND order_ownership = 1;

-- 副本 I92q6rR4vh.pdf | ownership = 0
SET @FILE_1_2 = (@ID := @ID + 1);
SET @FILE_NAME = 'I92q6rR4vh.pdf';
SET @BANK_SERIAL_NO = '1457375266916667392';
INSERT INTO `broker4infra`.`file_attachment` (`id`, `name`, `path`, `url`, `type`, `size`, `creator`, `create_time`, `updater`, `update_time`, `deleted`, `status`, `bucket_name`) VALUES (@FILE_1_2, @FILE_NAME, CONCAT('rgst-bank-receipt/202512/', @FILE_NAME), CONCAT('https://broker-cloud-prd-server.obs.cn-south-1.myhuaweicloud.com:443/rgst-bank-receipt/202512/', @FILE_NAME, '?AccessKeyId=SGHTWJV6RZGRUYH706N9&Expires=1766509248&Signature=ekvKW2UznDzMQ1JRE5rM1bI4gGI%3D'), 'application/pdf', 96612, NULL, '2025-12-24 00:00:48', NULL, '2025-12-24 00:00:48', b'0', 0, @BUCKET_NAME);
UPDATE broker4settlement.transaction_flow_detail SET receipt_file_id = @FILE_1_2 WHERE bank_serial_no = @BANK_SERIAL_NO AND order_ownership = 0;

-- 原始文件 2e1cf3401b6f41aa8e1993f6a4a910f4.pdf → fpOTeDcFIu.pdf | ownership = 1
SET @FILE_2_1 = (@ID := @ID + 1);
SET @FILE_NAME = 'fpOTeDcFIu.pdf';
SET @BANK_SERIAL_NO = '1457375267671642112';
INSERT INTO `broker4infra`.`file_attachment` (`id`, `name`, `path`, `url`, `type`, `size`, `creator`, `create_time`, `updater`, `update_time`, `deleted`, `status`, `bucket_name`) VALUES (@FILE_2_1, @FILE_NAME, CONCAT('rgst-bank-receipt/202512/', @FILE_NAME), CONCAT('https://broker-cloud-prd-server.obs.cn-south-1.myhuaweicloud.com:443/rgst-bank-receipt/202512/', @FILE_NAME, '?AccessKeyId=SGHTWJV6RZGRUYH706N9&Expires=1766509248&Signature=ekvKW2UznDzMQ1JRE5rM1bI4gGI%3D'), 'application/pdf', 96610, NULL, '2025-12-24 00:00:48', NULL, '2025-12-24 00:00:48', b'0', 0, @BUCKET_NAME);
UPDATE broker4settlement.transaction_flow_detail SET receipt_file_id = @FILE_2_1 WHERE bank_serial_no = @BANK_SERIAL_NO AND order_ownership = 1;

-- 副本 reJGBxu807.pdf | ownership = 0
SET @FILE_2_2 = (@ID := @ID + 1);
SET @FILE_NAME = 'reJGBxu807.pdf';
SET @BANK_SERIAL_NO = '1457375267671642112';
INSERT INTO `broker4infra`.`file_attachment` (`id`, `name`, `path`, `url`, `type`, `size`, `creator`, `create_time`, `updater`, `update_time`, `deleted`, `status`, `bucket_name`) VALUES (@FILE_2_2, @FILE_NAME, CONCAT('rgst-bank-receipt/202512/', @FILE_NAME), CONCAT('https://broker-cloud-prd-server.obs.cn-south-1.myhuaweicloud.com:443/rgst-bank-receipt/202512/', @FILE_NAME, '?AccessKeyId=SGHTWJV6RZGRUYH706N9&Expires=1766509248&Signature=ekvKW2UznDzMQ1JRE5rM1bI4gGI%3D'), 'application/pdf', 96610, NULL, '2025-12-24 00:00:48', NULL, '2025-12-24 00:00:48', b'0', 0, @BUCKET_NAME);
UPDATE broker4settlement.transaction_flow_detail SET receipt_file_id = @FILE_2_2 WHERE bank_serial_no = @BANK_SERIAL_NO AND order_ownership = 0;

-- 原始文件 cac35e591fb243baa1e1096766ada0fe.pdf → cIOrBYzTm3.pdf | ownership = 1
SET @FILE_3_1 = (@ID := @ID + 1);
SET @FILE_NAME = 'cIOrBYzTm3.pdf';
SET @BANK_SERIAL_NO = '1457335001568907264';
INSERT INTO `broker4infra`.`file_attachment` (`id`, `name`, `path`, `url`, `type`, `size`, `creator`, `create_time`, `updater`, `update_time`, `deleted`, `status`, `bucket_name`) VALUES (@FILE_3_1, @FILE_NAME, CONCAT('rgst-bank-receipt/202512/', @FILE_NAME), CONCAT('https://broker-cloud-prd-server.obs.cn-south-1.myhuaweicloud.com:443/rgst-bank-receipt/202512/', @FILE_NAME, '?AccessKeyId=SGHTWJV6RZGRUYH706N9&Expires=1766509248&Signature=ekvKW2UznDzMQ1JRE5rM1bI4gGI%3D'), 'application/pdf', 92668, NULL, '2025-12-24 00:00:48', NULL, '2025-12-24 00:00:48', b'0', 0, @BUCKET_NAME);
UPDATE broker4settlement.transaction_flow_detail SET receipt_file_id = @FILE_3_1 WHERE bank_serial_no = @BANK_SERIAL_NO AND order_ownership = 1;

-- 副本 qbFR2C0XbT.pdf | ownership = 0
SET @FILE_3_2 = (@ID := @ID + 1);
SET @FILE_NAME = 'qbFR2C0XbT.pdf';
SET @BANK_SERIAL_NO = '1457335001568907264';
INSERT INTO `broker4infra`.`file_attachment` (`id`, `name`, `path`, `url`, `type`, `size`, `creator`, `create_time`, `updater`, `update_time`, `deleted`, `status`, `bucket_name`) VALUES (@FILE_3_2, @FILE_NAME, CONCAT('rgst-bank-receipt/202512/', @FILE_NAME), CONCAT('https://broker-cloud-prd-server.obs.cn-south-1.myhuaweicloud.com:443/rgst-bank-receipt/202512/', @FILE_NAME, '?AccessKeyId=SGHTWJV6RZGRUYH706N9&Expires=1766509248&Signature=ekvKW2UznDzMQ1JRE5rM1bI4gGI%3D'), 'application/pdf', 92668, NULL, '2025-12-24 00:00:48', NULL, '2025-12-24 00:00:48', b'0', 0, @BUCKET_NAME);
UPDATE broker4settlement.transaction_flow_detail SET receipt_file_id = @FILE_3_2 WHERE bank_serial_no = @BANK_SERIAL_NO AND order_ownership = 0;

-- 原始文件 de5ae7c6d54c49f7ae90e3a534ab7a61.pdf → R8dvkEs7gj.pdf | ownership = 1
SET @FILE_4_1 = (@ID := @ID + 1);
SET @FILE_NAME = 'R8dvkEs7gj.pdf';
SET @BANK_SERIAL_NO = '1455612150541324288';
INSERT INTO `broker4infra`.`file_attachment` (`id`, `name`, `path`, `url`, `type`, `size`, `creator`, `create_time`, `updater`, `update_time`, `deleted`, `status`, `bucket_name`) VALUES (@FILE_4_1, @FILE_NAME, CONCAT('rgst-bank-receipt/202512/', @FILE_NAME), CONCAT('https://broker-cloud-prd-server.obs.cn-south-1.myhuaweicloud.com:443/rgst-bank-receipt/202512/', @FILE_NAME, '?AccessKeyId=SGHTWJV6RZGRUYH706N9&Expires=1766509248&Signature=ekvKW2UznDzMQ1JRE5rM1bI4gGI%3D'), 'application/pdf', 97474, NULL, '2025-12-24 00:00:48', NULL, '2025-12-24 00:00:48', b'0', 0, @BUCKET_NAME);
UPDATE broker4settlement.transaction_flow_detail SET receipt_file_id = @FILE_4_1 WHERE bank_serial_no = @BANK_SERIAL_NO AND order_ownership = 1;

-- 副本 ZYy7hS8zfB.pdf | ownership = 0
SET @FILE_4_2 = (@ID := @ID + 1);
SET @FILE_NAME = 'ZYy7hS8zfB.pdf';
SET @BANK_SERIAL_NO = '1455612150541324288';
INSERT INTO `broker4infra`.`file_attachment` (`id`, `name`, `path`, `url`, `type`, `size`, `creator`, `create_time`, `updater`, `update_time`, `deleted`, `status`, `bucket_name`) VALUES (@FILE_4_2, @FILE_NAME, CONCAT('rgst-bank-receipt/202512/', @FILE_NAME), CONCAT('https://broker-cloud-prd-server.obs.cn-south-1.myhuaweicloud.com:443/rgst-bank-receipt/202512/', @FILE_NAME, '?AccessKeyId=SGHTWJV6RZGRUYH706N9&Expires=1766509248&Signature=ekvKW2UznDzMQ1JRE5rM1bI4gGI%3D'), 'application/pdf', 97474, NULL, '2025-12-24 00:00:48', NULL, '2025-12-24 00:00:48', b'0', 0, @BUCKET_NAME);
UPDATE broker4settlement.transaction_flow_detail SET receipt_file_id = @FILE_4_2 WHERE bank_serial_no = @BANK_SERIAL_NO AND order_ownership = 0;

-- 原始文件 efed4e0769aa43d5b176d70112033f19.pdf → zpDqiuBqHn.pdf | ownership = 1
SET @FILE_5_1 = (@ID := @ID + 1);
SET @FILE_NAME = 'zpDqiuBqHn.pdf';
SET @BANK_SERIAL_NO = '1455612151375990784';
INSERT INTO `broker4infra`.`file_attachment` (`id`, `name`, `path`, `url`, `type`, `size`, `creator`, `create_time`, `updater`, `update_time`, `deleted`, `status`, `bucket_name`) VALUES (@FILE_5_1, @FILE_NAME, CONCAT('rgst-bank-receipt/202512/', @FILE_NAME), CONCAT('https://broker-cloud-prd-server.obs.cn-south-1.myhuaweicloud.com:443/rgst-bank-receipt/202512/', @FILE_NAME, '?AccessKeyId=SGHTWJV6RZGRUYH706N9&Expires=1766509248&Signature=ekvKW2UznDzMQ1JRE5rM1bI4gGI%3D'), 'application/pdf', 97475, NULL, '2025-12-24 00:00:48', NULL, '2025-12-24 00:00:48', b'0', 0, @BUCKET_NAME);
UPDATE broker4settlement.transaction_flow_detail SET receipt_file_id = @FILE_5_1 WHERE bank_serial_no = @BANK_SERIAL_NO AND order_ownership = 1;

-- 副本 u6OJLu3O26.pdf | ownership = 0
SET @FILE_5_2 = (@ID := @ID + 1);
SET @FILE_NAME = 'u6OJLu3O26.pdf';
SET @BANK_SERIAL_NO = '1455612151375990784';
INSERT INTO `broker4infra`.`file_attachment` (`id`, `name`, `path`, `url`, `type`, `size`, `creator`, `create_time`, `updater`, `update_time`, `deleted`, `status`, `bucket_name`) VALUES (@FILE_5_2, @FILE_NAME, CONCAT('rgst-bank-receipt/202512/', @FILE_NAME), CONCAT('https://broker-cloud-prd-server.obs.cn-south-1.myhuaweicloud.com:443/rgst-bank-receipt/202512/', @FILE_NAME, '?AccessKeyId=SGHTWJV6RZGRUYH706N9&Expires=1766509248&Signature=ekvKW2UznDzMQ1JRE5rM1bI4gGI%3D'), 'application/pdf', 97475, NULL, '2025-12-24 00:00:48', NULL, '2025-12-24 00:00:48', b'0', 0, @BUCKET_NAME);
UPDATE broker4settlement.transaction_flow_detail SET receipt_file_id = @FILE_5_2 WHERE bank_serial_no = @BANK_SERIAL_NO AND order_ownership = 0;

-- 原始文件 1a09ea5eace5471ea94b14077515ecb2.pdf → XKDrkTgLix.pdf | ownership = 1
SET @FILE_6_1 = (@ID := @ID + 1);
SET @FILE_NAME = 'XKDrkTgLix.pdf';
SET @BANK_SERIAL_NO = '1455612152135159808';
INSERT INTO `broker4infra`.`file_attachment` (`id`, `name`, `path`, `url`, `type`, `size`, `creator`, `create_time`, `updater`, `update_time`, `deleted`, `status`, `bucket_name`) VALUES (@FILE_6_1, @FILE_NAME, CONCAT('rgst-bank-receipt/202512/', @FILE_NAME), CONCAT('https://broker-cloud-prd-server.obs.cn-south-1.myhuaweicloud.com:443/rgst-bank-receipt/202512/', @FILE_NAME, '?AccessKeyId=SGHTWJV6RZGRUYH706N9&Expires=1766509248&Signature=ekvKW2UznDzMQ1JRE5rM1bI4gGI%3D'), 'application/pdf', 97474, NULL, '2025-12-24 00:00:48', NULL, '2025-12-24 00:00:48', b'0', 0, @BUCKET_NAME);
UPDATE broker4settlement.transaction_flow_detail SET receipt_file_id = @FILE_6_1 WHERE bank_serial_no = @BANK_SERIAL_NO AND order_ownership = 1;

-- 副本 z5CwoZdv8T.pdf | ownership = 0
SET @FILE_6_2 = (@ID := @ID + 1);
SET @FILE_NAME = 'z5CwoZdv8T.pdf';
SET @BANK_SERIAL_NO = '1455612152135159808';
INSERT INTO `broker4infra`.`file_attachment` (`id`, `name`, `path`, `url`, `type`, `size`, `creator`, `create_time`, `updater`, `update_time`, `deleted`, `status`, `bucket_name`) VALUES (@FILE_6_2, @FILE_NAME, CONCAT('rgst-bank-receipt/202512/', @FILE_NAME), CONCAT('https://broker-cloud-prd-server.obs.cn-south-1.myhuaweicloud.com:443/rgst-bank-receipt/202512/', @FILE_NAME, '?AccessKeyId=SGHTWJV6RZGRUYH706N9&Expires=1766509248&Signature=ekvKW2UznDzMQ1JRE5rM1bI4gGI%3D'), 'application/pdf', 97474, NULL, '2025-12-24 00:00:48', NULL, '2025-12-24 00:00:48', b'0', 0, @BUCKET_NAME);
UPDATE broker4settlement.transaction_flow_detail SET receipt_file_id = @FILE_6_2 WHERE bank_serial_no = @BANK_SERIAL_NO AND order_ownership = 0;

-- 原始文件 e5ec21dfef8a41c5b6c01507741d1d85.pdf → Cly2o04PFf.pdf | ownership = 1
SET @FILE_7_1 = (@ID := @ID + 1);
SET @FILE_NAME = 'Cly2o04PFf.pdf';
SET @BANK_SERIAL_NO = '1455612152923688960';
INSERT INTO `broker4infra`.`file_attachment` (`id`, `name`, `path`, `url`, `type`, `size`, `creator`, `create_time`, `updater`, `update_time`, `deleted`, `status`, `bucket_name`) VALUES (@FILE_7_1, @FILE_NAME, CONCAT('rgst-bank-receipt/202512/', @FILE_NAME), CONCAT('https://broker-cloud-prd-server.obs.cn-south-1.myhuaweicloud.com:443/rgst-bank-receipt/202512/', @FILE_NAME, '?AccessKeyId=SGHTWJV6RZGRUYH706N9&Expires=1766509248&Signature=ekvKW2UznDzMQ1JRE5rM1bI4gGI%3D'), 'application/pdf', 97479, NULL, '2025-12-24 00:00:48', NULL, '2025-12-24 00:00:48', b'0', 0, @BUCKET_NAME);
UPDATE broker4settlement.transaction_flow_detail SET receipt_file_id = @FILE_7_1 WHERE bank_serial_no = @BANK_SERIAL_NO AND order_ownership = 1;

-- 副本 KRc6ac6ftm.pdf | ownership = 0
SET @FILE_7_2 = (@ID := @ID + 1);
SET @FILE_NAME = 'KRc6ac6ftm.pdf';
SET @BANK_SERIAL_NO = '1455612152923688960';
INSERT INTO `broker4infra`.`file_attachment` (`id`, `name`, `path`, `url`, `type`, `size`, `creator`, `create_time`, `updater`, `update_time`, `deleted`, `status`, `bucket_name`) VALUES (@FILE_7_2, @FILE_NAME, CONCAT('rgst-bank-receipt/202512/', @FILE_NAME), CONCAT('https://broker-cloud-prd-server.obs.cn-south-1.myhuaweicloud.com:443/rgst-bank-receipt/202512/', @FILE_NAME, '?AccessKeyId=SGHTWJV6RZGRUYH706N9&Expires=1766509248&Signature=ekvKW2UznDzMQ1JRE5rM1bI4gGI%3D'), 'application/pdf', 97479, NULL, '2025-12-24 00:00:48', NULL, '2025-12-24 00:00:48', b'0', 0, @BUCKET_NAME);
UPDATE broker4settlement.transaction_flow_detail SET receipt_file_id = @FILE_7_2 WHERE bank_serial_no = @BANK_SERIAL_NO AND order_ownership = 0;

-- 原始文件 7e24ffca70c84318bcda190ea6da7ae2.pdf → V8U72ui8Xn.pdf | ownership = 1
SET @FILE_8_1 = (@ID := @ID + 1);
SET @FILE_NAME = 'V8U72ui8Xn.pdf';
SET @BANK_SERIAL_NO = '1455612153708023808';
INSERT INTO `broker4infra`.`file_attachment` (`id`, `name`, `path`, `url`, `type`, `size`, `creator`, `create_time`, `updater`, `update_time`, `deleted`, `status`, `bucket_name`) VALUES (@FILE_8_1, @FILE_NAME, CONCAT('rgst-bank-receipt/202512/', @FILE_NAME), CONCAT('https://broker-cloud-prd-server.obs.cn-south-1.myhuaweicloud.com:443/rgst-bank-receipt/202512/', @FILE_NAME, '?AccessKeyId=SGHTWJV6RZGRUYH706N9&Expires=1766509248&Signature=ekvKW2UznDzMQ1JRE5rM1bI4gGI%3D'), 'application/pdf', 97473, NULL, '2025-12-24 00:00:48', NULL, '2025-12-24 00:00:48', b'0', 0, @BUCKET_NAME);
UPDATE broker4settlement.transaction_flow_detail SET receipt_file_id = @FILE_8_1 WHERE bank_serial_no = @BANK_SERIAL_NO AND order_ownership = 1;

-- 副本 aZz3VhXpup.pdf | ownership = 0
SET @FILE_8_2 = (@ID := @ID + 1);
SET @FILE_NAME = 'aZz3VhXpup.pdf';
SET @BANK_SERIAL_NO = '1455612153708023808';
INSERT INTO `broker4infra`.`file_attachment` (`id`, `name`, `path`, `url`, `type`, `size`, `creator`, `create_time`, `updater`, `update_time`, `deleted`, `status`, `bucket_name`) VALUES (@FILE_8_2, @FILE_NAME, CONCAT('rgst-bank-receipt/202512/', @FILE_NAME), CONCAT('https://broker-cloud-prd-server.obs.cn-south-1.myhuaweicloud.com:443/rgst-bank-receipt/202512/', @FILE_NAME, '?AccessKeyId=SGHTWJV6RZGRUYH706N9&Expires=1766509248&Signature=ekvKW2UznDzMQ1JRE5rM1bI4gGI%3D'), 'application/pdf', 97473, NULL, '2025-12-24 00:00:48', NULL, '2025-12-24 00:00:48', b'0', 0, @BUCKET_NAME);
UPDATE broker4settlement.transaction_flow_detail SET receipt_file_id = @FILE_8_2 WHERE bank_serial_no = @BANK_SERIAL_NO AND order_ownership = 0;
