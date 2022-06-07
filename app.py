# 載入需要的模組
from flask import Flask, request, abort

from linebot import LineBotApi, WebhookHandler

from linebot.exceptions import InvalidSignatureError

from linebot.models import *
app = Flask(__name__)

# LINE 聊天機器人的基本資料
line_bot_api = LineBotApi('7XtF9lRSTx9CPRMuC5KhfYvK1WocFKNAHsRAGrYPMoq2cHEgMNmIReZaQRWHwb1TGnVE/3hOtz8jR7frRd9sck5O2gMUeA0mg52NLejJzhbqOLnyPvmK3AxiZ55i9Y6Hl9MF07qZfczyrXRoMasVqwdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('fed76c2afd22205b2ad18bb1874d2add')
line_bot_api.push_message("U28a0bd6e77b7629e05e0e63bc2d3a372", TextSendMessage(text='你可以開始了'))
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
