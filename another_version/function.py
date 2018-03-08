import requests
import json
from params import *


def start_crawl(page, url, params, data, headers):
    data['pn'] = str(page)
    response = requests.post(
        url, params=params, data=data, headers=headers)
    data = response.content.decode('utf-8')
    dict_data = json.loads(data)
    return dict_data


def save(data, filename):
    position_list = data["content"]["positionResult"]["result"]

    col = ['positionId', 'positionLables', 'positionName', 'positionAdvantage',
           'firstType', 'secondType', 'workYear', 'education', 'salary', 'isSchoolJob', 'companyId', 'companyShortName',
           'companyFullName', 'companySize', 'financeStage', 'industryField', 'industryLables', 'createTime',
           'formatCreateTime', 'city', 'district', 'businessZones', 'linestaion', 'stationname']

    f = open(filename, 'a', encoding='utf-8')
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
