# -*- coding: utf-8 -*-

import telebot
from utils import UtilsBot
import os

TOKEN = os.getenv("TOKEN_BOT")

class BotTelegram(object):
    """
    Clase que maneja los eventos de entrada del bot
    """

    def __init__(self):

        # Configurando con el token del bot
        self.token = TOKEN
        self.bot = telebot.TeleBot(self.token, parse_mode=None)

        # Metodo que retorna la lista
        @self.bot.message_handler(commands=['listado'])
        def getlist(message):
            try:
                lista = UtilsBot.getlist()
                titulo = message.chat.title
                self.bot.reply_to(message, "Lista Grupo: " + titulo + "\n\n" + lista)

            # Se captura el typeerro debido a imposibilidad de obtener el titulo de los grupos donde se encuentra el bot
            except TypeError:
                self.bot.reply_to(message, lista)

        # Metodo que elimina los datos de la lista
        @self.bot.message_handler(commands=['borrar'])
        def deletelist(message):
            if UtilsBot.deletelist():
                self.bot.reply_to(message, "Lista Eliminada")
            else:
                self.bot.reply_to(message, "A ocurrido un error eliminando la lista")

        # # Manejador de open
        # @self.bot.message_handler(commands=['open'])
        # def openlist(message):
        #     UtilsBot.status_flag = True
        #
        # # Manejador de open
        # @self.bot.message_handler(commands=['close'])
        # def closelist(message):
        #     UtilsBot.status_flag = False

        # Ver comandos
        @self.bot.message_handler(commands=['comandos'])
        def getcomandos(message):
            self.bot.reply_to(message, "Los comandos son: \n" +
                              # "/open para abrir la lista \n" +
                              # "/close para cerrar la lista \n" +
                              "/listado para visualizar la lista \n" +
                              "/borrar para eliminar la lista")

        # Comando no registrado
        @self.bot.message_handler(func=lambda message: True)
        def echo_all(message):
            # Verificando si esta disponible la escritura de la lista
            #is_enable = UtilsBot.status_flag

            # Si esta en open escribe, si no lo ignora
            # if is_enable:
                # Aqui es que llamo a los datos del perfil que escribe

                #if message.text.startswith("@") or message.text.startswith("Instagram.com/"):
            if message.text.startswith("@"):

                cambio = message.text.replace("@", "www.instagram.com/")
                UtilsBot.appendelem(cambio, message.from_user.first_name, message.from_user.username,
                                    message.from_user.last_name)

            elif message.text.startswith("Instagram.com/"):

                cambio = message.text.replace("Instagram.com/", "www.instagram.com/")
                UtilsBot.appendelem(cambio, message.from_user.first_name, message.from_user.username,
                                    message.from_user.last_name)

    def gettoken(self):
        return self.token
