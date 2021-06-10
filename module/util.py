from time import time
from datetime import date
import random
import math


class Util:
  """
  현재 시간을 구하는 함수(초단위)
  """

  def get_current_time(self):
    return math.floor(time())

  """
  현재 날짜를 구하는 함수(Y-m-d)
  """

  def get_current_date(self):
    today = date.today()
    return today.strftime('%Y-%m-%d')

  """
  랜덤 초를 구하는 함수
  """

  def get_random_seconds(self, start=2, end=5):
    return random.randint(start, end)
