# -*- coding: utf-8 -*- 
import os
import sys
reload(sys)
sys.setdefaultencoding('utf8') 

FILE_PATH = os.path.dirname(os.path.abspath(__file__))
sys.path.append(FILE_PATH + "/../lib/")


import time
import datetime


import random

import bottle
from bottle import jinja2_view , route, run, template,static_file

from bottle import request
bottle.TEMPLATE_PATH.append(FILE_PATH + "/../templates/")

@route('/css/<filepath:path>')
def server_static(filepath):
    return static_file(filepath, root=FILE_PATH + "/../static/css")

@route('/js/<filepath:path>')
def server_static(filepath):
    return static_file(filepath, root=FILE_PATH + "/../static/js")

@route('/images/<filepath:path>')
def server_static(filepath):
    return static_file(filepath, root=FILE_PATH + "/../static/images")

@route('/bootstrap/<filepath:path>')
def server_static(filepath):
    return static_file(filepath, root=FILE_PATH + "/../static/bootstrap")

@route('/ext/<filepath:path>')
def server_static(filepath):
    return static_file(filepath, root=FILE_PATH + "/../static/ext")

@route('/fonts/<filepath:path>')
def server_static(filepath):
    return static_file(filepath, root=FILE_PATH + "/../static/fonts")

@route('/')
@jinja2_view('shop.html')
def index():
    return {}

@route('/flow_analysis')
@jinja2_view('flow_analysis.html')
def flow_analysis():
    return {}

@route('/access_path_analysis')
@jinja2_view('access_path_analysis.html')
def flow_analysis():
    return {}

@route('/roi_analysis')
@jinja2_view('roi_analysis.html')
def roi_analysis():
    return {}

@route('/keyword_flow_analysis')
@jinja2_view('keyword_flow_analysis.html')
def keyword_flow_analysis():
    return {}

@route('/source_analysis')
@jinja2_view('source_analysis.html')
def source_analysis():
    return {}

@route('/region_analysis')
@jinja2_view('region_analysis.html')
def region_analysis():
    return {}

@route('/industry_monitor')
@jinja2_view('industry_monitor.html')
def industry_monitor():
    return {}

@route('/shop')
@jinja2_view('shop.html')
def shop():
    return {}

@route('/goods')
@jinja2_view('goods.html')
def goods():
    return {}

def str2date(date_str):
    if date_str == None:
        return datetime.date.today()

    date = datetime.datetime(* time.strptime(date_str, "%Y-%m-%d")[:6])
    return date

def get_uv(shop_id):
    start_date_str = request.query.start_date or None
    end_date_str = request.query.end_date or None
    
    start_date = str2date(start_date_str)
    end_date = str2date(end_date_str)

    uv_list = []
    for n in range(int ((end_date - start_date).days+1)):
        cur_date = start_date + datetime.timedelta(n)
        uv_list.append({"date":cur_date,"uv":random.randomInt(1,100)})
    return uv_list


def get_pv(shop_id):
    start_date_str = request.query.start_date or None
    end_date_str = request.query.end_date or None
    
    start_date = str2date(start_date_str)
    end_date = str2date(end_date_str)

    pv_list = []
    for n in range(int ((end_date - start_date).days+1)):
        cur_date = start_date + datetime.timedelta(n)
        pv_list.append({"date":cur_date,"pv":random.randomInt(1,100)})
    return pv_list

def get_ta(shop_id):
    start_date_str = request.query.start_date or None
    end_date_str = request.query.end_date or None
    
    start_date = str2date(start_date_str)
    end_date = str2date(end_date_str)

    ta_list = []
    for n in range(int ((end_date - start_date).days+1)):
        cur_date = start_date + datetime.timedelta(n)
        ta_list.append({"date":cur_date,"ta":random.randomInt(1,100)})
    return ta_list
    
def get_roi(shop_id):
    start_date_str = request.query.start_date or None
    end_date_str = request.query.end_date or None
    
    start_date = str2date(start_date_str)
    end_date = str2date(end_date_str)

    roi_list = []
    for n in range(int ((end_date - start_date).days+1)):
        cur_date = start_date + datetime.timedelta(n)
        roi_list.append({"date":cur_date,"roi":random.randomInt(1,100)})
    return roi_list

