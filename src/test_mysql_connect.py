# _*_ coding:utf-8 _*_

import MySQLdb

db = MySQLdb.connect("59.175.213.88", "test","clcc1229","resource", 33067)
cursor = db.cursor()
cursor.execute("SELECT VERSION()");
data = cursor.fetchone()

print "MySql version is %s" % data

db.close()
