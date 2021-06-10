from time import sleep
from module import Crawling
from module import Util

crawling = Crawling()
util = Util()

# 1. 뉴스 카테고리 url이 있는지 체크, 있다면 조회  없다면 크롤링해서 저장
is_use = 1
news_category_list = crawling.news_category_dao.select_by_is_use(is_use)
if(len(news_category_list) == 0):
  news_category_list = crawling.get_category_url()

print(news_category_list)

# 2. 뉴스 카테고리 url로 각 카테고리 별 best 3 기사 저장되어있는지 체크, 있다면 조회, 없다면 크롤링해서 저장
for category in news_category_list:
  news_list = crawling.news_dao.select_by_category_name_and_published_date(
      category.get('name'), '2021-06-11')
  if(len(news_list) == 0):
    news_list = crawling.get_news_content(
        category.get('name'), category.get('url'))
    sleep(util.get_random_seconds())
  print(news_list)


# 3. 메일 발송
