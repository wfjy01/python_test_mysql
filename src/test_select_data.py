# _*_ coding:utf-8 _*_

import MySQLdb

db = MySQLdb.connect("59.175.213.88", "test","clcc1229","testdb", 33067)
cursor = db.cursor()

sql="select * from employee \
        where income > '%d' " % (1000)

try:
    cursor.execute(sql)
    results = cursor.fetchall()
    for row in results:
          fname = row[0]
          lname = row[1]
          age = row[2]
          sex = row[3]
          income = row[4]
           # 打印结果
          print "fname=%s,lname=%s,age=%d,sex=%s,income=%d" % \
             (fname, lname, age, sex, income )
except:
    print "Error: unable to fecth data"
    
db.close()