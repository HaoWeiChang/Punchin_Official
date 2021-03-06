import os
from flask import Flask, request, abort
from dotenv import load_dotenv
from controller import (
    SendGetoffTime,
    Undefined_Func
)
from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage
)


load_dotenv()

app = Flask(__name__)

print(os.getenv('LINE_BOT_TOKEN'), os.getenv('LINE_BOT_SECRET'))
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
        print("Please check your channel access token/channel secret.")
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    dict = {
        '上班！!': SendGetoffTime
    }
    if event.message.text not in dict:
        text_message = Undefined_Func(event)
    else:
        text_message = dict.get(event.message.text, None)(event)

    line_bot_api.reply_message(
        event.reply_token,
        text_message
    )


if __name__ == "__main__":
    app.run(port=5000)
