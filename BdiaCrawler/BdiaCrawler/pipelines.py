# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import sqlite3
import time

class BdiacrawlerPipeline:
    def process_item(self, item, spider):
        return item

class SQLite3Pipeline(object):

    #打开数据库
    def open_spider(self, spider):
        db_name = spider.settings.get('SQLITE_DB_NAME', 'result.db')

        self.db_conn = sqlite3.connect(db_name)
        self.db_cur = self.db_conn.cursor()

    #关闭数据库
    def close_spider(self, spider):
        self.db_conn.commit()
        self.db_conn.close()

    #对数据进行处理
    def process_item(self, item, spider):
        self.insert_db(item)
        return item

    #插入数据
    def insert_db(self, item):
        values = (
            str(time.strftime("%Y-%m-%d", time.localtime())),
            item['plan_departure_time'],
            item['acture_departure_time'],
            item['est_departure_time'],
            str(item['flight_company']),
            str(item['flight_number']),
            item['flight_destination'],
            item['flight_check_in'],
            item['boarding_port'],
            item['flight_stat'],
        )

        sql = 'INSERT INTO depature_flight VALUES(?,?,?,?,?,?,?,?,?,?)'
        self.db_cur.execute(sql, values)