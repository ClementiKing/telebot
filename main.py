import os
import telebot
from pymongo import MongoClient, collection
from pymongo.server_api import ServerApi

mongo_conn_str = os.getenv('mongo_conn')

client = MongoClient(mongo_conn_str, server_api=ServerApi('1'))
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)

db = client['yh']
collection = db['yh']

document = {"name": "John Doe", "age": 30}
collection.insert_one(document)

API_KEY = os.getenv('API_KEY')
bot = telebot.TeleBot(API_KEY)

@bot.message_handler(commands=['start'])
def hello(message):
  bot.send_message(message.chat.id, "欢迎使用本机器人。")

@bot.message_handler(commands=['help'])
def greet(message):
  bot.reply_to(message, "需要帮助请联系e1285213@u.nus.edu。")

bot.polling()