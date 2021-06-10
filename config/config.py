class Config:
  def __init__(self):
    self.NAVER_NEWS_DOMAIN = 'https://m.news.naver.com'
    self.NAVER_NEWS_M_URL = 'https://m.news.naver.com/rankingList.nhn'
    self.CATEGORY_URL_SELECTOR = '#ct > div.rankingnews_press > div > ul > li'
    self.PLATFORM_NAVER = 'NAVER'
    self.DB_HOST = 'host'
    self.DB_USER = 'user'
    self.DB_PASSWORD = 'password'
    self.DB_NAME = 'db_name'
    self.CATEGORY_USE_LIST = ['정치', '생활', '많이본', '경제', 'IT', '사회', '세계', '연예']
