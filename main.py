import os
from flask import Flask, request, abort
from dotenv import load_dotenv
from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)
from time_format import time_format

load_dotenv()

app = Flask(__name__)


line_bot_api = LineBotApi(os.getenv('LINE_BOT_TOKEN'))
handler = WebhookHandler(os.getenv('LINE_BOT_SECRET'))


@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)
    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        print("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    punchin, getoff = time_format(event.timestamp)
    reply_str = '上班時間 : {punchin}\n下班時間 : {getoff}'
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=reply_str.format(punchin=punchin, getoff=getoff))
        )


if __name__ == "__main__":
    app.run()