def get_pct(shop_id):
    start_date_str = request.query.start_date or None
    end_date_str = request.query.end_date or None
    
    start_date = str2date(start_date_str)
    end_date = str2date(end_date_str)

    pct_list = []
    for n in range(int ((end_date - start_date).days+1)):
        cur_date = start_date + datetime.timedelta(n)
        pct_list.append({"date":cur_date,"pct":random.randomInt(1,100)})
    return pct_list


def get_sas(shop_id):
    start_date_str = request.query.start_date or None
    end_date_str = request.query.end_date or None
    
    start_date = str2date(start_date_str)
    end_date = str2date(end_date_str)

    sas_list = []
    for n in range(int ((end_date - start_date).days+1)):
        cur_date = start_date + datetime.timedelta(n)
        sas_list.append({"date":cur_date,"sas":random.randomInt(1,100)})
    return sas_list

@route('/shop/:shop_id')
@jinja2_view('index2.html')
def test(shop_id):
    start = request.query.start or 0
    limit = request.query.limit or 10
    orderby = request.query.orderby or ""
    keyword = request.query.keyword or ""
    shop = {
        "shop_id" : "123456",
        "title" : "名鞋库运动旗舰店",
        "url" : "http://www.baidu.com",
        "total_count" : 60,
        "start" : start,
        "orderby" : orderby,
        "keyword" : keyword,
        "sell_trend" : [
            {"date":"2014-01-14","count":60,"money":"30"},
            {"date":"2014-01-14","count":60,"money":"30"},
            {"date":"2014-01-14","count":60,"money":"30"},
        ]
    }
    items = [
            {"item_id":65535, "id" : int(start) , "url" : "www.baidu.com","title" : "耐克NIKE 男鞋 跑步鞋 气垫/AIR MAX 运动鞋 511915-015 黑+孔雀蓝+电黄+白 43 抢年货咯！爆款低至3折，折后全场领券满300减50，满500减100！限1月6-20日!" , "max_datapush_commit_ts":"2013-12-12","market_price":100.00,"jd_price":98.00,"image_url" : "http://img14.360buyimg.com/n1/g13/M00/0E/1E/rBEhUlJP8H4IAAAAAAIakZZ0tJkAADz5wC95VwAAhqp464.jpg"},
            {"item_id":128, "id" : int(start)+1, "url" : "www.google.com","title" : "思诺芙德SNOWFORTE 送礼女百搭100%纯山羊绒衫圆领打底女开衫0200800027 浅灰1702 95/S 爱你一生一世~京东跨年品牌团！ 全场1折起, 仅限1天 ！ 100%纯山羊绒 全年最低价 ","market_price":20000.00,"jd_price":10000.00,"image_url":"http://img30.360buyimg.com/popshop/g4/M00/04/15/rBEGFk-sdOoIAAAAAABQKJt3Z8AAAA6XQGGfd4AAFBA683.jpg"}
    ]
    return {"shop" : shop,"items":items}


'''
    <li class="active" ><a href="#item_last_trend_chart_{{item.id}}" data-toggle="tab" >商品近期销量</a></li>
    <li><a href="#item_trend_chart_{{item.id}}" data-toggle="tab" >销售和销售额趋势图</a></li>
    <li><a href="#item_trend_table_{{item.id}}" data-toggle="tab" >销售和销售额趋势表</a></li>
    <li><a href="#item_attribute_table_{{item.id}}" data-toggle="tab" >商品属性</a></li>
    <li><a href="#item_change_history_table_{{item.id}}" data-toggle="tab">商品变更记录</a></li>
'''

@route('/item_last_trend_chart/:item_id')
def get_item_last_trend_chart(item_id):
    data = {
        "labels" : ["7天销量","7天销售额","30天销量","30天销售额","7天成交量","30天成交量"],
        "datasets" : [
            {
                "fillColor" : "rgba(220,220,220,0.5)",
                "strokeColor" : "rgba(220,220,220,1)",
                "data" : [65,59,90,81,56,55]
            },
        ]
    }
    return {"item_id":item_id,"func_name":"item_last_trend_chart","data" : data}

