# 更具体的特征选择、特征提取和数据分析见analysis.ipynb文件

import pandas as pd
import numpy as np
import pymysql
import jieba
import jieba.posseg as pseg
import os
import sys
from sklearn import feature_extraction
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_extraction.text import CountVectorizer

# Python连接数据库
connection = pymysql.connect(host='localhost',
                             user='root',
                             password='6865215441',
                             db='LAGOU',
                             charset='utf8',
                             cursorclass=pymysql.cursors.DictCursor)
cursor = connection.cursor()

sql = 'SELECT detail FROM `detail` limit 10'
cursor.execute(sql)

detail_list = cursor.fetchall()corpus_before = []
for detail in detail_list:
    corpus_before.append(detail['detail'])
print(corpus_before.__len__())
chrs = ['，', '。', '！', '、', '；', '：', '？', '~',
        '(', ')', '；', ';', ',', '\n', '\t', '/', '-', '.', '\'']

corpus = []
for line in corpus_before:
    for ch in chrs:
        line = line.replace(ch, '')
    Word_spilt_jieba = jieba.cut(line, cut_all=False)
    line = ' '.join(Word_spilt_jieba)
    corpus.append(line)

 # 该类会将文本中的词语转换为词频矩阵，矩阵元素a[i][j] 表示j词在i类文本下的词频
vectorizer = CountVectorizer()
# 该类会统计每个词语的tf-idf权值
transformer = TfidfTransformer()
X = vectorizer.fit_transform(corpus)
# 第一个fit_transform是计算tf-idf，第二个fit_transform是将文本转为词频矩阵
tfidf = transformer.fit_transform(X)
# 获取词袋模型中的所有词语
word = vectorizer.get_feature_names()
# 将tf-idf矩阵抽取出来，元素a[i][j]表示j词在i类文本中的tf-idf权重
weight = tfidf.toarray()
