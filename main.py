import time
import telebot

funny_bot = telebot.TeleBot('6081579701:AAHlZSH98nnZmqc-KQqNv-FtUL4pmPHmW5g')
channel_name = '@Jokes_64'

f = open('data.txt', 'r', encoding='UTF-8')
jokes = f.read().split('\n')
f.close()

for joke in jokes:
    funny_bot.send_message(channel_name, joke)

    time.sleep(30)
funny_bot.send_message(channel_name, "Анекдоты закончились :-(")
