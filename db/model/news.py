from io import StringIO


class News:
  def __init__(self):
    self.id = 0
    self.published_date = ''
    self.platform_name = ''
    self.category_name = ''
    self.title = ''
    self.url = 0
    self.created_at = 0

  def to_sql_str(self):
    sql_str = '\'' + self.published_date + '\',\'' + self.platform_name + '\',\'' + \
        self.category_name + '\',\'' + self.title + \
        '\',\'' + self.url + '\',\'' + str(self.created_at) + '\''

    return sql_str
