from __future__ import print_function
import requests
import json


class LagouCrawl(object):

    def __init__(self):
        self.url = "https://www.lagou.com/jobs/positionAjax.json"
        # 请求头
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.79 Safari/537.36",
            "Referer": "https://www.lagou.com/jobs/list_python",
            "Cookie": "_ga=GA1.2.2032920817.1520234065; _gid=GA1.2.2007661123.1520234065; user_trace_token=20180305151430-d90e083a-2044-11e8-9cf0-525400f775ce; LGUID=20180305151430-d90e0bf2-2044-11e8-9cf0-525400f775ce; showExpriedIndex=1; showExpriedCompanyHome=1; showExpriedMyPublish=1; hasDeliver=0; index_location_city=%E5%8C%97%E4%BA%AC; JSESSIONID=ABAAABAACBHABBIECE1AB2B1B3ED00095A40CC2532D48F6; hideSliderBanner20180305WithTopBannerC=1; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1520234067,1520237823,1520298106; LGSID=20180306090145-f0f266a0-20d9-11e8-b126-5254005c3644; _putrc=6F0BC7CDE26E29D5; login=true; unick=%E5%AD%99%E5%85%B0%E6%98%8C; gate_login_token=d3d779887321e8280503a885cdda9b6badc9944fb3549bb7; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1520299986; _gat=1; LGRID=20180306093308-530763f4-20de-11e8-9d87-525400f775ce; TG-TRACK-CODE=index_search; SEARCH_ID=f130bb4a5c0140d7928602bd7d6d5054"
        }
        # 查询字符串
        self.params = {
            "city": "北京",
            "needAddtionalResult": False,
            "isSchoolJob": 0
        }
        # 表单数据
        self.data = {
            "first": True,
            "pn": '1',
            "kd": '技术总监'
        }

    def start_crawl(self, page=1):
        self.data['pn'] = str(page)
        response = requests.post(
            self.url, params=self.params, data=self.data, headers=self.headers)
        data = response.content.decode('utf-8')
        dict_data = json.loads(data)
        return dict_data

    def get_page_num(self):
        data = self.start_crawl()
        items = data['content']['positionResult']['totalCount']
        import math
        page = math.ceil(items/15)
        if page > 30:
            return 30
        else:
            return page

    def save(self, data, filename):
        position_list = data["content"]["positionResult"]["result"]

        col = ['positionId', 'positionLables', 'positionName', 'positionAdvantage',
               'firstType', 'secondType', 'workYear', 'education', 'salary', 'isSchoolJob', 'companyId', 'companyShortName',
               'companyFullName', 'companySize', 'financeStage', 'industryField', 'industryLables', 'createTime',
               'formatCreateTime', 'city', 'district', 'businessZones', 'linestaion', 'stationname']

        f = open('data/'+filename, 'a', encoding='utf-8')
        for position in position_list:
            line = ""
            flag = False
            for e in col:
                if flag:
                    line += ',' + "\""+str(position[e]) + "\""
                else:
                    line += "\""+str(position[e]) + "\""
                flag = True
            line += '\n'
            f.write(line)


positionName_list = []
with open('position_name.txt', 'r') as f:
    for line in f.readlines():
        positionName_list += line.strip().split(',')

city_list = ['', '北京', '上海', '杭州',
             '广州', '深圳', '成都']
f2 = open('info.txt', 'a')
f3 = open('error.txt', 'a')
for city in city_list:
    try:
        for name in positionName_list:
            try:
                print('city: {} position_name: {}'.format(city, name))
                spider = LagouCrawl()
                spider.params['city'] = city
                spider.data['kd'] = name
                page_num = spider.get_page_num()
                for page in range(1, page_num+1):
                    data = spider.start_crawl(page)
                    spider.save(
                        data, spider.params['city']+spider.data['kd']+'.txt')
                info = "info  city: {} name: {} page: {}\n".format(
                    city, name, page_num)
                print(info)
                f2.write(info)
            except Exception as e:
                print(e)
    except Exception as e:
        f3.write('error: '+str(e)+'\n')
f2.close()
f3.close()
