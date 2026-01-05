-- 初始化最大ID和桶名
SET @ID = (SELECT MAX(id) FROM broker4infra.file_attachment);
SET @BUCKET_NAME = "broker-cloud-pre-server";

-- 原始文件 cb1bb0ba3fe14145b917edf09e065f23.pdf → fRKJ15XOVb.pdf | ownership = 1
SET @FILE_1_1 = (@ID := @ID + 1);
SET @FILE_NAME = 'fRKJ15XOVb.pdf';
SET @BANK_SERIAL_NO = '1453062851479605248';
INSERT INTO `broker4infra`.`file_attachment` (`id`, `name`, `path`, `url`, `type`, `size`, `creator`, `create_time`, `updater`, `update_time`, `deleted`, `status`, `bucket_name`) VALUES (@FILE_1_1, @FILE_NAME, 'rgst-bank-receipt/202512/' + @FILE_NAME, 'https://broker-cloud-pre-server.obs.cn-south-1.myhuaweicloud.com:443/rgst-bank-receipt/202512/' + @FILE_NAME + '?AccessKeyId=SGHTWJV6RZGRUYH706N9&Expires=1766509248&Signature=ekvKW2UznDzMQ1JRE5rM1bI4gGI%3D', 'application/pdf', 102947, NULL, '2025-12-24 00:00:48', NULL, '2025-12-24 00:00:48', b'0', 0, @BUCKET_NAME);
UPDATE broker4settlement.transaction_flow_detail SET receipt_file_id = @FILE_1_1 WHERE bank_serial_no = @BANK_SERIAL_NO AND order_ownership = 1;

-- 副本 fD5xcoSPsw.pdf | ownership = 0
SET @FILE_1_2 = (@ID := @ID + 1);
SET @FILE_NAME = 'fD5xcoSPsw.pdf';
SET @BANK_SERIAL_NO = '1453062851479605248';
INSERT INTO `broker4infra`.`file_attachment` (`id`, `name`, `path`, `url`, `type`, `size`, `creator`, `create_time`, `updater`, `update_time`, `deleted`, `status`, `bucket_name`) VALUES (@FILE_1_2, @FILE_NAME, 'rgst-bank-receipt/202512/' + @FILE_NAME, 'https://broker-cloud-pre-server.obs.cn-south-1.myhuaweicloud.com:443/rgst-bank-receipt/202512/' + @FILE_NAME + '?AccessKeyId=SGHTWJV6RZGRUYH706N9&Expires=1766509248&Signature=ekvKW2UznDzMQ1JRE5rM1bI4gGI%3D', 'application/pdf', 102947, NULL, '2025-12-24 00:00:48', NULL, '2025-12-24 00:00:48', b'0', 0, @BUCKET_NAME);
UPDATE broker4settlement.transaction_flow_detail SET receipt_file_id = @FILE_1_2 WHERE bank_serial_no = @BANK_SERIAL_NO AND order_ownership = 0;

-- 原始文件 3687224b68c54efc883d53cad8574510.pdf → g8ZDfJtX5y.pdf | ownership = 1
SET @FILE_2_1 = (@ID := @ID + 1);
SET @FILE_NAME = 'g8ZDfJtX5y.pdf';
SET @BANK_SERIAL_NO = '1453032652549525505';
INSERT INTO `broker4infra`.`file_attachment` (`id`, `name`, `path`, `url`, `type`, `size`, `creator`, `create_time`, `updater`, `update_time`, `deleted`, `status`, `bucket_name`) VALUES (@FILE_2_1, @FILE_NAME, 'rgst-bank-receipt/202512/' + @FILE_NAME, 'https://broker-cloud-pre-server.obs.cn-south-1.myhuaweicloud.com:443/rgst-bank-receipt/202512/' + @FILE_NAME + '?AccessKeyId=SGHTWJV6RZGRUYH706N9&Expires=1766509248&Signature=ekvKW2UznDzMQ1JRE5rM1bI4gGI%3D', 'application/pdf', 102949, NULL, '2025-12-24 00:00:48', NULL, '2025-12-24 00:00:48', b'0', 0, @BUCKET_NAME);
UPDATE broker4settlement.transaction_flow_detail SET receipt_file_id = @FILE_2_1 WHERE bank_serial_no = @BANK_SERIAL_NO AND order_ownership = 1;

