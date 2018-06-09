# -*- coding:utf-8 -*-
import cybot

bot = cybot.instance({'token': 'api_token'})

def handler(api):
    if api['text']:
        markup = dict(inline_keyboard=[
                     [dict(text='Button url', url='https://t.me/RoboTaylor')]+
                     [dict(text='Edit'   , callback_data='edit')]])
        bot.sendMessage(api['chat']['id'], 'Test Keyboard', reply_markup=markup)
def callback(api):
    data = api['data']
    api  = api['message']
    if data == 'edit':
        bot.editMessageText(chat_id=api['chat']['id'], message_id=api['message_id'], text='Edited!')

bot.start_polling(chat=handler, callback_query=callback)
while 1:
    pass
