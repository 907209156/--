import codecs
import csv

import json
from flask import Flask
import pymysql
from flask_cors import CORS
from dbutils.pooled_db import PooledDB

app = Flask(__name__)
# 连接数据库
POOL = PooledDB(
    creator=pymysql,
    maxconnections=30, #连接池允许的最大连接树
    mincached=5,
    maxcached=5,  # 链接池中最多闲置的链接，0和None不限制
    # 链接池中最多共享的链接数量，0和None表示全部共享。PS: 无用，因为pymysql和MySQLdb等模块的 threadsafety都为1，所有值无论设置为多少，_maxcached永远为0，所以永远是所有链接都共享。
    maxshared=3,
    blocking=True,  # 连接池中如果没有可用连接后，是否阻塞等待。True，等待；False，不等待然后报错
    maxusage=None,  # 一个链接最多被重复使用的次数，None表示无限制
    setsession=[],  # 开始会话前执行的命令列表。如：["set datestyle to ...", "set time zone ..."]
    # ping MySQL服务端，检查是否服务可用。# 如：0 = None = never, 1 = default = whenever it is requested, 2 = when a cursor is created, 4 = when a query is executed, 7 = always
    ping=0,
    host='localhost',
    port=3306,
    user='root',
    passwd='lj123123',
    charset='utf8'
)

CORS(app, supports_credentials = True,resources=r'/*')

#---------------------------租房接口------------------------------

@app.route('/house/area_count',methods=['get','post'])
def area_rent_count():  # put application's code here
    con = POOL.connection() #从连接池拿一个链接

    # 创建一个游标对象cursor
    cursor = con.cursor()

    # 使用execute()方法执行SQL查询
    cursor.execute('use house;')
    cursor.execute("select * from area_rent_count;")

    # 使用 fetchone() 方法获取单条数据;使用 fetchall() 方法获取所有数据
    key = 1
    data = {}

    data['data'] = []
    area_rent_count = cursor.fetchall()
    if area_rent_count != None:
        data['success'] = True
    else:
        data['success'] = False
    for item in area_rent_count:
        data['data'].append({'name': item[0], 'value': item[1], 'key': key})
        key += 1

    return json.dumps(data)

@app.route('/house/rent_type',methods=['get','post'])
def rent_type_count():  # put application's code here
    con = POOL.connection() #从连接池拿一个链接
    # 创建一个游标对象cursor
    cursor = con.cursor()

    # 使用execute()方法执行SQL查询
    cursor.execute('use house;')
    cursor.execute("select * from rent_type_count;")

    # 使用 fetchone() 方法获取单条数据;使用 fetchall() 方法获取所有数据
    key = 1
    data = {}

    data['data'] = []
    rent_type_count = cursor.fetchall()
    if rent_type_count != None:
        data['success'] = True
    else:
        data['success'] = False
    for item in rent_type_count:
        data['data'].append({'type': item[0], 'value': item[1], 'key': key})
        key += 1

    return json.dumps(data)

@app.route('/house/area_price',methods=['get','post'])
def area_price():  # put application's code here
    con = POOL.connection() #从连接池拿一个链接
    # 创建一个游标对象cursor
    cursor = con.cursor()

    # 使用execute()方法执行SQL查询
    cursor.execute('use house;')
    cursor.execute("select * from area_price;")

    # 使用 fetchone() 方法获取单条数据;使用 fetchall() 方法获取所有数据
    key = 1
    data = {}

    data['data'] = []
    area_price = cursor.fetchall()
    if area_price != None:
        data['success'] = True
    else:
        data['success'] = False
    for item in area_price:
        data['data'].append({'name': item[0], 'avg_price': item[1], 'max_price': item[2],'min_price': item[3],'key': key})
        key += 1

    return json.dumps(data)

@app.route('/house/layout',methods=['get','post'])
def house_layout():  # put application's code here
    con = POOL.connection() #从连接池拿一个链接
    # 创建一个游标对象cursor
    cursor = con.cursor()

    # 使用execute()方法执行SQL查询
    cursor.execute('use house;')
    cursor.execute("select * from house_layout order by count desc;")

    # 使用 fetchone() 方法获取单条数据;使用 fetchall() 方法获取所有数据
    key = 1
    data = {}

    data['data'] = []
    house_layout = cursor.fetchall()
    if house_layout != None:
        data['success'] = True
    else:
        data['success'] = False
    for item in house_layout:
        if item[0] != '':
            data['data'].append({'layout_type': item[0], 'value': item[1], 'key': key})
            key += 1


    return json.dumps(data)

