# 載入需要的模組
from __future__ import unicode_literals
import os

from flask import Flask, request, abort

from linebot import LineBotApi, WebhookHandler

from linebot.exceptions import InvalidSignatureError

app = Flask(__name__)

# LINE 聊天機器人的基本資料
line_bot_api = LineBotApi('7XtF9lRSTx9CPRMuC5KhfYvK1WocFKNAHsRAGrYPMoq2cHEgMNmIReZaQRWHwb1TGnVE/3hOtz8jR7frRd9sck5O2gMUeA0mg52NLejJzhbqOLnyPvmK3AxiZ55i9Y6Hl9MF07qZfczyrXRoMasVqwdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('fed76c2afd22205b2ad18bb1874d2add')
# 接收 LINE 的資訊
@app.route("/callback", methods=['POST'])
def callback():
    signature = request.headers['X-Line-Signature']

    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'OK'

if __name__ == "__main__":
    app.run()
#訊息傳遞區塊
##### 基本上程式編輯都在這個function #####
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    message = TextSendMessage(text=event.message.text)
    line_bot_api.reply_message(event.reply_token,message)

#主程式
import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
