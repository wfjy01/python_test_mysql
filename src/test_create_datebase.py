# _*_ coding:utf-8 _*_

import MySQLdb

db = MySQLdb.connect("59.175.213.88", "test","clcc1229","testdb", 33067)
cursor = db.cursor()
cursor.execute("drop table if exists employee")

sql = """create table  EMPLOYEE (
         FIRST_NAME  CHAR(20) NOT NULL,
         LAST_NAME  CHAR(20),
         AGE INT,  
         SEX CHAR(1),
         INCOME FLOAT )"""

cursor.execute(sql)
db.close()
