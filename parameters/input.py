#-*-encoding:utf-8 -*-
__author__ = 'lina'

# airline = {
#     "departure": "PEK",
#     "arrival": ""
# }

para_input = {
    "arrival": {
        "valid": ["PEK", "CAN"],
        "no_data": ["123", "abcdef", "!@#$%"],
        "invalid": [""]
                },
    "departure": {
        "valid": ["SHA", "CTU"],
        "no_data": ["0", "PEKA", ";']"],
        "invalid": [""]
    },

    "pagesize": {
        "valid": [10, 1],
        # "no_data": [0],
        "invalid": [-10, "abc", "!%$#%#*&"]
    },

    "phone": {
        "valid": [13412345678],
        "invalid": [123, 0, 134123456789, 1341234567, "abc", ":,./"]
    },

    "region": {
        "valid": ["China"],
        "invalid": ["123", "safad"]
    },

    "poi": {
        "valid": ["31.235890,121.480935"],
        "invalid": ["11.11", "a.b", "a,b"]
    },

    "content":{
        "valid": ["abcdef"],
        "invalid": ["", " "]
    },

    "keywords": {
        "valid": ["abc"],
        "invalid": ["!@#!$#"]
    },

    "uid":{
        "valid": [10022742],
        "invalid": [0, 1, "-1"]
    },

    "text": {
        "valid": ["aaaa"],
        "invalid": ["", " "]
    },

    "type": {
        "valid": ['hotel', 'airline'],
        "invalid": [2]
    },

    "id":{
        "valid": [1234],
        "invalid": ["abcd"]
    },

    "wid":{
        "valid": ["88854"],
        "invalid": [1762093, "acad"]
    },

    "status":{
        "valid": [1, 2, 3],
        "invalid": ["acadapoi"]
    },

    "key":{
        "valid": [1, 2],
        "invalid": []
    },

    "return": {
        "valid": [1, -1, 0],
        "invalid": ["aaa", "bbbb"]
    },

    "extraname": {
        "valid": ["yu"],
        "invalid": ["123"]
    },

    "task_id": {
        "valid": [0],
        "invalid": ["aaa"]
    },

    "code": {
        "valid": ["1234"],
        "invalid": ["123", "12", "1", ""]
    },

    "password":{
        "valid": ["OFZQ8SGMmIoSW90DU36TRIih2kRac5CTW7OtA5I8gJw="],
        "invalid": [" "]
    },

    "name":{
        "valid": ["phuket", "samui"],
        "invalid": ["aaabbb"]
    },

    "avatar_origin":{
        "valid": ["6c05871eb4269d81152eea5abd7e482f"],
        "invalid": ["qerqerads", " "]
    },

    "wxuid":{
        "valid": ["oVZHSsqoWAYoUo25bEmHUw8xmjks"],
        "invalid": ["123313"]
    },

    "avatar": {
        "valid": ["e9c68001ee9716ec7f3bfc3598df4fa6"],
        "invalid": ["!@#$%%", ""]
    },

    "nickname":{
        "valid": ["zbyufei"],
        "invalid": ["abcdefghijklmnopqrstuvwxyz"]
    },

    "username": {
        "valid": ["vass", "avad"],
        "invalid": []
    },

    "group": {
        "valid": ["Hyatt", "Marriott"],
        "invalid": ["daea"]
    },

    "wuid": {
        "valid": ["23"],
        "invalid": [""," "]
    },

    "iata": {
        "valid": ["CTU"],
        "invalid": ["utc"]
    },

    "title": {
        "valid": ["aasf"],
        "invalid": ["a", "abcdefghijkabcdefghijkaaa"]
    },

    "hotel":{
        "valid": ["10000003"],
        "invalid": ["adac", ""]
    },

    "flight": {
        "valid": ["10004091"],
        "invalid": ["poiu", ""]
    },

    "reason": {
        "valid": ["asfssdfa"],
        "invalid": ["", " "]
    },

    "lastid": {
        "valid": [83277],
        "invalid": ["-1", "avds"]
    },

    "topicid": {
        "valid": [6],
        "invalid": ["qwe"],
    },

    "taskid": {
        "valid": [0],
        "invalid": ["qwert"]
    },

    "thumbs": {
        "valid": ["da04714820e1a1495bc6b87d90f8c8a8"],
        "invalid": [" ", "", "a", "1"]
    },

    "uniqueid": {
        "valid": ["14389269891885"],
        "invalid": ["qwert"]
    },

    "images": {
        "valid": ["a92b663f434bc0d6dbaa02affe05ac80"],
        "invalid": [" ", "", "pooo", "0"]
    },

    "flag": {
        "valid": ["true"],
        "invalid": ["are"]
    },

    "limit": {
        "valid": [1, 10],
        "no_data": [0],
        "invalid": [-1]
    },

    "profession": {
        "valid": ["信息技术与服务"],
        "invalid": [123]
    },

    "gender": {
        "valid": [1, 2, 3],
        "invalid": [-1, 0, 4, "rrr"]
    },

    "intro":{
        "valid": ["silence"],
        "invalid": [" ", "Abcdefghijklmnopqrstuvwxyzqwertyuioplkjhgfdsazxcvbnmpoiuytrewqasdfghjklmnbvcxzqwertyuioplkjhgfdsazxc"]
    },

    "come_from": {
        "valid": ["美国|亚利桑那州|图森", "中国|北京", "中国香港"],
        "invalid": ["!@#$%^", "", " "]
    },

#酒店类型
    "category": {
        "valid": ["1", "2", "3", "4", "5"],
        "invalid": ["134#%$^#%$", "0", "6"]
    },

    "city": {
        "valid": ["bali", "北京"],
        "invalid": ["@#!$"]
    },

    "brand": {
        "valid": ["喜来登"],
        "invalid": ["acvs", "!@#$%", 0]
    },

    "offset": {
        "valid": [0, 1, 10],
        "invalid": [-1, 100000]
    },

    "best_worst": {
        "valid": ["best", "worst"],
        "invalid": [12, "besta"]
    },

    "aircraft": {
        "valid": ["320"],
        "invalid": ["qwe", "0000"]
    },

    "carrier": {
        "valid": ["CA", "MU"],
        "invalid": ["@#$!", "123", "CACB"]
    },

#ISEFlight
    "depart": {
        "valid": ["sha"],
        "invalid": ["111"]
    },


    "country": {
        "valid": ["China"],
        "invalid": ["09"]
    },

#谁能看我的体验
    "switchfeed": {
        "valid": [0, 1, 2, 3],
        "invalid": [-1, 4, 123, "uiop"]
    },

#发布签到信息
    "switcharrival": {
        "valid": [0, 1],
        "invalid": [12, "xyz", "120038"]
    },


#允许分享
    "switchshare": {
        "valid": [0, 1],
        "invalid": [3, -0, "abc"]
    },

#公开地理信息
    "switchlocation": {
        "valid": [0, 1],
        "invalid": [-1, 2, 1.112]
    },
#IUserRemark
    "remark": {
        "valid": ["test remark"],
        "invalid": ["", " ", "超过十个字符测试差两个", "abcdqwertyuioplkjhgfd"]
    },

#IuserFeedback
    "image": {
        "valid": [],
        "invalid": []
    },

    "commentid": {
        "valid": [302296, 302295],
        "invalid": [0, "abc"]
    },

    "action": {
        "valid": ["incr", "set"],
        "invalid": ["ste", 0]
    },

    "step": {
        "valid": [],
        "invalid": []
    },

    "score_roomstyle": {
        "valid": [4],
        "invalid": [0, 6]
    },

    "score_fenwei": {
        "valid": [1],
        "invalid": [0, 6]
    },

    "score_design": {
        "valid": [2],
        "invalid": [0, 6]
    },

    "score_service": {
        "valid": [3],
        "invalid": [0, 6]
    },

    "scores": {
        "valid": [1.3, 5.0, 0.0],
        "invalid": [-0.1, 5.1]
    },

    "clear": {
        "valid": [0, 1],
        "invalid": [-1]
    },

    "review": {
        "valid": [3838],
        "invalid": [0, -1]
    },

    "comment_id": {
        "to_delete": [302297]
    },

    "feed_id": {
        "to_share": [],
        "to_delete": [137893]
    },

    "membership": {
        "valid": [43501]
    },

    "topic": {
        "valid": [5]
    },

    "tags": {
        "valid": ["aaa"],
        "invalid": [""]
    },

    "desc": {
        "valid": ["aaa"],
        "invalid": [""]
    },

    "draft": {
        "valid": ["aaa"]
    },

    "aid": {
        "valid": [123]
    },

    "location": {
        "valid": ["beijing"],
        "invalid": [""]
    },

    "sort": {
        "valid": ["desc"]
    },

    "distance": {
        "valid": ["123"]
    },

    "page": {
        "valid": [1],
        "invalid": [0]
    },

    "lastId": {
        "valid": [123],
        "invalid": [0]
    },

    "perPage": {
        "valid": [20],
        "invalid": [0]
    },

    "airline": {
        "valid": ["CA123"]
    },

    "living": {
        "valid": ["chengdu"]
    },

    "size": {
        "valid": [20]
    },

    "phones": {
        "valid": [123456],
        "invalid": [0]
    },

    "json": {
        "valid": [],
        "invalid": []
    },

    "notice": {
        "valid": [],
        "invalid": []
    },

    "msg": {
        "valid": [],
        "invalid": []
    },

    "needfeed": {
        "valid": [1, 0],
        "invalid": [-1]
    },

    "rights_id": {
        "valid": [1, 2, 3],
        "invalid": [-1]
    },

     "need_feed": {
        "valid": [1, 0],
        "invalid": [-1]
    },

    "sort_params": {
        "valid": [],
        "invalid": []
    },

    "state": {
        "valid": [],
        "invalid": []
    },

    "ordertime": {
        "valid": [],
        "invalid": []
    },

    "product_id": {
        "valid": [],
        "invalid": []
    },

    "peoplenum": {
        "valid": [],
        "invalid": []
    },

    "shop_id": {
        "valid": [],
        "invalid": []
    },

    "pageSize": {
        "valid": [10, 1],
        # "no_data": [0],
        "invalid": [-10, "abc", "!%$#%#*&"]
    },

    "need_filter": {
        "valid": [0, 1],
        "invalid": [-1]
    },

    "business": {
        "valid": [],
        "invalid": []
    },

    "data": {
        "valid": ["aaaa"],
        "invalid": ["aaaa"]
    },

    "act": {
        "valid": ["ddd"],
        "invalid": ["ddd"]
    },

    "score": {
        "valid": [11],
        "invalid": [0]
    },

    "date": {
        "valid": ["2015"],
        "invalid": [0]
    },

    "sign": {
        "valid": ["111"],
        "invalid": ["ddd"]
    },

    "clientbag": {
        "valid": [],
        "invalid": []
    },

    #todo
    #to fix
    "token": {
        "valid": ["ddd"],
        "invalid": []
    }

}

