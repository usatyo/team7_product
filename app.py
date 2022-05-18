import imp
import os, random
from flask import Flask, request, abort

from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import (
    MessageEvent,
    TextMessage,
    TextSendMessage,
)
from apscheduler.schedulers.background import BackgroundScheduler
import datetime
import time
import rain_check

def sensor():
    print("scheduler is alive")

sched = BackgroundScheduler(daemon=True)
sched.add_job(sensor, 'interval', minutes=60)
sched.start()

app = Flask(__name__)

YOUR_CHANNEL_ACCESS_TOKEN = os.environ["YOUR_CHANNEL_ACCESS_TOKEN"]
YOUR_CHANNEL_SECRET = os.environ["YOUR_CHANNEL_SECRET"]

line_bot_api = LineBotApi(YOUR_CHANNEL_ACCESS_TOKEN)
handler = WebhookHandler(YOUR_CHANNEL_SECRET)

@app.route("/callback", methods=["POST"])
def callback():
    # get X-Line-Signature header value
    signature = request.headers["X-Line-Signature"]

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        print(
            "Invalid signature. Please check your channel access token/channel secret."
        )
        abort(400)

    return "OK"

# @handler.add(MessageEvent, message=TextMessage)
# def handle_message(event):
#     msg = event.message.text
#     line_bot_api.reply_message(event.reply_token, TextSendMessage(text=msg))

if __name__ == "__main__":
    app.run()

while True:
    dt_now = datetime.datetime.now()
    # if dt_now.hour == 7 and dt_now.minute == 0 and dt_now.second == 0:
    if dt_now.second == 0:
        if rain_check.rain_check():
            messages = TextSendMessage(text='今日は雨')
        line_bot_api.broadcast(messages=messages)
        print('sent')
    time.sleep(1)
    print('done')