@app.route('/house/near_subway',methods=['get','post'])
def near_subway_ratio():  # put application's code here
    con = POOL.connection() #从连接池拿一个链接
    # 创建一个游标对象cursor
    cursor = con.cursor()

    # 使用execute()方法执行SQL查询
    cursor.execute('use house;')
    cursor.execute("select * from near_subway_ratio;")

    # 使用 fetchone() 方法获取单条数据;使用 fetchall() 方法获取所有数据
    key = 1
    data = {}

    data['data'] = []
    near_subway_ratio = cursor.fetchall()
    if near_subway_ratio != None:
        data['success'] = True
    else:
        data['success'] = False
    for item in near_subway_ratio:
        if item[0] != '':
            data['data'].append({'name': item[0], 'value': float(item[1]), 'key': key})
            key += 1


    return json.dumps(data)

@app.route('/hosue/central_heating',methods=['get','post'])
def central_heating_ratio():  # put application's code here
    con = POOL.connection() #从连接池拿一个链接
    # 创建一个游标对象cursor
    cursor = con.cursor()

    # 使用execute()方法执行SQL查询
    cursor.execute('use house;')
    cursor.execute("select * from central_heating_ratio;")

    # 使用 fetchone() 方法获取单条数据;使用 fetchall() 方法获取所有数据
    key = 1
    data = {}

    data['data'] = []
    central_heating_ratio = cursor.fetchall()
    if central_heating_ratio != None:
        data['success'] = True
    else:
        data['success'] = False
    for item in central_heating_ratio:
        if item[0] != '':
            data['data'].append({'name': item[0], 'value': float(item[1]), 'key': key})
            key += 1


    return json.dumps(data)

@app.route('/house/official_varification',methods=['get','post'])
def official_varification_ratio():  # put application's code here
    con = POOL.connection() #从连接池拿一个链接
    # 创建一个游标对象cursor
    cursor = con.cursor()

    # 使用execute()方法执行SQL查询
    cursor.execute('use house;')
    cursor.execute("select * from official_varification_ratio;")

    # 使用 fetchone() 方法获取单条数据;使用 fetchall() 方法获取所有数据
    key = 1
    data = {}

    data['data'] = []
    official_varification_ratio = cursor.fetchall()
    if official_varification_ratio != None:
        data['success'] = True
    else:
        data['success'] = False
    for item in official_varification_ratio:
        if item[0] != '':
            data['data'].append({'name': item[0], 'value': float(item[1]), 'key': key})
            key += 1


    return json.dumps(data)

@app.route('/house/area_size',methods=['get','post'])
def area_size():  # put application's code here
    con = POOL.connection() #从连接池拿一个链接
    # 创建一个游标对象cursor
    cursor = con.cursor()

    # 使用execute()方法执行SQL查询
    cursor.execute('use house;')
    cursor.execute("select * from area_size;")

    # 使用 fetchone() 方法获取单条数据;使用 fetchall() 方法获取所有数据
    key = 1
    data = {}

    data['data'] = []
    area_size = cursor.fetchall()
    if area_size != None:
        data['success'] = True
    else:
        data['success'] = False
    for item in area_size:
        data['data'].append({'name': item[0], 'avg_size': float(item[1]), 'max_size': float(item[2]),'min_size': float(item[3]),'key': key})
        key += 1

    return json.dumps(data)

#-------------------------------二手房在售接口-----------------------------
@app.route('/secondhand_house_onsale/area',methods=['get','post'])
def area_info():  # put application's code here
    con = POOL.connection() #从连接池拿一个链接
    # 创建一个游标对象cursor
    cursor = con.cursor()

    # 使用execute()方法执行SQL查询
    cursor.execute('use secondhand_house_onsale;')
    cursor.execute("select * from area_info;")

    # 使用 fetchone() 方法获取单条数据;使用 fetchall() 方法获取所有数据
    key = 1
    data = {}

    data['data'] = []
    area_info = cursor.fetchall()
    if area_info != None:
        data['success'] = True
    else:
        data['success'] = False
    for item in area_info:
        data['data'].append({'area': item[0], 'count':item[1],'max_price': item[2],'min_price': item[3],'avg_price': item[4],'key': key})
        key += 1

    return json.dumps(data)

