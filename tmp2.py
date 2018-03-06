import requests
import json
from __future__ import print_function


class LagouCrawl(object):

    def __init__(self):
        self.url = "https://www.lagou.com/jobs/positionAjax.json"
        # 请求头
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.79 Safari/537.36",
            "Referer": "https://www.lagou.com/jobs/list_python"
        }
        # 查询字符串
        self.params = {
            "city": "深圳",
            "needAddtionalResult": False,
            "isSchoolJob": 0
        }
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
        print(dict_data)


if __name__ == '__main__':
    spider = LagouCrawl()
    spider.start_crawl()
