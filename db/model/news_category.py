from io import StringIO


class NewsCategory:
  def __init__(self):
    self.id = 0
    self.name = ''
    self.url = ''
    self.is_use = 0
    self.created_at = 0

  def to_sql_str(self):
    sql_str = '\'' + self.name + '\',\'' + \
        self.url + '\', \'' + str(self.is_use) + \
        '\', \'' + str(self.created_at) + '\''
    return sql_str
