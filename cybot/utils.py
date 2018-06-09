# -*- coding:utf-8 -*-
import platform,os, sys, pyfiglet, math, redis, time, datetime, traceback, json
from . import configs
from pprint import pprint


class _msg(object):
	def __init__(self, api, tipo='chat'):
		self.msg = api
		self.message_id = api['message_id']

		# CHAT

		if api.get('text'):
			self.text = api['text']
		else:
			self.text = None

		if api.get('entities'):
			self.entities = api['entities']
			ent = api['entities'][0]
			self.type   = ent['type']
			self.offset = ent['offset']
			self.length = ent['length']
		else:
			self.entities = None

		if api.get('chat'):
			chat = api['chat']
			self.chat = api['chat']
			self.chat_id    = chat['id']
			self.chat_type  = chat['type']
			self.chat_title = chat['title']
			if chat.get('username'):
				self.chat_username = chat['username']
			else:
				self.username = None
		else:
			self.username = None

		if api.get('from'):
			self.from_user = api['from']
			from_user      = api['from']
			self.from_id   = from_user['id']
			self.from_first_name = from_user['first_name']
			if from_user.get('username'):
				self.from_username = from_user['username']
			if from_user.get('is_bot'):
				self.is_bot = from_user['is_bot']
			if from_user.get('language_code'):
				self.language_code = from_user['language_code']
		else:
			self.from_user = None

		if api.get('reply_to_message'):
			self.reply_to_message = api['reply_to_message']
			reply = self.reply_to_message['from']
			self.reply_first_name = reply['first_name']
			self.reply_from_id    = reply['id']
			if reply.get('username'):
				self.reply_username = reply['username']
			else:
				self.reply_username = None
		else:
			self.reply_to_message = None

		if api.get('new_chat_member'):
			self.new_chat_member = api['new_chat_member']
			self.new_chat_member_first_name = self.new_chat_member['first_name']
			self.new_chat_member_id = self.new_chat_member['id']
			if self.new_chat_member.get('username'):
				self.new_chat_member_username = self.new_chat_member['username']
			else:
				self.new_chat_member_username = None
		else:
			self.new_chat_member = None

		if api.get('left_chat_member'):
			self.left_chat_member = api['new_chat_member']
			self.left_chat_member_first_name = self.left_chat_member['first_name']
			self.left_chat_member_id = self.left_chat_member['id']
			if self.left_chat_member.get('username'):
				self.left_chat_member_username = self.left_chat_member['username']
			else:
				self.left_chat_member_username = None
		else:
			self.left_chat_member = None

class _inline(object):
	def __init__(self, api):
		self.api = api
		_api = api['from']
		self.from_first_name   = str(_api['first_name'])
		try:
			self.from_username = str(_api['username'])
		except:
			self.from_username = None
		self.id = api['id']
		self.offset  = api['offset']
		self.query   = api['query']
		self.from_id = str(_api['id'])
		self.from_is_bot = str(_api['is_bot'])
		try:
			self.from_language_code = str(_api['language_code'])
		except:
			self.from_language_code = 'nunzei'

class _callback(object):
	def __init__(self, api):
		self.api  = api
		self.data = api['data'] 
		self.chat_instance = api['chat_instance']
		self.data = str(api['data'])
		self.text = api['message']['text']
		self.date = api['message']['date']
		self.message_id = api['message']['message_id']
		try:
			self.chat_id = api['chat']['id']
		except:
			self.chat_id = api['message']['chat']['id']
		_api = api['from']
		try:
			self.from_first_name = str(_api['first_name'])
		except:
			self.from_first_name = None
		try:
			self.from_username = str(_api['username'])
		except:
			self.from_username = None
		try:
			self.from_id = str(_api['id'])
		except:
			self.from_id = None
		try:
			self.from_is_bot = str(_api['is_bot'])
		except:
			self.from_is_bot = None
		try:
			self.from_language_code = str(_api['language_code'])
		except:
			self.from_language_code = None
		_api = api['message']['chat']
		try:
			self.chat_first_name = str(_api['first_name'])
		except:
			self.chat_first_name = None
		
		self.message_chat_id = str(_api['id'])	
		self.chat_type = str(_api['type'])

		try:
			self.chat_username = str(_api['username'])
		except:
			self.chat_username = None
		_api = api['message']['from']
		try:
			self.message_from_first_name = str(_api['first_name'])
		except:
			self.message_from_first_name = None
		try:
			self.message_from_username = str(_api['username'])
		except:
			self.message_from_username = None
		try:
			self.message_from_id = str(_api['id'])
		except:
			self.message_from_id = None
		try:
			self.message_from_is_bot = str(_api['is_bot'])
		except:
			self.message_from_is_bot = None
		try:
			self.message_from_language_code = str(_api['language_code'])
		except:
			self.message_from_language_code = None

