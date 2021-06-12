import pymysql


class MysqlController:
  def __init__(self, host, user, password, db_name):
    self.connection = pymysql.connect(
        host=host, port=3306, user=user, password=password, db=db_name, 
        charset='utf8', autocommit=True, cursorclass=pymysql.cursors.DictCursor)
    self.cursor = self.connection.cursor()


