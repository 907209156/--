import requests
import uuid
import time
from bs4 import BeautifulSoup
import csv

def requestHtmlData():
    f = open("D://Desktop//second_hand_house_onsale.csv", 'a', newline='')  # 打开文件
    csv_writer = csv.writer(f, dialect='excel')  # 设置写入模式
    url = "https://bj.lianjia.com/ershoufang/dongcheng/pg{0}/"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.55 Safari/537.36 Edg/96.0.1054.43'
    }
    i = 1;
    while (1 == 1):
        rurl = url.replace("{0}", str(i))
        print("请求地址：" + rurl)
        i += 1
        if (i > 101):
            break
        resp = requests.get(rurl, headers=headers)

        html = resp.text
        soup = BeautifulSoup(html, 'html.parser')  # 解析
        # print (soup)
        infos = soup.findAll(class_='info clear')
        # print(infos)
        for info in infos:
            try:
                title = info.find(class_='title').find('a').get_text() #卖房标题 例如：东城区，南北通透两居，中间层采光好，商品房
                # print(title)

                area = '东城' #区域

                position_info = info.find(class_='positionInfo').findAll('a')
                position = position_info[0].get_text() #房源位置 例如：安乐林头条2号院 永定门
                for item in position_info[1:]:
                    position += item.get_text()
                # print(position)

                house_info = info.find(class_='houseInfo').get_text() #房源信息 例如：2室1厅 | 57.91平米 | 南 北 | 简装 | 中楼层(共6层) | 1989年建 | 板楼
                # print(house_info)

                house_info_list = house_info.split('|')
                layout = house_info_list[0].strip() #房型 例如：2室1厅
                size = house_info_list[1].strip()[:-2] #大小 例如：57.91  （单位是平米）
                orientation = house_info_list[2].strip()  # 朝向 例如：南 北
                decoration = house_info_list[3].strip()  #装修 例如：简装
                floor = house_info_list[4].strip().split('(')[0] #楼层 例如：中楼层(共6层)
                print(floor)

                subway_tag = info.find(class_='tag').find(class_='subway')
                near_subway = True #是否近地铁
                if subway_tag == None:
                    near_subway = False

                total_price = info.find(class_='totalPrice totalPrice2').find('span').get_text() #总价 例如：758 （单位是万元）
                unit_price_info = info.find(class_='unitPrice').find('span').get_text()[:-3].split(',')
                unit_price = unit_price_info[0] #单价 例如：80816 （单位是元/平）
                for item in unit_price_info[1:]:
                    unit_price += item
                # print(title, area, position, layout, size, decoration, floor, orientation,near_subway, total_price,unit_price)
                # hp = [title, area, position, layout, size, decoration, floor, orientation,near_subway, total_price,unit_price]
                # csv_writer.writerow(hp)  # 写入一行
            except Exception as e:
                print(e)
        print("睡眠3s")
        time.sleep(3)

if __name__ == '__main__':
    requestHtmlData()
    print("--------------爬取结束-------------")

