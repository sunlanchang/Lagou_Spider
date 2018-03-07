from function import *


city = '北京'
keyword = 'C++'
page = 30
url, headers, params, data = get_url_headers_params_data()
f = open('position.txt', 'r', encoding='utf-8')
for line in f.readlines():
    city_keyword = line.strip().split(',')
    city, keyword = city_keyword[0], city_keyword[1]
    params['city'] = city
    data['kd'] = keyword
    for page in range(1, page+1):
        res_data = start_crawl(page, url, params, data, headers)
        save(res_data, params['city']+data['kd']+'.txt')
        print("page:", page)
