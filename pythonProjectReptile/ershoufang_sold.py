import requests
import uuid
import time
from bs4 import BeautifulSoup
import csv

def requestHtmlData():
    f = open("D://Desktop//second_hand_house_sold.csv", 'a', newline='')  # 打开文件
    csv_writer = csv.writer(f, dialect='excel')  # 设置写入模式
    url = "https://bj.lianjia.com/chengjiao/yanqing/pg{0}/"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 Edg/108.0.1462.54',
        'Cookie':'lianjia_uuid=c7725531-6860-4d80-8bfa-bcde075322bc; _smt_uid=63b146e4.18705b97; select_city=110000; crosSdkDT2019DeviceId=jltyq5-u2h4ea-jyfr3osqxjhmugn-gaa3tbsm7; login_ucid=2000000300904814; lianjia_token=2.00138595f97bef897b0228bcc8e1ae0811; lianjia_token_secure=2.00138595f97bef897b0228bcc8e1ae0811; security_ticket=ZmwtybM4hh121XbmC+JRpKdIXBCMxI6uRaDZ5zLT5SDyM6IUhBvEKx4iw+kPBuhewqWs7/0uxakHJan4Z7Y39lu+CEizRaErK7aYaf8FS2FTevyF+b5PT9n8BUV708Jr31A+muUak7ng9wGbQMkgDaDduUYrZLmteNzkCPe2v8E=; lianjia_ssid=7792b0a7-265f-4fe9-a18e-8b488962aaa8; GUARANTEE_BANNER_SHOW=true; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%221856c7cae80582-01a1074295aeb4-7a575473-1327104-1856c7cae81ec6%22%2C%22%24device_id%22%3A%221856c7cae80582-01a1074295aeb4-7a575473-1327104-1856c7cae81ec6%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_referrer%22%3A%22%22%2C%22%24latest_referrer_host%22%3A%22%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%7D%7D'
    }
    i = 1;
    while (1 == 1):
        rurl = url.replace("{0}", str(i))
        print("请求地址：" + rurl)
        i += 1
        if (i > 3):
            break
        resp = requests.get(rurl, headers=headers)

        html = resp.text
        soup = BeautifulSoup(html, 'html.parser')  # 解析
        # print (soup)
        infos = soup.find(class_='listContent').findAll('li')
        # print(infos)
        for info in infos:
            try:
                info_area = info.find(class_='info')
                title = info_area.find(class_='title').find('a').get_text().split()[0] #已售房标题 例如：华龙美晟
                layout = info_area.find(class_='title').find('a').get_text().split()[1]  # 房型 例如：2室1厅
                size = info_area.find(class_='title').find('a').get_text().split()[2][:-2] #大小 例如：57.91  （单位是平米）
                # print(title,layout,size)

                area = '延庆'  # 区域

                house_info = info_area.find(class_='houseInfo').get_text() #房源信息 例如：南 北 | 简装
                # print(house_info)
                house_info_list = house_info.split('|')
                orientation =  house_info_list[0].strip() # 朝向 例如：南 北
                decoration = house_info_list[1].strip()  # 装修 例如：简装
                # print(orientation,decoration)

                floor = info_area.find(class_='positionInfo').get_text().split()[0].split('(')[0]  # 楼层 例如：中楼层(共6层)
                type = info_area.find(class_='positionInfo').get_text().split()[1] #房屋类型 例如：板楼

                tag_area = info_area.find(class_='dealHouseTxt')
                if tag_area == None:
                    tag = '无标签' #房屋标签 例如：房屋满两年-近地铁
                else:
                    tag = tag_area.findAll('span')[0].get_text()
                    if len(tag_area.findAll('span')) > 1 :
                        for item in tag_area.findAll('span')[1:]:
                            tag += '-' + item.get_text()

                print(title, area,  layout, size, decoration, floor,type, orientation,tag)
                hp = [title, area,  layout, size, decoration, floor,type, orientation,tag]
                csv_writer.writerow(hp)  # 写入一行

            except Exception as e:
                print(e)
        print("睡眠3s")
        time.sleep(3)

if __name__ == '__main__':
    requestHtmlData()
    print("--------------爬取结束-------------")

