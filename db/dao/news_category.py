from db import MysqlController


class NewsCategoryDAO(MysqlController):

  def insert(self, news_category):
    sql = 'INSERT INTO news_category (name, url, is_use, created_at) VALUES (' + \
        news_category.to_sql_str() + ')'

    self.cursor.execute(sql)
    self.connection.commit()

  def select_by_category_name(self, name):
    sql = 'SELECT * FROM news_category WHERE name LIKE \'' + name + '\''

    self.cursor.execute(sql)
    result = self.cursor.fetchall()
    return result

  def select_by_is_use(self, is_use):
    sql = 'SELECT * FROM news_category WHERE is_use = \'' + str(is_use) + '\''

    self.cursor.execute(sql)
    result = self.cursor.fetchall()
    return result