-- 副本 QwQ7HFugiq.pdf | ownership = 0
SET @FILE_2_2 = (@ID := @ID + 1);
SET @FILE_NAME = 'QwQ7HFugiq.pdf';
SET @BANK_SERIAL_NO = '1453032652549525505';
INSERT INTO `broker4infra`.`file_attachment` (`id`, `name`, `path`, `url`, `type`, `size`, `creator`, `create_time`, `updater`, `update_time`, `deleted`, `status`, `bucket_name`) VALUES (@FILE_2_2, @FILE_NAME, 'rgst-bank-receipt/202512/' + @FILE_NAME, 'https://broker-cloud-pre-server.obs.cn-south-1.myhuaweicloud.com:443/rgst-bank-receipt/202512/' + @FILE_NAME + '?AccessKeyId=SGHTWJV6RZGRUYH706N9&Expires=1766509248&Signature=ekvKW2UznDzMQ1JRE5rM1bI4gGI%3D', 'application/pdf', 102949, NULL, '2025-12-24 00:00:48', NULL, '2025-12-24 00:00:48', b'0', 0, @BUCKET_NAME);
UPDATE broker4settlement.transaction_flow_detail SET receipt_file_id = @FILE_2_2 WHERE bank_serial_no = @BANK_SERIAL_NO AND order_ownership = 0;

-- 原始文件 12268813dd514c9287af8ce3f4541f53.pdf → yPuke8jAfl.pdf | ownership = 1
SET @FILE_3_1 = (@ID := @ID + 1);
SET @FILE_NAME = 'yPuke8jAfl.pdf';
SET @BANK_SERIAL_NO = '1452676807433261056';
INSERT INTO `broker4infra`.`file_attachment` (`id`, `name`, `path`, `url`, `type`, `size`, `creator`, `create_time`, `updater`, `update_time`, `deleted`, `status`, `bucket_name`) VALUES (@FILE_3_1, @FILE_NAME, 'rgst-bank-receipt/202512/' + @FILE_NAME, 'https://broker-cloud-pre-server.obs.cn-south-1.myhuaweicloud.com:443/rgst-bank-receipt/202512/' + @FILE_NAME + '?AccessKeyId=SGHTWJV6RZGRUYH706N9&Expires=1766509248&Signature=ekvKW2UznDzMQ1JRE5rM1bI4gGI%3D', 'application/pdf', 103106, NULL, '2025-12-24 00:00:48', NULL, '2025-12-24 00:00:48', b'0', 0, @BUCKET_NAME);
UPDATE broker4settlement.transaction_flow_detail SET receipt_file_id = @FILE_3_1 WHERE bank_serial_no = @BANK_SERIAL_NO AND order_ownership = 1;

-- 副本 fXQwloTkKb.pdf | ownership = 0
SET @FILE_3_2 = (@ID := @ID + 1);
SET @FILE_NAME = 'fXQwloTkKb.pdf';
SET @BANK_SERIAL_NO = '1452676807433261056';
INSERT INTO `broker4infra`.`file_attachment` (`id`, `name`, `path`, `url`, `type`, `size`, `creator`, `create_time`, `updater`, `update_time`, `deleted`, `status`, `bucket_name`) VALUES (@FILE_3_2, @FILE_NAME, 'rgst-bank-receipt/202512/' + @FILE_NAME, 'https://broker-cloud-pre-server.obs.cn-south-1.myhuaweicloud.com:443/rgst-bank-receipt/202512/' + @FILE_NAME + '?AccessKeyId=SGHTWJV6RZGRUYH706N9&Expires=1766509248&Signature=ekvKW2UznDzMQ1JRE5rM1bI4gGI%3D', 'application/pdf', 103106, NULL, '2025-12-24 00:00:48', NULL, '2025-12-24 00:00:48', b'0', 0, @BUCKET_NAME);
UPDATE broker4settlement.transaction_flow_detail SET receipt_file_id = @FILE_3_2 WHERE bank_serial_no = @BANK_SERIAL_NO AND order_ownership = 0;
