-- MySQL dump 10.13  Distrib 5.1.73, for redhat-linux-gnu (x86_64)
--
-- Host: localhost    Database: secondhand_house_onsale
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
-- Table structure for table `area_info`
--

DROP TABLE IF EXISTS `area_info`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `area_info` (
  `area` varchar(20) DEFAULT NULL,
  `count` int(11) DEFAULT NULL,
  `max_price` int(11) DEFAULT NULL,
  `min_price` int(11) DEFAULT NULL,
  `avg_price` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `area_info`
--

LOCK TABLES `area_info` WRITE;
/*!40000 ALTER TABLE `area_info` DISABLE KEYS */;
INSERT INTO `area_info` VALUES ('东城',2994,180000,14867,113107),('丰台',3000,154009,15021,61700),('亦庄开发区',1011,179992,3724,55866),('大兴',2995,141083,11036,43668),('西城',3000,179970,26696,127344),('通州',3000,120790,12202,44282),('门头沟',1554,114850,5881,37840),('顺义',2999,124481,10385,39369),('昌平',2995,148458,13832,45999),('朝阳',3000,177888,17202,72383),('海淀',2997,179921,27159,100300),('石景山',2563,148255,7759,52012),('密云',2960,73747,8603,23235),('平谷',69,56796,13946,23511),('延庆',70,60490,8680,23407),('怀柔',1396,98118,5292,30287),('房山',2981,97165,9856,30177);
/*!40000 ALTER TABLE `area_info` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `decoration_info`
--

DROP TABLE IF EXISTS `decoration_info`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `decoration_info` (
  `decoration` varchar(5) DEFAULT NULL,
  `count` int(11) DEFAULT NULL,
  `ratio` decimal(3,2) DEFAULT NULL,
  `max_price` int(11) DEFAULT NULL,
  `min_price` int(11) DEFAULT NULL,
  `avg_price` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `decoration_info`
--

LOCK TABLES `decoration_info` WRITE;
/*!40000 ALTER TABLE `decoration_info` DISABLE KEYS */;
INSERT INTO `decoration_info` VALUES ('其他',5190,'0.13',179936,9859,55034),('毛坯',1351,'0.03',179931,8952,47891),('简装',14138,'0.36',180000,8603,59782),('精装',18839,'0.48',179992,8993,63667);
/*!40000 ALTER TABLE `decoration_info` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `floor_info`
--

DROP TABLE IF EXISTS `floor_info`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `floor_info` (
  `floor` varchar(20) DEFAULT NULL,
  `count` int(11) DEFAULT NULL,
  `ratio` decimal(3,2) DEFAULT NULL,
  `max_price` int(11) DEFAULT NULL,
  `min_price` int(11) DEFAULT NULL,
  `avg_price` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `floor_info`
--

LOCK TABLES `floor_info` WRITE;
/*!40000 ALTER TABLE `floor_info` DISABLE KEYS */;
INSERT INTO `floor_info` VALUES ('顶层',4965,'0.13',179970,8603,60474),('底层',3757,'0.09',180000,10379,64082),('中楼层',10248,'0.26',179896,9100,63756),('低楼层',5628,'0.14',179925,11173,65669),('高楼层',6335,'0.16',179966,8993,62791);
/*!40000 ALTER TABLE `floor_info` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `is_near_subway_info`
--

DROP TABLE IF EXISTS `is_near_subway_info`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `is_near_subway_info` (
  `is_near_subway` varchar(10) DEFAULT NULL,
  `count` int(11) DEFAULT NULL,
  `ratio` decimal(3,2) DEFAULT NULL,
  `max_price` int(11) DEFAULT NULL,
  `min_price` int(11) DEFAULT NULL,
  `avg_price` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `is_near_subway_info`
--

LOCK TABLES `is_near_subway_info` WRITE;
/*!40000 ALTER TABLE `is_near_subway_info` DISABLE KEYS */;
INSERT INTO `is_near_subway_info` VALUES ('TRUE',15451,'0.39',180000,3724,78834),('FALSE',24133,'0.61',179925,5190,48804);
/*!40000 ALTER TABLE `is_near_subway_info` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `layout_info`
--

DROP TABLE IF EXISTS `layout_info`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `layout_info` (
  `layout` varchar(20) DEFAULT NULL,
  `count` int(11) DEFAULT NULL,
  `ratio` decimal(3,2) DEFAULT NULL,
  `max_price` int(11) DEFAULT NULL,
  `min_price` int(11) DEFAULT NULL,
  `avg_price` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `layout_info`
--

LOCK TABLES `layout_info` WRITE;
/*!40000 ALTER TABLE `layout_info` DISABLE KEYS */;
INSERT INTO `layout_info` VALUES ('5室4厅',31,'0.00',126985,22964,51521),('5室5厅',5,'0.00',108495,27881,51468),('5室6厅',3,'0.00',101681,41583,61615),('5房间1卫',6,'0.00',76829,22755,40757),('5房间2卫',35,'0.00',64218,14694,38487),('5房间3卫',20,'0.00',125298,32164,45160),('5房间4卫',6,'0.00',35122,27005,32697),('6室1厅',30,'0.00',179907,10196,57454),('6室2厅',199,'0.01',154658,9856,48641),('6室3厅',138,'0.00',159353,12825,56359),('6室4厅',31,'0.00',104398,21836,56996),('6室5厅',9,'0.00',86123,29151,61089),('6室6厅',1,'0.00',29127,29127,29127),('6房间1卫',2,'0.00',44997,40555,42776),('6房间2卫',5,'0.00',48589,33596,41042),('6房间3卫',8,'0.00',56064,32315,40214),('6房间4卫',3,'0.00',44475,19379,34184),('6房间5卫',1,'0.00',52460,52460,52460),('7室0厅',2,'0.00',155968,26107,91037),('7室1厅',10,'0.00',117301,19642,56034),('7室2厅',56,'0.00',157069,15138,52562),('0室0厅',1,'0.00',38744,38744,38744),('0房间0卫',2,'0.00',34639,17005,25822),('10室2厅',3,'0.00',90482,32627,68458),('10室3厅',3,'0.00',81662,52571,62268),('10室5厅',3,'0.00',142308,42320,75649),('12室3厅',2,'0.00',77373,77373,77373),('12室4厅',1,'0.00',119498,119498,119498),('1室0厅',654,'0.02',180000,15798,72210),('1室1厅',3942,'0.10',179970,9563,71893),('1室2厅',92,'0.00',172911,13079,56085),('1房间0卫',6,'0.00',46891,17202,30643),('1房间1卫',76,'0.00',42986,10385,25216),('1房间2卫',1,'0.00',34414,34414,34414),('2室0厅',65,'0.00',170308,20468,93346),('2室1厅',14202,'0.36',179966,9100,63611),('2室2厅',2430,'0.06',179373,10037,51192),('2室3厅',13,'0.00',175942,17426,79810),('2房间1卫',183,'0.00',66277,11664,30332),('2房间2卫',35,'0.00',60038,16534,37562),('3室0厅',26,'0.00',167598,26473,96613),('3室1厅',6218,'0.16',179948,8680,64144),('3室2厅',5573,'0.14',179955,8603,51418),('7室3厅',34,'0.00',160223,24002,56062),('7室4厅',14,'0.00',128618,23753,66541),('7室5厅',7,'0.00',121431,41635,64455),('7室6厅',3,'0.00',57239,50788,55088),('7房间4卫',1,'0.00',31131,31131,31131),('8室1厅',2,'0.00',48274,30710,39492),('8室2厅',21,'0.00',119531,19626,43256),('8室3厅',18,'0.00',165475,29244,72513),('8室4厅',9,'0.00',154266,29282,56735),('8室5厅',5,'0.00',79669,44468,66660),('8室6厅',1,'0.00',36823,36823,36823),('8室7厅',1,'0.00',102384,102384,102384),('8室8厅',2,'0.00',30001,30001,30001),('8房间3卫',1,'0.00',40986,40986,40986),('9室1厅',1,'0.00',62952,62952,62952),('9室2厅',12,'0.00',87345,37084,54336),('9室3厅',7,'0.00',95332,31281,51478),('9室4厅',6,'0.00',63990,28527,54944),('9室5厅',2,'0.00',67386,60858,64122),('9室6厅',1,'0.00',47351,47351,47351),('9室7厅',3,'0.00',120524,30443,60470),('车位',66,'0.00',77947,3724,13692),('3室3厅',119,'0.00',172536,17174,60670),('3室4厅',5,'0.00',80252,30366,54172),('3房间0卫',4,'0.00',82528,28967,69137),('3房间1卫',173,'0.00',56371,12161,27733),('3房间2卫',114,'0.00',65076,21508,37106),('3房间3卫',1,'0.00',26456,26456,26456),('4室0厅',4,'0.00',132108,97257,116373),('4室1厅',578,'0.01',179658,11548,60577),('4室2厅',2382,'0.06',178168,9898,58182),('4室3厅',299,'0.01',166946,12258,54535),('4室4厅',25,'0.00',105221,19334,54440),('4室6厅',1,'0.00',30760,30760,30760),('4室9厅',1,'0.00',154009,154009,154009),('4房间0卫',1,'0.00',30166,30166,30166),('4房间1卫',44,'0.00',85335,12693,30051),('4房间2卫',87,'0.00',78009,11036,37459),('4房间3卫',16,'0.00',62600,34414,42776),('5室0厅',2,'0.00',35686,35686,35686),('5室1厅',130,'0.00',150200,17963,48780),('5室2厅',894,'0.02',179992,10706,53549),('5室3厅',355,'0.01',178194,11559,52659);
/*!40000 ALTER TABLE `layout_info` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `orientation_info`
--

DROP TABLE IF EXISTS `orientation_info`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `orientation_info` (
  `orientation` varchar(20) DEFAULT NULL,
  `count` int(11) DEFAULT NULL,
  `ratio` decimal(3,2) DEFAULT NULL,
  `max_price` int(11) DEFAULT NULL,
  `min_price` int(11) DEFAULT NULL,
  `avg_price` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `orientation_info`
--

LOCK TABLES `orientation_info` WRITE;
/*!40000 ALTER TABLE `orientation_info` DISABLE KEYS */;
INSERT INTO `orientation_info` VALUES ('北 南',483,'0.01',179966,10310,48002),('南',4846,'0.12',179931,5881,65629),('南 北',22430,'0.57',179992,3724,53526),('南 西',206,'0.01',178295,12960,71508),('南 西 北',456,'0.01',179907,20399,69808),('西',1020,'0.03',179921,5026,72382),('西北',558,'0.01',170454,16715,73296),('西南',1184,'0.03',179966,13308,72840),('东',1220,'0.03',179927,7818,76640),('东 北',225,'0.01',179390,14444,72362),('东 南',224,'0.01',166341,14981,67150),('东 南 北',578,'0.01',179621,13704,66876),('东 南 西 北',235,'0.01',165475,17442,56446),('东 西',1627,'0.04',179948,10471,71968),('东北',514,'0.01',177831,11036,73853),('东南',1349,'0.03',176548,12161,74501),('北',620,'0.02',180000,5190,71230);
/*!40000 ALTER TABLE `orientation_info` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `size_info`
--

DROP TABLE IF EXISTS `size_info`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `size_info` (
  `size_section` varchar(10) DEFAULT NULL,
  `count` int(11) DEFAULT NULL,
  `ratio` decimal(3,2) DEFAULT NULL,
  `max_price` int(11) DEFAULT NULL,
  `min_price` int(11) DEFAULT NULL,
  `avg_price` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `size_info`
--

LOCK TABLES `size_info` WRITE;
/*!40000 ALTER TABLE `size_info` DISABLE KEYS */;
INSERT INTO `size_info` VALUES ('110-130',3862,'0.10',179925,8680,53042),('90-110',5942,'0.15',179894,8939,53059),('50-70',9086,'0.23',179970,10385,71671),('70-90',8454,'0.21',179948,9563,56707),('<50',2500,'0.06',180000,3724,77872),('>150',6501,'0.16',179992,8603,57227),('130-150',3209,'0.08',179955,9534,54817);
/*!40000 ALTER TABLE `size_info` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-01-10 17:52:34
