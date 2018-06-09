# -*- coding:utf-8 -*-
import cybot

""" simple skeleto whit use cybot webhook """

bot = cybot.instance({'token': 'api_token'})

def handler(api):
  if api.get('text'):
    bot.sendMessage(99999999, 'Hello World!')

bot.start_webhook(handler)
