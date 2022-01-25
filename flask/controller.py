import random
from time_format import time_format
from linebot.models import (
    TextSendMessage,
)


def SendGetoffTime(event):
    emoji = [
        {
            "index": 0,
            "productId": "5ac1bfd5040ab15980c9b435",
            "emojiId": "039"
        },
        {
            "index": 5,
            "productId": "5ac1bfd5040ab15980c9b435",
            "emojiId": "039"
        }
    ]
    punchin, getoff = time_format(event.timestamp)
    reply_str = '$成功打卡$\n上班時間 : {}\n下班時間 : {}'.format(punchin, getoff)
    text_message = TextSendMessage(text=reply_str, emojis=emoji)
    return text_message


def Undefined_Func(event):
    rnd = random.randint(0, 5)
    msg = [
        "我只會顯示上班跟下班時間",
        "來聽首音樂吧\nhttps://www.youtube.com/watch?v=DbXMjAYSa68",
        "今天你打卡了嗎",
        "真希望有提醒下班的功能",
        "要下班了嗎？",
        "小知識 :\n除了上下班回覆,其他都是罐頭訊息"
    ]
    text_message = TextSendMessage(text=msg[rnd])
    return text_message