@route('/item_trend_chart/:item_id')
def get_item_trend_chart(item_id):
    data = {
        "labels" : ["January","February","March","April","May","June","July"],
        "datasets" : [
            {
                "fillColor" : "rgba(220,220,220,0.5)",
                "strokeColor" : "rgba(220,220,220,1)",
                "data" : [65,59,90,81,56,55,40]
            },
            {
                "fillColor" : "rgba(151,187,205,0.5)",
                "strokeColor" : "rgba(151,187,205,1)",
                "data" : [28,48,40,19,96,27,100]
            }
        ]
    }
    return {"item_id":item_id,"func_name":"item_trend_chart","data" : data}

@route('/item_trend_table/:item_id')
def get_item_trend_table(item_id):
    data = [
        {"date":"2014-01-14","count":60,"money":"30"},
        {"date":"2014-01-14","count":60,"money":"30"},
        {"date":"2014-01-14","count":60,"money":"30"},
        {"date":"2014-01-14","count":60,"money":"30"},
    ]
    title = {"date" : "日期","count" : "销售量","money" : "销售额"}
    return {"item_id":item_id,"func_name":"item_trend_table","data" : data, "title" : title}

@route('/item_attribute_table/:item_id')
def get_item_attribute_table(item_id):
    data = [
        {"attr_name" : "attr1", "attr_value" : "val1"},
        {"attr_name" : "attr2", "attr_value" : "val2"},
        {"attr_name" : "attr3", "attr_value" : "val3"},
        {"attr_name" : "attr4", "attr_value" : "val4"},
    ]
    return {"item_id":item_id,"func_name":"item_attribute_table","data" : data}

@route('/item_change_history_table/:item_id')
def get_item_change_history_table(item_id):
    data = [
        {"date":"2014-01-14","price":"30"},
        {"date":"2014-01-14","price":"30"},
        {"date":"2014-01-14","price":"30"},
    ]
    title = {"date" : "日期","price" : "原价格"}
    return {"item_id":item_id,"func_name":"item_change_history_table","data" : data, "title" : title}



''' shop api ''' 

@route('/shop_last_trend_chart/:shop_id')
def get_shop_last_trend_chart(shop_id):
    data = {
        "labels" : ["7天销量","7天销售额","30天销量","30天销售额","7天成交量","30天成交量"],
        "datasets" : [
            {
                "fillColor" : "rgba(220,220,220,0.5)",
                "strokeColor" : "rgba(220,220,220,1)",
                "data" : [65,59,90,81,56,55]
            },
        ]
    }
    return {"shop_id":shop_id,"func_name":"shop_last_trend_chart","data" : data}

@route('/shop_trend_chart/:shop_id')
def get_shop_trend_chart(shop_id):
    data = {
        "labels" : ["January","February","March","April","May","June","July"],
        "datasets" : [
            {
                "fillColor" : "rgba(220,220,220,0.5)",
                "strokeColor" : "rgba(220,220,220,1)",
                "data" : [65,59,90,81,56,55,40]
            },
            {
                "fillColor" : "rgba(151,187,205,0.5)",
                "strokeColor" : "rgba(151,187,205,1)",
                "data" : [28,48,40,19,96,27,100]
            }
        ]
    }
    return {"shop_id":shop_id,"func_name":"shop_trend_chart","data" : data}

@route('/shop_trend_table/:shop_id')
def get_shop_trend_table(shop_id):
    data = [
        {"date":"2014-01-14","count":60,"money":"30"},
        {"date":"2014-01-14","count":60,"money":"30"},
        {"date":"2014-01-14","count":60,"money":"30"},
        {"date":"2014-01-14","count":60,"money":"30"},
    ]
    title = {"date" : "日期","count" : "销售量","money" : "销售额"}
    return {"item_id":shop_id,"func_name":"shop_trend_table","data" : data, "title" : title}

run(host='localhost', port=8081,reloader=True)
