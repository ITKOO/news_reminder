from db import MysqlController


class NewsDAO(MysqlController):

  def insert(self, news):
    sql = 'INSERT INTO news (published_date, platform_name, category_name, title, url, created_at) VALUES (' + \
        news.to_sql_str() + ')'

    print(sql)
    self.cursor.execute(sql)
    self.connection.commit()

  def select_by_category_name_and_published_date(self, category_name, published_date):
    sql = 'SELECT * FROM news WHERE category_name LIKE \'' + \
        category_name + '\' AND published_date like \'' + published_date + '\''

    self.cursor.execute(sql)
    result = self.cursor.fetchall()
    return result
