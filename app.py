from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
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
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=event.message.text))


if __name__ == "__main__":
    app.run() 