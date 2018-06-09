#-*- coding:utf-8 -*-
import cybot

""" simple skeleto whit uses a Cybion Db similar to Redis-Server """

bot = cybot.instance({'token': 'api_token', 'db': '0'})

def handler(api):
  bot.hset('h1', 'h2', 'h3')
  get = bot.hget('h1', 'h2')
  print(get)
  
bot.start_polling(handler)
while True:
  pass
