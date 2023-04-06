import pymysql




class DB(object):
    def __init__(self):
        try:
            self.db = pymysql.connect(host='localhost', user='root', password='123456', database='watchlist')
            self.cursor = self.db.cursor()
            print('connect success')
        except:
            print('connect fail')
    # 查询
    def getData(self):
        sql = 'select * from User'