import os
from dotenv import load_dotenv, find_dotenv

# Loading .env variables
load_dotenv(find_dotenv())

TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
if TELEGRAM_TOKEN is None:
    raise Exception("Please setup the .env variable TELEGRAM_TOKEN.")

#PORT = int(os.environ.get('PORT', '8443'))
#HEROKU_APP_NAME = os.getenv("HEROKU_APP_NAME")

TELEGRAM_SUPPORT_CHAT_ID = os.getenv("TELEGRAM_SUPPORT_CHAT_ID")
if TELEGRAM_SUPPORT_CHAT_ID is None or not str(TELEGRAM_SUPPORT_CHAT_ID).lstrip("-").isdigit():
    raise Exception("You need to specify 'TELEGRAM_SUPPORT_CHAT_ID' env variable: The bot will forward all messages to this chat_id. Add this bot https://t.me/ShowJsonBot to your private chat to find its chat_id.")
TELEGRAM_SUPPORT_CHAT_ID = int(TELEGRAM_SUPPORT_CHAT_ID)


WELCOME_MESSAGE = "Здравствуйте, на связи поддержка МТС Developers! 🖐 Бот поможет с консультацией по подключению сервисов на МТС Developers. Специалисты технической поддержки работают по будням с 9:00 до 19:00 (по московскому времени) 👨‍💻 Пожалуйста, напишите свой вопрос, мы ответим вам в ближайшее время."
REPLY_TO_THIS_MESSAGE = "Ответьте на это сообщение."
WRONG_REPLY = "Пользователь выше не разрешает пересылать свои сообщения. Вы должны ответить на ответ бота."