# msg obj
class Api(_msg):

	def __init__(self, api):
		super(Api, self).__init__(api)
# callback obj
class Callback(_callback):
	def __init__(self, api):
		super(Callback, self).__init__(api)
# inline obj
class Inline(_inline):
	def __init__(self, api):
		super(Inline, self).__init__(api)
# make keyboards
def keyboard(**kwargs):
	return json.dumps(args)

def makedict(**kwargs):
	return kwargs

# returt True, member is adm on chat
def is_adm(api, cmd='compare'):

	admins = getChatAdministrators(api.chat_id)
	ListAdm= [adm['user']['id'] for adm in admins]
	if cmd == 'compare':
		if (api.from_id in ListAdm or api.from_id in config.adms):
			return True
		else:
			return False
	if cmd == 'list':
		return ListAdm
	
# get the operational system 
def get_sys():
	os = platform.system()
	return os



# Clear terminal 
def clear():
	if get_sys() == 'Linux':
		clear = 'clear'
	if get_sys() == 'Windows':
		clear = 'cls'
	os.system(clear)

	
def list_dir(a):
	if get_sys() == 'Linux':
		lists = 'ls'
	if get_sys() == 'Windows':
		lists = 'dir'

	return os.system('%s %s' %(lists, a))

# exit system
def exit():
	sys.exit()

# a pyfiglet banner
def figlet(text, font='doom'):
	f = pyfiglet.Figlet(font=font)
	return f.renderText(text)

# convert filesizes
def convert(size_bytes):
	if size_bytes == 0:
		return "0B"
	size_name = ("B", "KB", "MB", "GB", "TB", "PB", "EB", "ZB", "YB")
	i = int(math.floor(math.log(size_bytes, 1024)))
	p = math.pow(1024, i)
	s = round(size_bytes / p, 2)
	return "%s %s" % (s, size_name[i])


# Ignore Old Messages
def ignore(api, Max=5):
	if config.IGNORAR_MSG == True:
		if (eval(msg(api).date)-int(time.time()))>Max:
			return
## [ VERIFY HAVE STR ITEM]
def get_str(string):
	if 'a' in string:
		return True
	if 'b' in string:
		return True
	if 'c' in string:
		return True
	if 'd' in string:
		return True
	if 'e' in string:
		return True
	if 'f' in string:
		return True
	if 'g' in string:
		return True
	if 'h' in string:
		return True
	if 'i' in string:
		return True
	if 'j' in string:
		return True
	if 'k' in string:
		return True
	if 'l' in string:
		return True
	if 'm' in string:
		return True
	if 'n' in string:
		return True
	if 'o' in string:
		return True
	if 'p' in string:
		return True
	if 'q' in string:
		return True
	if 'r' in string:
		return True
	if 's' in string:
		return True
	if 't' in string:
		return True
	if 'u' in string:
		return True
	if 'v' in string:
		return True
	if 'w' in string:
		return True
	if 'x' in string:
		return True
	if 'y' in string:
		return True
	if 'z' in string:
		return True
	else:
		return False

## [ VERIFY HAVE INT ITEM]
def get_int(ints):

	if '0' in ints:
		return True
	if '1' in ints:
		return True
	if '2' in ints:
		return True
	if '3' in ints:
		return True
	if '4' in ints:
		return True
	if '5' in ints:
		return True
	if '6' in ints:
		return True
	if '7' in ints:
		return True
	if '8' in ints:
		return True
	if '9' in ints:
		return True
	else:
		return False

# Calendar
class data:
	datas = datetime.datetime.now()

	dia   = datas.day

	mes   = datas.month

	ano	  = datas.year

	hor  = datas.hour

	segundo = datas.second

	minuto = datas.minute

	hora = '{}:{}:{}'.format(hor, minuto, segundo)
	data = "{}/{}/{}".format(dia,mes,ano)
	datetime = {'time': hora, 'date': data}

# Reboot script 
def reboot(sleep=2): # By Lucal Alberto
	time.sleep(2)
	os.execl(sys.executable, sys.executable, *sys.argv)

