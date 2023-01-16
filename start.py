# -*- coding: utf-8 -*-

import os
from flaskbot import FlaskBot

if __name__ == "__main__":
    server = FlaskBot().server
    server.run(host="0.0.0.0", port=int(os.environ.get('PORT', 5000)))


# from bot import BotTelegram
#
# if __name__ == "__main__":
#     bot = BotTelegram()
#     bot.bot.polling()