@app.route('/secondhand_house_onsale/layout',methods=['get','post'])
def layout_info():  # put application's code here
    con = POOL.connection() #从连接池拿一个链接
    # 创建一个游标对象cursor
    cursor = con.cursor()

    # 使用execute()方法执行SQL查询
    cursor.execute('use secondhand_house_onsale;')
    cursor.execute("select * from layout_info;")

    # 使用 fetchone() 方法获取单条数据;使用 fetchall() 方法获取所有数据
    key = 1
    data = {}

    data['data'] = []
    layout_info = cursor.fetchall()
    if layout_info != None:
        data['success'] = True
    else:
        data['success'] = False
    for item in layout_info:
        data['data'].append({'layout': item[0], 'count':item[1],'ratio':float(item[2]),'max_price': item[3],'min_price': item[4],'avg_price': item[5],'key': key})
        key += 1

    return json.dumps(data)

@app.route('/secondhand_house_onsale/decoration',methods=['get','post'])
def decoration_info():  # put application's code here
    con = POOL.connection() #从连接池拿一个链接
    # 创建一个游标对象cursor
    cursor = con.cursor()

    # 使用execute()方法执行SQL查询
    cursor.execute('use secondhand_house_onsale;')
    cursor.execute("select * from decoration_info;")

    # 使用 fetchone() 方法获取单条数据;使用 fetchall() 方法获取所有数据
    key = 1
    data = {}

    data['data'] = []
    decoration_info = cursor.fetchall()
    if decoration_info != None:
        data['success'] = True
    else:
        data['success'] = False
    for item in decoration_info:
        data['data'].append({'decoration': item[0], 'count':item[1],'ratio':float(item[2]),'max_price': item[3],'min_price': item[4],'avg_price': item[5],'key': key})
        key += 1

    return json.dumps(data)

@app.route('/secondhand_house_onsale/size',methods=['get','post'])
def size_info():  # put application's code here
    con = POOL.connection() #从连接池拿一个链接
    # 创建一个游标对象cursor
    cursor = con.cursor()

    # 使用execute()方法执行SQL查询
    cursor.execute('use secondhand_house_onsale;')
    cursor.execute("select * from size_info;")

    # 使用 fetchone() 方法获取单条数据;使用 fetchall() 方法获取所有数据
    key = 1
    data = {}

    data['data'] = []
    size_info = cursor.fetchall()
    if size_info != None:
        data['success'] = True
    else:
        data['success'] = False
    for item in size_info:
        data['data'].append({'size_section': item[0], 'count':item[1],'ratio':float(item[2]),'max_price': item[3],'min_price': item[4],'avg_price': item[5],'key': key})
        key += 1

    return json.dumps(data)

@app.route('/secondhand_house_onsale/floor',methods=['get','post'])
def floor_info():  # put application's code here
    con = POOL.connection() #从连接池拿一个链接
    # 创建一个游标对象cursor
    cursor = con.cursor()

    # 使用execute()方法执行SQL查询
    cursor.execute('use secondhand_house_onsale;')
    cursor.execute("select * from floor_info;")

    # 使用 fetchone() 方法获取单条数据;使用 fetchall() 方法获取所有数据
    key = 1
    data = {}

    data['data'] = []
    floor_info = cursor.fetchall()
    if floor_info != None:
        data['success'] = True
    else:
        data['success'] = False
    for item in floor_info:
        data['data'].append({'floor': item[0], 'count':item[1],'ratio':float(item[2]),'max_price': item[3],'min_price': item[4],'avg_price': item[5],'key': key})
        key += 1

    return json.dumps(data)

@app.route('/secondhand_house_onsale/orientation',methods=['get','post'])
def orientation_info():  # put application's code here
    con = POOL.connection() #从连接池拿一个链接
    # 创建一个游标对象cursor
    cursor = con.cursor()

    # 使用execute()方法执行SQL查询
    cursor.execute('use secondhand_house_onsale;')
    cursor.execute("select * from orientation_info;")

    # 使用 fetchone() 方法获取单条数据;使用 fetchall() 方法获取所有数据
    key = 1
    data = {}

    data['data'] = []
    orientation_info = cursor.fetchall()
    if orientation_info != None:
        data['success'] = True
    else:
        data['success'] = False
    for item in orientation_info:
        data['data'].append({'orientation': item[0], 'count':item[1],'ratio':float(item[2]),'max_price': item[3],'min_price': item[4],'avg_price': item[5],'key': key})
        key += 1

    return json.dumps(data)

