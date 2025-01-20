import smtplib
import os
from dotenv import load_dotenv
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


load_dotenv()

smtpObj = smtplib.SMTP('smtp.yandex.ru', 587)

smtpObj.starttls()
smtpObj.login(os.getenv('EMAIL_HOST_USER'), os.getenv('EMAIL_HOST_PASSWORD'))

# Создание объекта сообщения
msg = MIMEMultipart()

# Настройка параметров сообщения
msg["From"] = os.getenv('EMAIL_HOST_USER')
msg["To"] = "askaryaparov@yandex.ru"
msg["Subject"] = "Тестовое письмо 📧"

# Добавление текста в сообщение
text = "FFFFFFFFFFFFFFF"
msg.attach(MIMEText(text, "plain"))

# Отправка письма
smtpObj.sendmail(os.getenv('EMAIL_HOST_USER'), "askaryaparov@yandex.ru", msg.as_string())

# Закрытие соединения
smtpObj.quit()