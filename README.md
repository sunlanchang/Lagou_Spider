# 拉勾网爬虫与数据挖掘
## 描述
爬取拉勾网50万条职位信息，进行数据清洗，数据挖掘。
## 环境
- Ubuntu 16.04
- mac OS 10.13.3 
- MySQL
- phpMyAdmin
- Chrome
- Python3
- VScode
- Anaconda Jupyter Notebook
- DataGrip
### Python模块
- request
- BeautifulSoup
- Json
### 文件描述
- `get_position.py`爬取拉勾网的爬虫程序
- `position_name.txt`保存拉勾所有职位
## 用到的shell命令
统计文件行数
```shell
wc -l file
```
# 数据库
## 查询
- 去重查询
```sql
SELECT positionId,COUNT(DISTINCT positionId) FROM position GROUP by positionId
```
- 查询各个职位招收人数
```sql
SELECT 职位名称,COUNT(职位名称) FROM L拉勾职位表 GROUP BY 职位名称 order BY COUNT(职位名称) desc
```
## 创建数据库
```SQL
CREATE TABLE `LAGOU`.`position` ( `ID` INT NOT NULL AUTO_INCREMENT , `positionId` INT(10) NOT NULL , `positionLables` VARCHAR(20) NOT NULL , `positionName` VARCHAR(20) NOT NULL , `positionAdvantage` VARCHAR(20) NOT NULL , `firstType` VARCHAR(20) NOT NULL , `secondType` VARCHAR(20) NOT NULL , `workYear` INT(10) NOT NULL , `education` VARCHAR(20) NOT NULL , `salary` VARCHAR(20) NOT NULL , `isSchoolJob` VARCHAR(5) NOT NULL , `companyId` INT(10) NOT NULL , `companyShortName` VARCHAR(20) NOT NULL , `companyFullName` VARCHAR(20) NOT NULL , `companySize` VARCHAR(20) NOT NULL , `financeStage` VARCHAR(20) NOT NULL , `industryField` VARCHAR(20) NOT NULL , `industryLables` VARCHAR(20) NOT NULL , `createTime` VARCHAR(20) NOT NULL , `formatCreateTime` VARCHAR(20) NOT NULL , `city` VARCHAR(20) NOT NULL , `district` VARCHAR(20) NOT NULL , `businessZones` VARCHAR(20) NOT NULL , `linestaion` VARCHAR(20) NOT NULL , `stationname` VARCHAR(20) NOT NULL , PRIMARY KEY (`ID`)) ENGINE = InnoDB
```
## csv文件导入数据库
```SQL
load data local infile '/home/ubuntu//workspace/Lagou_Spider/lagou.txt'
into table position_2
fields terminated by ','  optionally enclosed by '"' escaped by '"'
lines terminated by '\n';
```
## 备份数据库
```SQL
mysqldump -u root -p database_name table_name > dump.txt
password *****
```
## 导入数据库sql文件
```SQL
mysql -u root -p database_name < dump.txt password ***** 
```
## 参考
https://www.jianshu.com/p/16cd37a5355f  
https://www.zhihu.com/search?type=content&q=%E6%8B%89%E5%8B%BE%20%E7%88%AC%E8%99%AB