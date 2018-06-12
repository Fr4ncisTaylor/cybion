# -*- coding:utf-8 -*-

import urllib3, json, platform, os, sys, pyfiglet, math, redis, time, datetime, traceback
from threading import Thread
from . import cor
from pprint    import pprint
from . import db, utils, configs
import flask
from flask import Flask, request, abort


datetime = utils.data.datetime

def parser(msg, _type):
	if _type == 'inline':
		return utils.Inline(msg)

	if _type == 'callback':
		return utils.Callback(msg)
	
	if _type == 'handle':
		return utils.Api(msg)

	else:
		return msg

def handler(msg, method,  _type=None):
	
	try:
		if configs.RETURN_DICT == False:
			parse = parser(msg, _type)
			method(parse)
		else:
			method(msg)
	except:
		if configs.TRACEBACK_PRINTER == True:
			traceback.print_exc()
		pass

def process(debug, msgs, chat, callback_query=None, inline_query=None, chosen_inline_result=None, shipping_query=None, pre_checkout_query=None, edited_message=None):
	if debug == True:
		pprint(msgs)
	if type(msgs) is dict:
		
		if msgs.get('message', None) is not None :
			msg  = msgs['message']
			chat = chat 
			handler(msg, chat,  _type='handle')

		elif msgs.get('edited_message', None) is not None and edited_message is not None:
			msg   = msgs['edited_message']
			_type = 'edited_message'
			chat  = edited_message
			handler(msg, chat,  _type)
		
		elif msgs.get('channel_post', None) is not None and channel_post is not None:
			msg   = msgs['channel_post']
			_type = 'channel_post'
			chat  = channel_post
			handler(msg, chat,  _type)

		elif msgs.get('edited_channel_post', None) is not None and edited_channel_post is not None:
			msg   = msgs['edited_channel_post']
			_type = 'edited_message'
			chat  = edited_channel_post
			handler(msg, chat,  _type)

		elif msgs.get('inline_query', None) is not None and inline_query is not None:
			msg   = msgs['inline_query']
			_type = 'inline_query'
			chat  = inline_query
			handler(msg, chat,  _type)

		elif msgs.get('chosen_inline_result', None) is not None and chosen_inline_result is not None:
			msg   = msgs['chosen_inline_result']
			_type = 'chosen_inline_result'
			chat  = chosen_inline_result
			handler(msg, chat,  _type)

		elif msgs.get('callback_query', None) is not None and callback_query is not None:
			msg   = msgs['callback_query']
			_type = 'callback_query'
			chat  = callback_query
			handler(msg, chat,  _type)

		elif msgs.get('shipping_query', None) is not None and shipping_query is not None:
			msg   = msgs['shipping_query']
			_type = 'shipping_query'
			chat  = shipping_query
			handler(msg, chat,  _type)

		elif msgs.get('pre_checkout_query', None) is not None and pre_checkout_query is not None:
			msg   = msgs['pre_checkout_query']
			_type = 'edited_message'
			chat  = edited_message
			handler(msg, chat,  _type)


class _bot(object):
	def __init__(self, instancia):
		self.token  = instancia['token']
		try:
			self.db = instancia['db']
		except:
			self.db = configs.DEFAULT_DB

	
