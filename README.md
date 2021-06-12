# News Reminder


> 단국대학교 1학년 1학기<br>
> 창의적사고와 코딩(SW) 수업 개인 프로젝트

<br>

* 실행방법
1. config 폴더안에 있는 config.py 파일에서 아래의 내용을 자신의 환경에 맞게 수정합니다.
```  
self.DB_HOST = 'host'
self.DB_USER = 'user_name'
self.DB_PASSWORD = 'password'
self.DB_NAME = 'db_name'
self.MAIL_SENDER = 'gmail account'
self.MAIL_APP_KEY = 'gmail mail app key'
 ```
2. 해당 디비에서 news, news_category table을 생성해줍니다.
``` 
create table news
(
    id             int auto_increment
        primary key,
    published_date date        not null,
    platform_name  varchar(50) null,
    category_name  varchar(50) not null,
    title          text        null,
    url            text        null,
    created_at     int         null
);

create table news_category
(
    id         int auto_increment
        primary key,
    name       varchar(50)          null,
    is_use     tinyint(1) default 1 null,
    url        text                 null,
    created_at int                  null
);
``` 


<br>
 
2. 터미널에서 main.py 파일을 실행합니다.
```  
python main.py
```  
<br>

* 내용

 &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;네이버 뉴스에서 카테고리별, 상위 3개의 기사들의<br>
 &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;제목과 접속링크를 이메일로 알려주는 서비스
<br><br>

* 실행결과
<img width="804" alt="스크린샷 2021-06-12 오후 5 15 34" src="https://user-images.githubusercontent.com/31758135/121770027-efe70500-cba1-11eb-82fe-5a10dd488750.png">
<img width="500" src="https://user-images.githubusercontent.com/31758135/121770057-1e64e000-cba2-11eb-8317-cf9809dd19f0.png">
