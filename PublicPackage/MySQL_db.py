"""
@file: MySQL_db.py
@copyright: laoZ
"""
import pymysql.cursors
import os
import configparser as cparser
from Config.HostConfig import test_host,ol_host,uat_host

# ======== 读取 DbConfig.ini mysqlconf 设置 ===========
base_dir = str(os.path.dirname(os.path.dirname(__file__)))
base_dir = base_dir.replace('\\', '/')
file_path = base_dir + "/Config/DbConfig.ini"
'''
根据Host地址读取数据库
'''

cf = cparser.ConfigParser()

cf.read(file_path)
if test_host:
    print(test_host)
    host = cf.get("test_mysql", "host")
    port = cf.get("test_mysql", "port")
    db   = cf.get("test_mysql", "db_name")
    user = cf.get("test_mysql", "user")
    password = cf.get("test_mysql", "password")
elif uat_host:
    print(test_host)
    host = cf.get("uat_mysql", "host")
    port = cf.get("uat_mysql", "port")
    db   = cf.get("uat_mysql", "db_name")
    user = cf.get("uat_mysql", "user")
    password = cf.get("uat_mysql", "password")
else :
    host = cf.get("ol_mysql", "host")
    port = cf.get("ol_mysql", "port")
    db   = cf.get("ol_mysql", "db_name")
    user = cf.get("ol_mysql", "user")
    password = cf.get("ol_mysql", "password")

# ======== MySql 基本操作 ===================
class DB:

    def __init__(self):
        try:
            # 连接到数据库
            self.connection = pymysql.connect(host=host,
                                              port=int(port),
                                              user=user,
                                              password=password,
                                              db=db,
                                              charset='utf8mb4',
                                              cursorclass=pymysql.cursors.DictCursor)
        except pymysql.err.OperationalError as e:
            print("Mysql Error %d: %s" % (e.args[0], e.args[1]))

    # 明确表数据
    def clear(self, table_name):
        # real_sql = "truncate table " + table_name + ";"
        real_sql = "delete from " + table_name + ";"
        with self.connection.cursor() as cursor:
            cursor.execute("SET FOREIGN_KEY_CHECKS=0;")
            cursor.execute(real_sql)
        self.connection.commit()

    # 插入sql语句
    def insert(self, table_name, table_data):
        for key in table_data:
            table_data[key] = "'"+str(table_data[key])+"'"
        key   = ','.join(table_data.keys())
        value = ','.join(table_data.values())
        real_sql = "INSERT INTO " + table_name + " (" + key + ") VALUES (" + value + ")"
        #print(real_sql)
        with self.connection.cursor() as cursor:
            cursor.execute(real_sql)

        self.connection.commit()

    # 删除sql语句
    def delete(self, table_name, table_data):
        for key in table_data:
            table_data[key] = "'"+str(table_data[key])+"'"
        key   = ','.join(table_data.keys())
        value = ','.join(table_data.value())
        real_sql = "DELETE FROM " + table_name + " (" + key + ") WHERE (" + value + ")"
        #print(real_sql)
        with self.connection.cursor() as cursor:
            cursor.execute(real_sql)

        self.connection.commit()

    # 更新sql语句
    def update(self, table_name, table_data):
        for key in table_data:
            table_data[key] = "'" + str(table_data[key]) + "'"
        key = ','.join(table_data.keys())
        value = ','.join(table_data.value())
        real_sql = "UPDATE" + table_name + " (" + key + ") SET (" + value + ")"
        # print(real_sql)
        with self.connection.cursor() as cursor:
            cursor.execute(real_sql)

        self.connection.commit()

    # 关闭数据库
    def close(self):
        self.connection.close()

    # 初始化数据
    def init_data(self, datas):
        for table, data in datas.items():
            self.clear(table)
            for d in data:
                self.insert(table, d)
        self.close()