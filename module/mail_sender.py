import smtplib
from config import Config
from email.mime.text import MIMEText


class MailSender:
  def __init__(self, account, password):
    self.config = Config()
    self.smtp = smtplib.SMTP('smtp.gmail.com', 587)
    self.smtp.starttls()
    self.smtp.login(account, password)

  def send_message(self, to, title, content):
    message = MIMEText(content, 'html')
    message['Subject'] = title
    self.smtp.sendmail(self.config.MAIL_SENDER, to, message.as_string())
    # 세션 종료
    self.smtp.quit()
