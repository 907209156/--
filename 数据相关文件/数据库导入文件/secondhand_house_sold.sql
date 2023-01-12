-- MySQL dump 10.13  Distrib 5.1.73, for redhat-linux-gnu (x86_64)
--
-- Host: localhost    Database: secondhand_house_sold
-- ------------------------------------------------------
-- Server version	5.1.73

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `area_sold_info`
--

DROP TABLE IF EXISTS `area_sold_info`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `area_sold_info` (
  `area` varchar(20) DEFAULT NULL,
  `count` int(8) DEFAULT NULL,
  `ratio` decimal(3,2) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `area_sold_info`
--

LOCK TABLES `area_sold_info` WRITE;
/*!40000 ALTER TABLE `area_sold_info` DISABLE KEYS */;
INSERT INTO `area_sold_info` VALUES ('西城',2976,'0.08'),('通州',2968,'0.07'),('门头沟',2937,'0.07'),('顺义',2961,'0.07'),('东城',2982,'0.08'),('丰台',2956,'0.07'),('亦庄开发区',2967,'0.07'),('大兴',2946,'0.07'),('密云',725,'0.02'),('平谷',48,'0.00'),('延庆',37,'0.00'),('怀柔',179,'0.00'),('房山',2922,'0.07'),('昌平',2973,'0.08'),('朝阳',2960,'0.07'),('海淀',2968,'0.07'),('石景山',3070,'0.08');
/*!40000 ALTER TABLE `area_sold_info` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `decoration_sold_info`
--

DROP TABLE IF EXISTS `decoration_sold_info`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `decoration_sold_info` (
  `decoration` varchar(10) DEFAULT NULL,
  `count` int(8) DEFAULT NULL,
  `ratio` decimal(3,2) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `decoration_sold_info`
--

LOCK TABLES `decoration_sold_info` WRITE;
/*!40000 ALTER TABLE `decoration_sold_info` DISABLE KEYS */;
INSERT INTO `decoration_sold_info` VALUES ('精装',20379,'0.51'),('简装',14999,'0.38'),('其他',3343,'0.08'),('毛坯',854,'0.02');
/*!40000 ALTER TABLE `decoration_sold_info` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `floor_sold_info`
--

DROP TABLE IF EXISTS `floor_sold_info`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `floor_sold_info` (
  `floor` varchar(10) DEFAULT NULL,
  `count` int(8) DEFAULT NULL,
  `ratio` decimal(3,2) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `floor_sold_info`
--

LOCK TABLES `floor_sold_info` WRITE;
/*!40000 ALTER TABLE `floor_sold_info` DISABLE KEYS */;
INSERT INTO `floor_sold_info` VALUES ('中楼层',15531,'0.39'),('低楼层',7625,'0.19'),('地下室',209,'0.01'),('高楼层',8297,'0.21'),('底层',3770,'0.10'),('顶层',4143,'0.10');
/*!40000 ALTER TABLE `floor_sold_info` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `house_type_sold_info`
--

DROP TABLE IF EXISTS `house_type_sold_info`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `house_type_sold_info` (
  `house_type` varchar(10) DEFAULT NULL,
  `count` int(8) DEFAULT NULL,
  `ratio` decimal(3,2) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `house_type_sold_info`
--

LOCK TABLES `house_type_sold_info` WRITE;
/*!40000 ALTER TABLE `house_type_sold_info` DISABLE KEYS */;
INSERT INTO `house_type_sold_info` VALUES ('板塔结合',6053,'0.15'),('板楼',25886,'0.65'),('塔楼',7367,'0.19');
/*!40000 ALTER TABLE `house_type_sold_info` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `is_near_subway_sold_info`
--

DROP TABLE IF EXISTS `is_near_subway_sold_info`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `is_near_subway_sold_info` (
  `is_near_subway` varchar(10) DEFAULT NULL,
  `count` int(8) DEFAULT NULL,
  `ratio` decimal(3,2) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `is_near_subway_sold_info`
--

LOCK TABLES `is_near_subway_sold_info` WRITE;
/*!40000 ALTER TABLE `is_near_subway_sold_info` DISABLE KEYS */;
INSERT INTO `is_near_subway_sold_info` VALUES ('FALSE',22136,'0.56'),('TRUE',17439,'0.44');
/*!40000 ALTER TABLE `is_near_subway_sold_info` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `layout_sold_info`
--

DROP TABLE IF EXISTS `layout_sold_info`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `layout_sold_info` (
  `layout` varchar(20) DEFAULT NULL,
  `count` int(8) DEFAULT NULL,
  `ratio` decimal(3,2) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `layout_sold_info`
--

LOCK TABLES `layout_sold_info` WRITE;
/*!40000 ALTER TABLE `layout_sold_info` DISABLE KEYS */;
INSERT INTO `layout_sold_info` VALUES ('3室1厅',5402,'0.14'),('3室2厅',2898,'0.07'),('3房间1卫',345,'0.01'),('1室0厅',1326,'0.03'),('1室1厅',6298,'0.16'),('1房间1卫',386,'0.01'),('3房间2卫',223,'0.01'),('4室1厅',258,'0.01'),('4室2厅',708,'0.02'),('2室1厅',17946,'0.45'),('2室2厅',2108,'0.05'),('2房间1卫',557,'0.01');
/*!40000 ALTER TABLE `layout_sold_info` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `orientation_sold_info`
--

DROP TABLE IF EXISTS `orientation_sold_info`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `orientation_sold_info` (
  `orientation` varchar(20) DEFAULT NULL,
  `count` int(8) DEFAULT NULL,
  `ratio` decimal(3,2) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `orientation_sold_info`
--

LOCK TABLES `orientation_sold_info` WRITE;
/*!40000 ALTER TABLE `orientation_sold_info` DISABLE KEYS */;
INSERT INTO `orientation_sold_info` VALUES ('西',1473,'0.04'),('西北',655,'0.02'),('西南',1441,'0.04'),('东 西',1494,'0.04'),('东北',591,'0.01'),('东南',1592,'0.04'),('北',944,'0.02'),('北 南',333,'0.01'),('东',1766,'0.04'),('东 北',251,'0.01'),('东 南',256,'0.01'),('东 南 北',494,'0.01'),('南',7530,'0.19'),('南 北',18532,'0.47'),('南 西',274,'0.01'),('南 西 北',422,'0.01');
/*!40000 ALTER TABLE `orientation_sold_info` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `size_sold_info`
--

DROP TABLE IF EXISTS `size_sold_info`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `size_sold_info` (
  `size_section` varchar(10) DEFAULT NULL,
  `count` int(8) DEFAULT NULL,
  `ratio` decimal(3,2) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `size_sold_info`
--

LOCK TABLES `size_sold_info` WRITE;
/*!40000 ALTER TABLE `size_sold_info` DISABLE KEYS */;
INSERT INTO `size_sold_info` VALUES ('<50',4843,'0.12'),('50-70',12149,'0.31'),('>150',2038,'0.05'),('110-130',2601,'0.07'),('130-150',1753,'0.04'),('70-90',10236,'0.26'),('90-110',5909,'0.15');
/*!40000 ALTER TABLE `size_sold_info` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-01-10 18:23:51
