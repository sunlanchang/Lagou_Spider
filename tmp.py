import pymysql

config = {
    'host': '10.10.10.53',
    'port': 3306,
    'user': 'root',
    'password': 'qsz961225',
    'db': 'LAGOU',
          'charset': 'utf8mb4',
          'cursorclass': pymysql.cursors.DictCursor,
}

# Connect to the database
connection = pymysql.connect(**config)
