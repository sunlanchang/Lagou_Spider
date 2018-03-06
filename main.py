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
        self.page = 1
        # 表单数据
        self.data = {
            "first": True,
            "pn": 1,
            "kd": 'python'
        }

    def start_crawl(self):
        response = requests.post(
            self.url, params=self.params, data=self.data, headers=self.headers)
        data = response.content.decode('utf-8')
        dict_data = json.loads(data)
        for i in range(0, 15):
            positionId = dict_data['content']['positionResult']['result'][i]['positionId']
            print(i)
            print(positionId)

        # P = 0
        # with open("data1.txt", "a", encoding="utf-8") as f:
        #     P += 1
        #     f.write("page: "+str(P)+"\n")
        #     f.write(data)


if __name__ == '__main__':
    spider = LagouCrawl()
    spider.start_crawl()
    # for page in range(1, 31):
    #     spider.page = page
    #     spider.start_crawl()
    #     print("page:", page)
