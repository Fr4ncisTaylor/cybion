# -*- coding:utf-8 -*-
import cybot

""" simple skeleto whit use cybot webhook """

bot = cybot.instance({'token': 'api_token'})

def handler(api):
  if api.get('text'):
    bot.sendMessage(api['chat']['id'], 'Hello World!')

url = 'https://my.webhook.url.com'
bot.start_webhook(webhook_url=url, chat=handler)
while 1:
  pass