@app.route('/secondhand_house_onsale/near_subway',methods=['get','post'])
def is_near_subway_info():  # put application's code here
    con = POOL.connection() #从连接池拿一个链接
    # 创建一个游标对象cursor
    cursor = con.cursor()

    # 使用execute()方法执行SQL查询
    cursor.execute('use secondhand_house_onsale;')
    cursor.execute("select * from is_near_subway_info;")

    # 使用 fetchone() 方法获取单条数据;使用 fetchall() 方法获取所有数据
    key = 1
    data = {}

    data['data'] = []
    is_near_subway_info = cursor.fetchall()
    if is_near_subway_info != None:
        data['success'] = True
    else:
        data['success'] = False
    for item in is_near_subway_info:
        data['data'].append({'is_near_subway': item[0], 'count':item[1],'ratio':float(item[2]),'max_price': item[3],'min_price': item[4],'avg_price': item[5],'key': key})
        key += 1

    return json.dumps(data)

#---------------------------------二手房已售接口----------------------------
@app.route('/secondhand_house_sold/area',methods=['get','post'])
def area_sold_info():  # put application's code here
    con = POOL.connection() #从连接池拿一个链接
    # 创建一个游标对象cursor
    cursor = con.cursor()

    # 使用execute()方法执行SQL查询
    cursor.execute('use secondhand_house_sold;')
    cursor.execute("select * from area_sold_info;")

    # 使用 fetchone() 方法获取单条数据;使用 fetchall() 方法获取所有数据
    key = 1
    data = {}

    data['data'] = []
    area_sold_info = cursor.fetchall()
    if area_sold_info != None:
        data['success'] = True
    else:
        data['success'] = False
    for item in area_sold_info:
        data['data'].append({'area': item[0], 'count':item[1],'ratio':float(item[2]),'key': key})
        key += 1

    return json.dumps(data)


@app.route('/secondhand_house_sold/layout',methods=['get','post'])
def layout_sold_info():  # put application's code here
    con = POOL.connection() #从连接池拿一个链接
    # 创建一个游标对象cursor
    cursor = con.cursor()

    # 使用execute()方法执行SQL查询
    cursor.execute('use secondhand_house_sold;')
    cursor.execute("select * from layout_sold_info;")

    # 使用 fetchone() 方法获取单条数据;使用 fetchall() 方法获取所有数据
    key = 1
    data = {}

    data['data'] = []
    layout_sold_info = cursor.fetchall()
    if layout_sold_info != None:
        data['success'] = True
    else:
        data['success'] = False
    for item in layout_sold_info:
        data['data'].append({'layout': item[0], 'count':item[1],'ratio':float(item[2]),'key': key})
        key += 1

    return json.dumps(data)

@app.route('/secondhand_house_sold/decoration',methods=['get','post'])
def decoration_sold_info():  # put application's code here
    con = POOL.connection() #从连接池拿一个链接
    # 创建一个游标对象cursor
    cursor = con.cursor()

    # 使用execute()方法执行SQL查询
    cursor.execute('use secondhand_house_sold;')
    cursor.execute("select * from decoration_sold_info;")

    # 使用 fetchone() 方法获取单条数据;使用 fetchall() 方法获取所有数据
    key = 1
    data = {}

    data['data'] = []
    decoration_sold_info = cursor.fetchall()
    if decoration_sold_info != None:
        data['success'] = True
    else:
        data['success'] = False
    for item in decoration_sold_info:
        data['data'].append({'decoration': item[0], 'count':item[1],'ratio':float(item[2]),'key': key})
        key += 1

    return json.dumps(data)


@app.route('/secondhand_house_sold/size',methods=['get','post'])
def size_sold_info():  # put application's code here
    con = POOL.connection() #从连接池拿一个链接
    # 创建一个游标对象cursor
    cursor = con.cursor()

    # 使用execute()方法执行SQL查询
    cursor.execute('use secondhand_house_sold;')
    cursor.execute("select * from size_sold_info;")

    # 使用 fetchone() 方法获取单条数据;使用 fetchall() 方法获取所有数据
    key = 1
    data = {}

    data['data'] = []
    size_sold_info = cursor.fetchall()
    if size_sold_info != None:
        data['success'] = True
    else:
        data['success'] = False
    for item in size_sold_info:
        data['data'].append({'size': item[0], 'count':item[1],'ratio':float(item[2]),'key': key})
        key += 1

    return json.dumps(data)


