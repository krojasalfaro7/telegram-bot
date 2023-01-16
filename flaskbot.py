# -*- coding: utf-8 -*-

from flask import Flask, request
from bot import BotTelegram
import telebot
import os

APP_URL = os.getenv("APP_URL")


class FlaskBot(object):

    def __init__(self):
        self.server = Flask(__name__)
        self.bot = BotTelegram()

        @self.server.route('/' + self.bot.gettoken(), methods=['POST'])
        def getmessage():
            self.bot.bot.process_new_updates([telebot.types.Update.de_json(request.stream.read().decode("utf-8"))])
            return "Estableciendo el webhook!", 200

        @self.server.route("/")
        def webhook():
            self.bot.bot.remove_webhook()
            self.bot.bot.set_webhook(url=APP_URL + self.bot.gettoken())
            return "Estableciendo el webhook!", 200

