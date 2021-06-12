import requests

from bs4 import BeautifulSoup
from module import Util
from config import Config
from db.model import News
from db.model import NewsCategory
from db.dao import NewsCategoryDAO
from db.dao import NewsDAO


class Crawling:
  def __init__(self):
    self.util = Util()
    self.config = Config()
    self.news_category_dao = NewsCategoryDAO(
        self.config.DB_HOST, self.config.DB_USER, self.config.DB_PASSWORD, self.config.DB_NAME)
    self.news_dao = NewsDAO(self.config.DB_HOST, self.config.DB_USER,
                            self.config.DB_PASSWORD, self.config.DB_NAME)

  """
  네이버 뉴스에서 카테고리 별 url을 구해
  배열에 저장한 후 리턴하는 함수
  """

  def get_category_url(self):
    category_url_dictionary = {}
    category_cnt = 0

    response = requests.get(self.config.NAVER_NEWS_M_URL)
    html = response.text
    parsed_html = BeautifulSoup(html, 'html.parser')

    for category_info in parsed_html.select('.section_list li'):
      is_use = 0

      category_name = category_info.find('a').text
      category_name = category_name.replace(' ', '')
      category_url = category_info.find('a').get('href')

      if 'http' not in category_url:
        category_url = self.config.NAVER_NEWS_DOMAIN + category_url

      if category_name in self.config.CATEGORY_USE_LIST:
        is_use = 1
        category_url_dictionary[category_name] = category_url

      self.save_news_category(category_name, category_url, is_use)

    return category_url_dictionary
    # print(category_url_dictionary)

  """
  카테고리 별 url 마다 best 3위 기사를 수집해 
  DB에 저장하는 함수
  """

  def get_news_content(self, category_name, category_url):
    response = requests.get(category_url)
    html = response.text
    parsed_html = BeautifulSoup(html, 'html.parser')
    news_list = []

    for news_data in parsed_html.select('#_headlineFlicking div div:nth-child(1) div .sh_body ul li'):
      if(len(news_data['class']) == 1):
        continue

      news_title = news_data.select('.sh_text a')[0].text
      news_title = news_title.replace('\'', '')
      news_title = news_title.replace('\"', '')
      news_url = news_data.select('.sh_text a')[0].get('href')

      news = self.save_news(self.config.PLATFORM_NAVER,
                            category_name, news_title, news_url)
      news_list.append(news)

    return news_list

  """
  news 객체에 데이터를 담아
  DB에 insert 하는 함수 
  """

  def save_news(self, platform_name, category_name, news_title, news_url):
    news = News()
    news.published_date = self.util.get_current_date()
    news.platform_name = platform_name
    news.category_name = category_name
    news.title = news_title
    news.url = news_url
    news.created_at = self.util.get_current_time()

    self.news_dao.insert(news)

    return news

  """
  news_category 객체에 데이터를 담아
  DB에 insert 하는 함수 
  """

  def save_news_category(self, name, url, is_use):
    news_category = NewsCategory()
    news_category.name = name
    news_category.url = url
    news_category.is_use = is_use
    news_category.created_at = self.util.get_current_time()

    self.news_category_dao.insert(news_category)
