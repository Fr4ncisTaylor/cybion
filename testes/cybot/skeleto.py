#-*- coding:utf-8 -*-
import cybot

""" Simple skeleto to run bot with use cybot """

bot = cybot.instance({'token': 'telegram_api_token'})

def handler(api):
  if api.get('text'):
    bot.sendMessage(99999999, 'Hello World!')

bot.start(handler)
while True:
  pass
