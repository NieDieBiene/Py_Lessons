import smtplib
import os

from pathlib import Path
from dotenv import load_dotenv

dotenv_path = Path('.env')
load_dotenv(dotenv_path)

server = smtplib.SMTP_SSL('smtp.yandex.ru', 465)
server.login(os.getenv('LOGIN'), os.getenv('PASSWORD'))

email_from = os.getenv('EMAIL')
email_to = "mind2rubbish@yandex.ru"

letter = """From: {email_from}
To: {email_to}
Subject: Приглашение!
Content-Type: text/plain charset="UTF-8"

Привет, {friend_name}! {my_name} приглашает тебя на сайт {website}!

{website} — это новая версия онлайн-курса по программированию. 
Изучаем Python и не только. Решаем задачи. Получаем ревью от преподавателя. 

Как будет проходить ваше обучение на {website}? 

→ Попрактикуешься на реальных кейсах. 
Задачи от тимлидов со стажем от 10 лет в программировании.
→ Будешь учиться без стресса и бессонных ночей. 
Задачи не «сгорят» и не уйдут к другому. Занимайся в удобное время и ровно столько, сколько можешь.
→ Подготовишь крепкое резюме.
Все проекты — они же решение наших задачек — можно разместить на твоём GitHub. Работодатели такое оценят. 

Регистрируйся → {website}  
На курсы, которые еще не вышли, можно подписаться и получить уведомление о релизе сразу на имейл."""

website = "https://dvmn.org/profession-ref-program/dunaevaksenia/pmoZg/"
name_to = "Ёжик"
name_from = "Ксюша"

letter = letter.format(email_from = email_from, email_to = email_to, my_name = name_from, friend_name = name_to, website = website)

letter = letter.encode("UTF-8")

server.sendmail(email_from, email_to, letter)
server.quit()