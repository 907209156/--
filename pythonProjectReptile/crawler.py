import requests
import uuid
import time
from bs4 import BeautifulSoup
import csv

def requestHtmlData():
    f = open("D://Desktop//house.csv", 'a', newline='')  # 打开文件
    csv_writer = csv.writer(f, dialect='excel')  # 设置写入模式
    url = "https://bj.lianjia.com/zufang/yanqing/pg{0}/#contentList"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.55 Safari/537.36 Edg/96.0.1054.43'
    }
    i = 1;
    while (1 == 1):
        rurl = url.replace("{0}", str(i))
        print("请求地址：" + rurl)
        i += 1
        if (i > 2):
            break
        resp = requests.get(rurl, headers=headers)

        html = resp.text
        soup = BeautifulSoup(html, 'html.parser')  # 解析
        # print (soup)
        infos = soup.findAll(class_='content__list--item')
        # print(infos)
        for info in infos:
            try:
                title = info.find(class_='content__list--item--aside').attrs['title']
                type = title.split(' ')[0].split('·')[0]#合租类型
                name = title.split(' ')[0].split('·')[1]#名字
                layout = title.split(' ')[1]#布局
                orientation = title.split(' ')[2]#朝向
                price = info.find(class_='content__list--item--main').find(class_='content__list--item-price').find(
                    'em').get_text();#价格
                size = info.find(class_='content__list--item--main').find(
                    class_='content__list--item--des').get_text().split("\n")[3][8:-1]#占地面积

                area = info.find(class_='content__list--item--main').find(
                    class_='content__list--item--des').a.get_text();#区域
                addresses = info.find(class_='content__list--item--main').find(
                    class_='content__list--item--des').findAll('a');
                address = addresses[0].get_text() + '-' + addresses[1].get_text() + '-' + addresses[2].get_text()#地址
                tags = info.find(class_='content__list--item--main').find(class_='content__list--item--bottom').findAll(
                    'i');
                tagStr = ''#标签
                for tag in tags:
                    if (tagStr != ''):
                        tagStr += '-'
                    tagStr += tag.get_text()
                print(name,area,type,price,size,layout,address,orientation,tagStr)
                hp = [name,area,type,price,size,layout,address,orientation,tagStr]
                csv_writer.writerow(hp)  # 写入一行
            except Exception as e:
                print(e)
        print("睡眠3s")
        time.sleep(3)

# if __name__ == '__main__':
#     requestHtmlData()
#     print("--------------爬取结束-------------")

