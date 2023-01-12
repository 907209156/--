以下是对所有文档的介绍
House：使用python语言编写的北京市租售房屋数据可视化平台的后端项目，app.py文件里面包含了所有将在前端用到的数据接口。

pythonProjectReptil:使用python语言编写的爬虫项目，用于爬取链家网的租房数据。
	crawler.py文件用于爬取北京市租房数据
	ershoufang_onsale.py文件用于爬取北京市在售二手房数据
	ershoufang_sold.py文件用于爬取北京市已售二手房数据


数据相关文件：
	爬虫原始数据：
		house.csv:北京市出租房源的相关数据
		second_hand_house_online.csv:北京市在售二手房源的相关数据
		second_hand_house_sold.csv:北京市已售二手房源的相关数据
	数据库导入文件：
		house.sql：根据北京出租房源源数据进行分析所得到的数据表组成的数据库导入文件
		secondhand_house_onsale.sql：根据北京在售二手房源源数据进行分析所得到的数据表组成的数据库导入文件
		secondhand_house_sold.sql：根据北京已售二手房源源数据进行分析所得到的数据表组成的数据库导入文件
	数据相关接口文档：分别是租房、在售二手房、已售二手房相关数据所对应的结构和接口简介

secondhand_sold_location.csv:根据爬到的已售二手房的地址数据，调用高德api获取的geojson格式的经纬度位置数据文件