class instance(_bot):
	class Th(Thread) :
		def __init__ (self, msgs, chat, callback_query, inline_query, chosen_inline_result, shipping_query, pre_checkout_query, edited_message):
			Thread.__init__(self)
			
			process(msgs, chat, callback_query, inline_query, chosen_inline_result, shipping_query, pre_checkout_query, edited_message)

	def __init__(self, instancia):
		super(instance, self).__init__(instancia)
		self.token = instancia['token']
		try:
			self.db = instancia['db']
		except:
			self.db = '0'

	
	def request(self, api_method, payload=None, method='GET'):
		http = urllib3.PoolManager()
		api = 'https://api.telegram.org/bot{}/{}?'.format(self.token, api_method)
		if method == 'GET':
			req = http.request(method, url=api, fields=payload, headers={'Content-Type': 'application/json'})
			req = json.loads(req.data.decode('utf-8'))
		
		if method == 'POST':
			req = http.request(method, url=api, fields=payload, headers={'Content-Type': 'application/json'}).json()	
			req = json.loads(req.data.decode('utf-8'))
		
		if req.get('result'):
			req = req['result']
			return req
		elif req.get('error_code'):
			print(req['description'])

		else:
			return req
		
	def getMe(self):
		return self.request('getMe')

	def sendMessage(self, chat_id, text, parse_mode=None, reply_markup=None, reply_to_message_id=None, disable_web_page_preview=None, disable_notification=None):
		payload = locals()
		return self.request('sendMessage', payload)

	def sendReply(self, api, chat_id, text, parse_mode=None, reply_markup=None, disable_web_page_preview=None, disable_notification=None):
		payload    = locals()
		message_id = api.message_id
		return self.request('sendMessage', payload)

	def forwardMessage(self, chat_id, from_chat_id, message_id, disable_notification=None):
		payload = locals()
		return self.request('forwardMessage', payload)

	def sendPhoto(self, chat_id, photo, caption=None, parse_mode=None, disable_notification=None, reply_to_message_id=None, reply_markup=None):
		payload = locals()
		return self.request('sendPhoto', payload, method='POST')

	def sendGif(self, chat_id, gif, caption=None, parse_mode=None, disable_notification=None, reply_to_message_id=None, reply_markup=None):
		payload = locals()
		return self.request('sendGif', payload, method='POST')

	def sendAudio(self, chat_id, audio, caption, duration, performer, title, parse_mode=None,  disable_notification=None,reply_to_message_id=None, reply_markup=None):
		payload = locals()
		return self.request('sendAudio', payload, method='POST')

	def sendDocument(self, chat_id, document, caption=None, duration=None, performer=None, title=None, parse_mode=None, disable_notification=None,reply_to_message_id=None, reply_markup=None):
		payload = locals()
		return self.request('sendDocument', payload, method='POST')

	def sendVideo(self, chat_id, video, duration=None, width=None, leight=None, capition=None,  supports_streaming=None, disable_notification=None, parse_mode=None, reply_to_message_id=None, reply_markup=None):
		payload = locals()
		return self.request('sendVideo', payload, method='POST')

	def sendVoice(self, chat_id, voice, caption=None,  duration=None, disable_notification=None, parse_mode=None, reply_to_message_id=None, reply_markup=None):
		payload = locals()
		return self.request('sendVoice', payload, method='POST')

	def sendVoiceNote(self, chat_id, video_note=None, duration=None, length=None, disable_notification=None,reply_to_message_id=None, reply_markup=None):
		payload = locals()
		return self.request('sendVoiceNote', payload, method='POST')

	def sendMediaGroup(self, chat_id, media=None, disable_notification=None,reply_to_message_id=None):
		payload = locals()
		return self.request('sendMediaGroup', payload, method='POST')

	def sendLocation(self, chat_id, latitude, longitude, live_period=None, disable_notification=None,reply_to_message_id=None, reply_markup=None):
		payload = locals()
		return self.request('sendLocation', payload)

	def editMessageLiveLocation(self, chat_id, latitude, longitude, live_period=None, disable_notification=None,reply_to_message_id=None, reply_markup=None):
		payload = locals()
		return self.request('editMessageLiveLocation', payload)

	def stopMessageLiveLocation(self, chat_id, latitude, longitude, live_period=None, disable_notification=None,reply_to_message_id=None, reply_markup=None):
		payload = locals()
		return self.request('stopMessageLiveLocation', payload)

	def sendVenue(self, chat_id, latitude, longitude, title, address=None, foursquare_id=None, disable_notification=None,reply_markup=None):
		payload = locals()
		return self.request('sendVenue', payload)

	def sendContact(self, chat_id, phone_number, first_name, last_name, disable_notification=None,reply_to_message_id=None, reply_markup=None):
		payload = locals()
		return self.request('sendContact', payload)

	def sendChatAction(self, chat_id, action):
		payload = locals()
		return self.request('sendChatAction', payload)

	def getUserProfilePhotos(user_id, offset=None, limit=None):
		payload = locals()
		return self.request('getUserProfilePhotos', payload)

	def getFile(self, file_id):
		payload = locals()
		return self.request('getFile', payload)

	def kickChatMember(self, chat_id, user_id, until_date=None):
		payload = locals()
		return self.request('kickChatMember', payload)

	def unbanChatMember(self, chat_id, user_id):
		payload = locals()
		return self.request('unbanChatMember', payload)

	def restrictChatMember(self, chat_id, user_id,  can_send_messages, can_send_media_messages, can_send_others_message, can_add_web_page_preview,until_date=None):
		payload = locals()
		return self.request('restrictChatMember', payload)

	def promoteChatMember(self, chat_id, user_id, can_change_info, can_post_messages, can_edit_message, can_delete_messages, can_invite_users, can_restrict_members, can_pin_messages, can_promote_members):
		payload = locals()
		return self.request('promoteChatMember', payload)

	def exportChatInviteLink(self, chat_id):
		payload = locals()
		return self.request('exportChatInviteLink', payload)

	def setChatPhoto(self, chat_id, photo):
		payload = locals()
		return self.request('setChatPhoto', payload, method='POST')

	def deleteChatPhoto(self, chat_id):
		payload = locals()
		return self.request('deleteChatPhoto', payload)

	def setChatTitle(self, chat_id, title):
		payload = locals()
		return self.request('setChatTitle', payload)

	def setChatDescription(self, chat_id, description):
		payload = locals()
		return self.request('setChatDescription', payload)

	def pinChatMessage(self, chat_id, message_id, disable_notification):
		payload = locals()
		return self.request('pinChatMessage', payload)

	def unpinChatMessage(self, chat_id):
		payload = locals()
		return self.request('unpinChatMessage', payload)

	def leaveChat(self, chat_id):
		payload = locals()
		return self.request('leaveChat', payload)

	def getChat(self, chat_id):
		payload = locals()
		return self.request('getChat', payload)

	def getChatAdministrators(self, chat_id):
		payload = locals()
		return self.request('getChatAdministrators', payload)

	def getChatMembersCount(self, chat_id):
		payload = locals()
		return self.request('getChatMembersCount', payload)

	def getChatMember(self, chat_id, user_id):
		payload = locals()
		return self.request('getChatMember', payload)

	def setChatStickerSet(self, chat_id, sticker_set_name):
		payload = locals()
		return self.request('setChatStickerSet', payload)

	def deleteChatStickerSet(self, chat_id):
		payload = locals()
		return self.request('deleteChatStickerSet', payload)

	def answerCallbackQuery(self, callback_query_id, text=None, show_alert=None, url=None,cache_time=None):
		payload = locals()
		return self.request('answerCallbackQuery', payload)

	def answerShippingQuery(self, shipping_query_id, ok, shipping_options=None, error_message=None):
		payload = locals()
		return self.request('answerShippingQuery', payload)

	def answerPreCheckoutQuery(self, pre_checkout_query_id, ok, error_message=None):
		payload = locals()
		return self.request('answerPreCheckoutQuery', payload)

	def editMessageText(self, chat_id, message_id, text, parse_mode=None, disable_web_page_preview=None, reply_markup=None):
		payload = locals()
		return self.request('editMessageText', payload)

	def editMessageCaption(self, chat_id, message_id, caption=None, parse_mode=None, reply_markup=None):
		payload = locals()
		return self.request('editMessageCaption', payload)

	def editMessageReplyMarkup(self, chat_id, message_id, reply_markup=None):
		payload = locals()
		return self.request('editMessageReplyMarkup', payload)

	def deleteMessage(self, chat_id, message_id):
		payload = locals()
		return self.request('deleteMessage', payload)

	def sendSticker(self, chat_id, sticker, disable_notification=None, reply_to_message_id=None, reply_markup=None):
		payload = locals()
		return self.request('sendSticker', payload)

	def getStickerSet(self, name):
		payload = locals()
		return self.request('getStickerSet', payload)

	def uploadStickerFile(self, user_id, png_sticker):
		payload = locals()
		return self.request('uploadStickerFile', payload)

	def createNewStickerSet(self, user_id, name, title, png_sticker, emojis, contains_masks=None, mask_position=None):
		payload = locals()
		return self.request('createNewStickerSet', payload)

	def addStickerToSet(self, user_id, name, png_sticker, emojis, mask_position=None):
		payload = locals()
		return self.request('addStickerToSet', payload)

	def setStickerPositionInSet(self, sticker, position):
		payload = locals()
		return self.request('setStickerPositionInSet', payload)

	def deleteStickerFromSet(sticker):
		payload = locals()
		return self.request('deleteStickerFromSet', payload)

	def answerInlineQuery(self, inline_query_id, results, cache_time=None, is_personal=None, next_offset=None, switch_pm_text=None, switch_pm_parameter=None):
		payload = locals()
		return self.request('answerInlineQuery', payload)

	def getUpdates(self, offset=None, limit=None, timeout=None, allowed_updates=None):
		payload = locals()
		return self.request('getUpdates', payload)

	def download_file(self, file_id, destino):
		file = getFile(file_id)
		url  = 'https://api.telegram.org/file/bot%s/%s' % (token, file)
		req  = requests.open(url)
		with open(destino, 'wb') as file:
			file.write(re.content)
		return 'file download to %s' % (destino)
	def setWebhook(self, url, certificate=None, max_conections=None, allowed_updates=None):
		payload = {'url': url+'/webhook/telegram', 'certificate': certificate, 'allowed_updates':allowed_updates}
		return self.request('setWebhook', payload)

	def deleteWebhook(self):
		return self.request('deleteWebhook')

	def getWebhookInfo(self):
		return self.request('getWebhookInfo')

	def start_paralelo(self, chat, callback_query=None, inline_query=None, chosen_inline_result=None, shipping_query=None, pre_checkout_query=None, edited_message=None, sleep=0.1, offset=None, timeout=20, allowed_updates=None):
		threads = []
		while 1 :
			try:
				threads.append(self.getUpdates(offset))
				if threads != []:
					msgs = threads[-1]
					t = self.Th(msgs, chat, callback_query, inline_query, chosen_inline_result, shipping_query, pre_checkout_query, edited_message)
					t.daemon = configs.THREADS_DAEMON
					t.start()
					try   :offset = msgs['update_id'] + 1
					except:offset = 0
					del threads[:]
			except :traceback.print_exc()
			finally:time.sleep(sleep)

	
	def start_polling(self, chat, daemon=True, callback_query=None, inline_query=None, chosen_inline_result=None, shipping_query=None, pre_checkout_query=None, edited_message=None, sleep=0.1, offset=None, timeout=20, allowed_updates=None):
		while 1:
			try:
				result = self.getUpdates(offset=offset, timeout=timeout, allowed_updates=allowed_updates)
				allowed_updates = None
				if result != []:
					for msg in result:
						#t = self.Th(msg, chat, callback_query, inline_query, chosen_inline_result, shipping_query, pre_checkout_query, edited_message)
						#t.daemon = daemon
						#t.start()
						process(msg, chat, callback_query, inline_query, chosen_inline_result, shipping_query, pre_checkout_query, edited_message)
						try   :offset = msg['update_id'] + 1
						except:offset = 0
			except :traceback.print_exc()
			finally:time.sleep(sleep)
	def start_webhook(self, webhook_url, chat, callback_query=None, inline_query=None, chosen_inline_result=None, shipping_query=None, pre_checkout_query=None, edited_message=None, debug=None):
		print(cor.lg_red+'Webhook status: '+cor.lg_white+str(self.setWebhook(webhook_url))+cor.lg_green)
		app = Flask(__name__)
		@app.route('/webhook/telegram', methods=['POST'])
		def webhook():		
			msg = request.json
			process(debug, msg, chat, callback_query, inline_query, chosen_inline_result, shipping_query, pre_checkout_query, edited_message)
			return  '',200
			

		@app.errorhandler(404)
		def server_error(e):
			return flask.Response(status=200)

		app.run(port='3001')


	def stop(self, Time=0.1):
		time.sleep(Time)
		os.execl(sys.executable, sys.executable, '--version')

	def is_adm(self, api, cmd='compare'):

		admins = self.getChatAdministrators(api.chat_id)
		ListAdm= [adm['user']['id'] for adm in admins]
		if (int(api.from_id) in ListAdm):
			return True

		else:
			return False

		
	def delete(self, name):
		con  = self.db
		try:
			if utils.get_sys() =='Windows':
				pasta = 'cybot\\db\\database\\{con}\\'.format(con=con, hashs=hashs)
			if utils.get_sys() == 'Linux':
				pasta = 'cybot/db/database/{con}/'.format(con=con, hashs=hashs)
			file = pasta+'{name}.cb'.format(name=name)
			open(file).read()
			exist = True
		except:
			exist = False
			return utils.makedict(code=False, message="hash does't exist", db=con, datetime=datetime)
		
		if exist == True:
			try:
				os.remove(file)
				return utils.makedict(code=True, message='sucess!', db=con, datetime=datetime)
			except:
				return utils.makedict(code=False, db=con, datetime=datetime)

	def hdelete(self,hashs,name):
		con = self.db
		if utils.get_sys() =='Windows':
			pasta = 'cybot\\db\\database\\{con}\\{hashs}\\'.format(con=con, hashs=hashs)
		if utils.get_sys() == 'Linux':
			pasta = 'cybot/db/database/{con}/{hashs}/'.format(con=con, hashs=hashs)
		try:
			file = pasta+'{name}.cb'.format(name=name)
			open(file).read()
			exist = True
		except:
			exist = False
			return utils.makedict(code='False', message="hash does't exist",db=con, datetime=datetime)
		if exist == True:
			try:
				os.remove(file)
				return utils.makedict(code='True', message='sucess!', db=con, datetime=datetime)
			except:
				return utils.makedict(code='False', db=con, datetime=datetime)

	def save(self, name, args):
		content = str(args)

		con = self.db
		if utils.get_sys() =='Windows':
			pasta = 'cybot\\db\\database\\{con}\\'.format(con=con )
		if utils.get_sys() == 'Linux':
			pasta = 'cybot/db/database/{con}/'.format(con=con)
		file = pasta+'{name}.cb'.format(con=con, name=name)
		try:
			with open(file, 'w') as arquivo:
				arquivo.write(content)
			return utils.makedict(code=True, db=con, hash=name, args=args, datetime=datetime)
		except:
			return utils.makedict(message=False, db=con, hash=name, args=args, datetime=datetime)
	
	def hsave(self, hashs, name, args):
		content = str(args)
		hashs   = str(hashs)
		con   = self.db
		if utils.get_sys() =='Windows':
			pasta = 'cybot\\db\\database\\{con}\\{hashs}\\'.format(con=con, hashs=hashs)
		if utils.get_sys() == 'Linux':
			pasta = 'cybot/db/database/{con}/{hashs}/'.format(con=con, hashs=hashs)
		try:
			os.listdir(pasta)
		except:
			os.system('mkdir %s' %(pasta))

		file = 'cybot/db/database/{con}/{hashs}/{name}.cb'.format(con=con, hashs=hashs, name=name)
		try:
			with open(file, 'w') as arquivo:
				arquivo.write(content)
			return str(utils.makedict(code=True, db=con, hash=(hashs, name), args=args, datetime=datetime))
		except:
			return str(utils.makedict(message=False, db=con, hash=(hashs, name), args=args, datetime=datetime))
	
	def hget(self, hashs, name):
		con = self.db
		if utils.get_sys() =='Windows':
			pasta = 'cybot\\db\\database\\{con}\\{hashs}\\'.format(con=con, hashs=hashs)
		if utils.get_sys() == 'Linux':
			pasta = 'cybot/db/database/{con}/{hashs}/'.format(con=con, hashs=hashs)

		file = pasta+'{name}.cb'.format(con=con, hashs=hashs, name=name)
		try:
			with open(file, 'r') as arquivo:
				return utils.makedict(code=True, message=arquivo.read(), db=con, hash=(hashs, name), datetime=datetime)
		except:
			return utils.makedict(code=False, message=arquivo.read(), db=con, hash=(hashs, name), datetime=datetime)

	def hgetall(self, hashs):
		con = self.db
		if utils.get_sys() =='Windows':
			pasta = 'cybot\\db\\database\\{con}\\{hashs}\\'.format(con=con, hashs=hashs)
		if utils.get_sys() == 'Linux':
			pasta = 'cybot/db/database/{con}/{hashs}/'.format(con=con, hashs=hashs)


		lista = []
		count = 0
		for files in os.listdir(pasta):
			count +=1
			with open(pasta+files, 'r') as arquivo:
				lista.append({files: arquivo.read()},)	
		return utils.makedict(code=True, total=count, message=lista, db=con, hash=hashs, datetime=datetime)
		#except:
		#	return makedict(code=False, message=arquivo.read(), db=con, hash=(hashs, name), datetime=datetime)

	def get(self, name):
		con = self.db
		if utils.get_sys() =='Windows':
			pasta = 'cybot\\db\\database\\{con}\\'.format(con=con)
		if utils.get_sys() == 'Linux':
			pasta = 'cybot/db/database/{con}/'.format(con=con)

		file = pasta+'{name}.cb'.format(name=name)
		try:
			with open(file, 'r') as arquivo:
				return utils.makedict(code=True, message=arquivo.read(), db=con, hash=name, datetime=datetime)
		except:
			return utils.makedict(code=False, message="Hash unknown", db=con, hash=name, datetime=datetime)

	def set(self, k1, k2):
		return self.save(k1, k2)

	def hset(self, k1, k2, k3):
		return self.hsave(k1, k2, k3)

	def rm(self, k1):
		return self.delete(k1)