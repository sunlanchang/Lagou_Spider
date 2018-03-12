import requests
import json
from bs4 import BeautifulSoup


class LagouCrawl(object):
    def __init__(self):
        self.url = "https://www.lagou.com/jobs/positionAjax.json"
        # 请求头
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.79 Safari/537.36",
            "Referer": "https://www.lagou.com/jobs/list_python",
            "Cookie": "_ga=GA1.2.2032920817.1520234065; user_trace_token=20180305151430-d90e083a-2044-11e8-9cf0-525400f775ce; LGUID=20180305151430-d90e0bf2-2044-11e8-9cf0-525400f775ce; showExpriedIndex=1; showExpriedCompanyHome=1; showExpriedMyPublish=1; hasDeliver=0; JSESSIONID=ABAAABAACBHABBIECE1AB2B1B3ED00095A40CC2532D48F6; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1520234067,1520237823,1520298106; _putrc=6F0BC7CDE26E29D5; login=true; unick=%E5%AD%99%E5%85%B0%E6%98%8C; X_HTTP_TOKEN=025791c357e801ef2f8a0ec859128372; index_location_city=%E5%85%A8%E5%9B%BD; _gid=GA1.2.1630552347.1520776825; hideSliderBanner20180305WithTopBannerC=1; gate_login_token=64abbe0a8665b9254c7694c6468bed9b47a6369148326fea; _gat=1; LGSID=20180312125843-09a6a879-25b2-11e8-b1dd-5254005c3644; PRE_UTM=; PRE_HOST=; PRE_SITE=https%3A%2F%2Fwww.lagou.com%2Fjobs%2F3859972.html; PRE_LAND=https%3A%2F%2Fwww.lagou.com%2F; TG-TRACK-CODE=index_search; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1520830726; LGRID=20180312125846-0ba0dd39-25b2-11e8-ac8c-525400f775ce; SEARCH_ID=7f67a5046cb44d64a75d7c7602496b34"
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
        print(page)
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

    def get_position_detail(self, data):
        position_id_list = []
        position_list = data['content']['positionResult']['result']
        for position in position_list:
            position_id_list.append(position['positionId'])
        print('po id', position_id_list)
        for id in position_id_list:
            try:
                url = 'https://www.lagou.com/jobs/'
                url += str(id)+'.html'
                print(url)
                html_doc = requests.get(url, headers=self.headers).text
                soup = BeautifulSoup(html_doc, 'lxml')
                bonus = soup.select('.job-advantage p')
                print('benifit:')
                for bo in bonus:
                    print(bo.text.strip())
                desc = soup.select('.job_bt p')
                print('description:')
                for de in desc:
                    print(de.text.strip())
            except Exception as e:
                print(e)


positionName_list = []
with open('position_name_tmp.txt', 'r') as f:
    for line in f.readlines():
        positionName_list += line.strip().split(',')

city_list = ['', '北京', '上海', '杭州',
             '广州', '深圳', '成都']
for city in city_list:
    try:
        for name in positionName_list:
            try:
                print('city: {} position_name: {}'.format(city, name))
                spider = LagouCrawl()
                spider.params['city'] = city
                spider.data['kd'] = name
                # import pdb
                # pdb.set_trace()
                page_num = spider.get_page_num()
                for page in range(1, page_num+1):
                    data = spider.start_crawl(page)
                    spider.get_position_detail(data)
            except:
                pass
    except:
        pass
