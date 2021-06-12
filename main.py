from module import MailSender
from time import sleep
from module import Crawling
from module import MailSender
from module import Util
from config import Config
from db.model import News
from db.model import NewsCategory

crawling = Crawling()
config = Config()
mail_sender = MailSender(config.MAIL_SENDER, config.MAIL_APP_KEY)
util = Util()

# 메일 제목 및 내용 선언 
current_date = util.get_current_date()
to = 'itkoo2000@gmail.com' # 메일을 보낼 사람
mail_title = '[' + current_date + '] 네이버 뉴스 리마인더'
mail_content = ''

# 1. 뉴스 카테고리 url이 있는지 체크, 있다면 조회  없다면 크롤링해서 저장
is_use = 1
news_category_list = crawling.news_category_dao.select_by_is_use(is_use)
if(len(news_category_list) == 0):
  print('뉴스 카테고리 데이터가 존재하지않습니다 ... 새로 데이터를 수집합니다 ...')
  news_category_list = crawling.get_category_url()
else:
  print('뉴스 카테고리 데이터가 존재합니다 ... ')

# 2. 뉴스 카테고리 url로 각 카테고리 별 best 3 기사 저장되어있는지 체크, 있다면 조회, 없다면 크롤링해서 저장
for category in news_category_list:
  if isinstance(category, str):
    category_name = category
    category_url = news_category_list.get(category_name)
  else:
    category_name = category.get('name')
    category_url = category.get('url')
  
  news_list = crawling.news_dao.select_by_category_name_and_published_date(category_name, current_date)
  if(len(news_list) == 0):
    print(current_date, ',', category_name, '에 해당하는 뉴스 데이터가 존재하지않습니다 ... 새로 데이터를 수집합니다 ...')
    news_list = crawling.get_news_content(category_name, category_url)
    sleep(util.get_random_seconds())
  else:
    print(current_date, ',', category_name, '에 해당하는 뉴스 데이터가 존재합니다 ... ')

  # 메일 내용 생성
  mail_content += '<h2>' + category_name + '</h2>'
  mail_content += '<ul>'
  for news in news_list:
    if isinstance(news, dict):
      mail_content += '<li><a href=\'' + news.get('url') + '\'>' + news.get('title') + '</a></li>'
    else:
      mail_content += '<li><a href=\'' + news.url + '\'>' + news.title + '</a></li>'
  mail_content += '</ul><br>'
  

# 3. 메일 발송
print(current_date, '의 뉴스리마인더 메일을 발송합니다 ... ')
mail_sender.send_message(to, mail_title, mail_content)
print('메일 발송이 완료되었습니다 ...')
