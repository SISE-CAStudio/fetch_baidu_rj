-- --------------------------------------------------------
-- 主机:                           127.0.0.1
-- 服务器版本:                        5.5.32 - MySQL Community Server (GPL)
-- 服务器操作系统:                      Win32
-- HeidiSQL 版本:                  8.3.0.4694
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;

-- 导出 rjbaidu 的数据库结构
CREATE DATABASE IF NOT EXISTS `rjbaidu` /*!40100 DEFAULT CHARACTER SET utf8 COLLATE utf8_unicode_ci */;
USE `rjbaidu`;


-- 导出  表 rjbaidu.info 结构
CREATE TABLE IF NOT EXISTS `info` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `softname` varchar(50) COLLATE utf8_unicode_ci DEFAULT NULL COMMENT '软件名称',
  `classify` varchar(50) COLLATE utf8_unicode_ci DEFAULT NULL COMMENT '软件分类',
  `softpic` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL COMMENT '软件图片',
  `version` varchar(50) COLLATE utf8_unicode_ci DEFAULT NULL COMMENT '软件版本',
  `size` varchar(50) COLLATE utf8_unicode_ci DEFAULT NULL COMMENT '文件大小',
  `downloadlink` text COLLATE utf8_unicode_ci COMMENT '百度的下载链接',
  `website` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL COMMENT '软件官网',
  `introduction` text COLLATE utf8_unicode_ci COMMENT '功能简介',
  `whatisnew` text COLLATE utf8_unicode_ci COMMENT '新版特征',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- 正在导出表  rjbaidu.info 的数据：~0 rows (大约)
DELETE FROM `info`;
/*!40000 ALTER TABLE `info` DISABLE KEYS */;
/*!40000 ALTER TABLE `info` ENABLE KEYS */;
/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IF(@OLD_FOREIGN_KEY_CHECKS IS NULL, 1, @OLD_FOREIGN_KEY_CHECKS) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
