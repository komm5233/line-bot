# import random

from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage, StickerSendMessage
)

app = Flask(__name__)

line_bot_api = LineBotApi('OMBJu7FTomQOwfLVb4naq3NBZUEOOwmQJuFldrdKurtns8j1LRypVj0maeXjDksJ+/g+rpU8MoLCo3IgBEK78jq5MmeyCVarLQyOKEobp+UXwcAc/Qk8Z8/Od1kBIm8M5n5dSvu5idBdVyjwGpPIuwdB04t89/1O/w1cDnyilFU=') # YOUR_CHANNEL_ACCESS_TOKEN
handler = WebhookHandler('7780733e0f02813fa5a933d2ea616e9b') # YOUR_CHANNEL_SECRET


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
    msg = event.message.text
    r = '供沙小拉?'
    if '給我貼圖' in msg:
        # ran = random.randint(17839, 17878)
        sticker_message = StickerSendMessage(
            package_id = '446',
            sticker_id = '1988'
        )
        line_bot_api.reply_message(
            event.reply_token,
            sticker_message)

        return

    if msg in ['hi', 'Hi']:
        r = 'hi'
    elif msg == '你吃飯沒':
        r = '還沒'
    elif msg == '你是誰':
        r = '這裡是群聊'
    elif msg in ['你在幹嘛', '在幹嘛']:
        r = '在想尼^0^'
    elif '快到了' in msg:
        r = '那我下去幫你拿東西'
    elif '晚安' in msg:
        r = '睡屁睡'

    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=r))


if __name__ == "__main__":
    app.run() 