import random

from App.models import HomeBaner

baners = {"status": "0", "msg": "OK", "data": [
    {"bannerid": "2320", "type": "7", "object_id": "0", "title": "", "url": "\/",
     "image": "https:\/\/cs.vmovier.com\/Uploads\/Banner\/2018\/05\/03\/5aea858279adf.jpg", "description": "",
     "userid": "10000305", "addtime": "1525319044", "uptime": "1525319044", "orderid": "9", "cateid": "0",
     "count_click": "0", "status": "1", "start_time": "1525319042", "end_time": "0",
     "extra": "{\"app_banner_type\":\"2\",\"app_banner_param\":\"53951\",\"app_show_type\":\"all\"}",
     "extra_data": {"app_banner_type": "2", "app_banner_param": "53951", "app_show_type": "all", "is_album": "0"}},
    {"bannerid": "2314", "type": "7", "object_id": "0", "title": "", "url": "\/",
     "image": "https:\/\/cs.vmovier.com\/Uploads\/Banner\/2018\/04\/26\/5ae1ed7a5a8e3.jpg", "description": "",
     "userid": "10000002", "addtime": "1524755834", "uptime": "1524755834", "orderid": "8", "cateid": "0",
     "count_click": "734", "status": "1", "start_time": "1524755834", "end_time": "0",
     "extra": "{\"app_banner_type\":\"1\",\"app_banner_param\":\"http:\\\/\\\/www.xinpianchang.com\\\/activity\\\/filmfest\\\/ts-filmfest\",\"app_show_type\":\"all\"}",
     "extra_data": {"app_banner_type": "1",
                    "app_banner_param": "http:\/\/www.xinpianchang.com\/activity\/filmfest\/ts-filmfest",
                    "app_show_type": "all"}},
    {"bannerid": "2318", "type": "7", "object_id": "0", "title": "", "url": "\/",
     "image": "https:\/\/cs.vmovier.com\/Uploads\/Banner\/2018\/05\/01\/5ae882c5eaee8.jpg", "description": "",
     "userid": "10000305", "addtime": "1525187270", "uptime": "1525187270", "orderid": "7", "cateid": "0",
     "count_click": "765", "status": "1", "start_time": "1525187269", "end_time": "0",
     "extra": "{\"app_banner_type\":\"2\",\"app_banner_param\":\"53913\",\"app_show_type\":\"all\"}",
     "extra_data": {"app_banner_type": "2", "app_banner_param": "53913", "app_show_type": "all", "is_album": "0"}},
    {"bannerid": "2265", "type": "7", "object_id": "0", "title": "", "url": "\/",
     "image": "https:\/\/cs.vmovier.com\/Uploads\/Banner\/2018\/04\/09\/5acb777b50a9d.jpg", "description": "",
     "userid": "10000307", "addtime": "1523283835", "uptime": "1523283835", "orderid": "6", "cateid": "0",
     "count_click": "4271", "status": "1", "start_time": "1522413060", "end_time": "0",
     "extra": "{\"app_banner_type\":\"1\",\"app_banner_param\":\"http:\\\/\\\/www.xinpianchang.com\\\/activity\\\/creation\\\/id-18\",\"app_show_type\":\"all\"}",
     "extra_data": {"app_banner_type": "1",
                    "app_banner_param": "http:\/\/www.xinpianchang.com\/activity\/creation\/id-18",
                    "app_show_type": "all"}},
    {"bannerid": "2316", "type": "7", "object_id": "0", "title": "", "url": "\/",
     "image": "https:\/\/cs.vmovier.com\/Uploads\/Banner\/2018\/04\/27\/5ae2cd10b108d.jpg", "description": "",
     "userid": "10000305", "addtime": "1524813077", "uptime": "1524813077", "orderid": "5", "cateid": "0",
     "count_click": "431", "status": "1", "start_time": "1524813072", "end_time": "0",
     "extra": "{\"app_banner_type\":\"2\",\"app_banner_param\":\"53874\",\"app_show_type\":\"all\"}",
     "extra_data": {"app_banner_type": "2", "app_banner_param": "53874", "app_show_type": "all", "is_album": "0"}},
    {"bannerid": "2261", "type": "7", "object_id": "0", "title": "", "url": "\/",
     "image": "https:\/\/cs.vmovier.com\/Uploads\/Banner\/2018\/03\/21\/5ab243d7ccc92.png", "description": "",
     "userid": "10000307", "addtime": "1521632218", "uptime": "1521632218", "orderid": "4", "cateid": "0",
     "count_click": "2031", "status": "1", "start_time": "1521632215", "end_time": "0",
     "extra": "{\"app_banner_type\":\"1\",\"app_banner_param\":\"http:\\\/\\\/www.xinpianchang.com\\\/activity\\\/independence\\\/ts-real\",\"app_show_type\":\"all\"}",
     "extra_data": {"app_banner_type": "1",
                    "app_banner_param": "http:\/\/www.xinpianchang.com\/activity\/independence\/ts-real",
                    "app_show_type": "all"}},
    {"bannerid": "2308", "type": "7", "object_id": "0", "title": "", "url": "\/",
     "image": "https:\/\/cs.vmovier.com\/Uploads\/Banner\/2018\/04\/24\/5aded98ebacdf.jpg", "description": "",
     "userid": "10000002", "addtime": "1524554139", "uptime": "1524554139", "orderid": "3", "cateid": "0",
     "count_click": "357", "status": "1", "start_time": "1524554126", "end_time": "0",
     "extra": "{\"app_banner_type\":\"2\",\"app_banner_param\":\"53888\",\"app_show_type\":\"all\"}",
     "extra_data": {"app_banner_type": "2", "app_banner_param": "53888", "app_show_type": "all", "is_album": "0"}},
    {"bannerid": "2075", "type": "7", "object_id": "0", "title": "", "url": "\/",
     "image": "https:\/\/cs.vmovier.com\/Uploads\/Banner\/2018\/04\/26\/5ae1bd3edeb69.jpg", "description": "",
     "userid": "10000307", "addtime": "1524743489", "uptime": "1524743489", "orderid": "2", "cateid": "0",
     "count_click": "17549", "status": "1", "start_time": "1511175600", "end_time": "0",
     "extra": "{\"app_banner_type\":\"1\",\"app_banner_param\":\"https:\\\/\\\/edu.xinpianchang.com\\\/course\\\/18?from=vappbanner\",\"app_show_type\":\"all\"}",
     "extra_data": {"app_banner_type": "1",
                    "app_banner_param": "https:\/\/edu.xinpianchang.com\/course\/18?from=vappbanner",
                    "app_show_type": "all"}},
    {"bannerid": "2218", "type": "7", "object_id": "0", "title": "", "url": "\/",
     "image": "https:\/\/cs.vmovier.com\/Uploads\/Banner\/2018\/04\/28\/5ae426f080aff.jpg", "description": "",
     "userid": "10000307", "addtime": "1524901623", "uptime": "1524901623", "orderid": "1", "cateid": "0",
     "count_click": "4338", "status": "1", "start_time": "1518005580", "end_time": "0",
     "extra": "{\"app_banner_type\":\"1\",\"app_banner_param\":\"https:\\\/\\\/mp.weixin.qq.com\\\/s\\\/UE68c0ZEyEgkdwlHTob7uA\",\"app_show_type\":\"all\"}",
     "extra_data": {"app_banner_type": "1", "app_banner_param": "https:\/\/mp.weixin.qq.com\/s\/UE68c0ZEyEgkdwlHTob7uA",
                    "app_show_type": "all"}}]}
value = baners['data']


def add_baner(db):
    for val in value:
        baner = HomeBaner()
        baner.image = val.get('image').replace('\\', '')
        baner.name = 'baner %d' % random.randint(1, 200)
        baner.trackId = random.randint(1, 200)
        try:
            db.session.add(baner)
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            print(e)
