"""
default_reply: botへmentionがあったときに、定義されたレスポンス以外はdocomo自然対話APIへ渡す
"""

from slackbot.bot import default_reply
import requests
import json
import types
import slackbot_settings

@default_reply()
def default(message):
    """
    Docomo自然対話APIから返答する
    """
    #エンドポイントの設定
    endpoint = 'https://api.apigw.smt.docomo.ne.jp/naturalChatting/v1/dialogue?APIKEY=REGISTER_KEY'
    appid = slackbot_settings.DOCOMO_APP_ID
    url = endpoint.replace('REGISTER_KEY', slackbot_settings.DOCOMO_API_KEY)
    text = message.body['text']
    #会話の入力
    payload = {'language':'ja-JP', 'botId':'Chatting','appId':appid,'voiceText':text}
    headers = {'Content-type': 'application/json'}

    #送信
    r = requests.post(url, data=json.dumps(payload), headers=headers)
    data = r.json()

    #jsonの解析
    response = data['systemText']['utterance'] #変更

    #表示
    message.reply('%s' % response)