@app.route('/secondhand_house_sold/floor',methods=['get','post'])
def floor_sold_info():  # put application's code here
    con = POOL.connection() #从连接池拿一个链接
    # 创建一个游标对象cursor
    cursor = con.cursor()

    # 使用execute()方法执行SQL查询
    cursor.execute('use secondhand_house_sold;')
    cursor.execute("select * from floor_sold_info;")

    # 使用 fetchone() 方法获取单条数据;使用 fetchall() 方法获取所有数据
    key = 1
    data = {}

    data['data'] = []
    floor_sold_info = cursor.fetchall()
    if floor_sold_info != None:
        data['success'] = True
    else:
        data['success'] = False
    for item in floor_sold_info:
        data['data'].append({'floor': item[0], 'count':item[1],'ratio':float(item[2]),'key': key})
        key += 1

    return json.dumps(data)


@app.route('/secondhand_house_sold/orientation',methods=['get','post'])
def orientation_sold_info():  # put application's code here
    con = POOL.connection() #从连接池拿一个链接
    # 创建一个游标对象cursor
    cursor = con.cursor()

    # 使用execute()方法执行SQL查询
    cursor.execute('use secondhand_house_sold;')
    cursor.execute("select * from orientation_sold_info;")

    # 使用 fetchone() 方法获取单条数据;使用 fetchall() 方法获取所有数据
    key = 1
    data = {}

    data['data'] = []
    orientation_sold_info = cursor.fetchall()
    if orientation_sold_info != None:
        data['success'] = True
    else:
        data['success'] = False
    for item in orientation_sold_info:
        data['data'].append({'orientation': item[0], 'count':item[1],'ratio':float(item[2]),'key': key})
        key += 1

    return json.dumps(data)


@app.route('/secondhand_house_sold/is_near_subway',methods=['get','post'])
def is_near_subway_sold_info():  # put application's code here
    con = POOL.connection() #从连接池拿一个链接
    # 创建一个游标对象cursor
    cursor = con.cursor()

    # 使用execute()方法执行SQL查询
    cursor.execute('use secondhand_house_sold;')
    cursor.execute("select * from is_near_subway_sold_info;")

    # 使用 fetchone() 方法获取单条数据;使用 fetchall() 方法获取所有数据
    key = 1
    data = {}

    data['data'] = []
    is_near_subway_sold_info = cursor.fetchall()
    if is_near_subway_sold_info != None:
        data['success'] = True
    else:
        data['success'] = False
    for item in is_near_subway_sold_info:
        data['data'].append({'is_near_subway': item[0], 'count':item[1],'ratio':float(item[2]),'key': key})
        key += 1

    return json.dumps(data)


@app.route('/secondhand_house_sold/house_type',methods=['get','post'])
def house_type_sold_info():  # put application's code here
    con = POOL.connection() #从连接池拿一个链接
    # 创建一个游标对象cursor
    cursor = con.cursor()

    # 使用execute()方法执行SQL查询
    cursor.execute('use secondhand_house_sold;')
    cursor.execute("select * from house_type_sold_info;")

    # 使用 fetchone() 方法获取单条数据;使用 fetchall() 方法获取所有数据
    key = 1
    data = {}

    data['data'] = []
    house_type_sold_info = cursor.fetchall()
    if house_type_sold_info != None:
        data['success'] = True
    else:
        data['success'] = False
    for item in house_type_sold_info:
        data['data'].append({'house_type': item[0], 'count':item[1],'ratio':float(item[2]),'key': key})
        key += 1

    return json.dumps(data)


@app.route('/secondhand_house_sold/location',methods=['get','post'])
def city_sale_info():  # put application's code here
    data = {}
    data['success'] = True
    data['data'] = []
    with codecs.open('data/secondhand_sold_location.csv', encoding='utf-8-sig') as f:
        for row in csv.DictReader(f, skipinitialspace=True):
            data['data'].append(row)

    return json.dumps(data)

if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True,port=8080)
