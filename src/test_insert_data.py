# _*_ coding:utf-8 _*_

import MySQLdb

db = MySQLdb.connect("59.175.213.88", "test","clcc1229","testdb", 33067)
cursor = db.cursor()

#SQL 插入
sql="""INSERT INTO EMPLOYEE(FIRST_NAME,
         LAST_NAME, AGE, SEX, INCOME) VALUES('Mac', 'Mohan', 20, 'M', 2000)"""
         
sql1= "INSERT INTO EMPLOYEE(FIRST_NAME, \
       LAST_NAME, AGE, SEX, INCOME) \
       VALUES ('%s', '%s', '%d', '%c', '%d' )" % \
       ('Mac', 'Mohan', 20, 'F', 2000)
try:
    cursor.execute(sql1)
    db.commit()
except:
    db.rollback()

db.close()