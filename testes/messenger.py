
from flask import Flask, request
from pprint import pprint
from cybion import messenger

app = Flask(__name__)

ACCESS_TOKEN = "token_acess"
VERIFY_TOKEN = "teste"
bot = messenger.Bot(ACCESS_TOKEN)

def test_message(recipient_id):
    bot.sendMessage(recipient_id, 'test sendMessage')

def test_keyborad(recipient_id):
    keyboard = [dict(title='Arsenal', type='web_url', url='http://arsenal.com'),
                dict(title='Other', type='postback', payload='other'),]
    bot.sendMessage(recipient_id, 'test sendMessage, keyboards', keyboard)

def test_image(recipient_id):
    bot.sendImage(recipient_id, 'https://i.imgur.com/ttlb9aj.jpg')

def test_gif(recipient_id):
    bot.sendImage(recipient_id, 'https://media.giphy.com/media/rl0FOxdz7CcxO/giphy.gif')

##### verification 
@app.route("/", methods=['GET', 'POST'])
def hello():
    if request.method == 'GET':
        if request.args.get("hub.verify_token") == VERIFY_TOKEN:
            return request.args.get("hub.challenge"), 200
        else:
            return 'Invalid verification token', 400
    if request.method == 'POST':
        data  = request.get_json()['entry'][0]['messaging'][0]
        pprint(data)
        if data.get('message'):
            recipient_id = data['sender']['id']
            test_message(recipient_id)
            test_keyborad(recipient_id)
            test_image(recipient_id)
            test_gif(recipient_id)
                  
        return "Success", 200

if __name__ == "__main__":
    app.run(port=3000, debug=True)
