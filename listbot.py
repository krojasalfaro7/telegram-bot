# -*- coding: utf-8 -*-

from ormbot import ORMBot


class ListBot(object):
    """
    Clase utils para el manejo de funciones correlativas al bot
    """

    def __init__(self):
        # Bandera que indica si se puede escribir o no en la lista
        self.status_flag = False

    @property
    def status_flag(self):
        return self.status_flag

    @status_flag.setter
    def status_flag(self, flag):
        self.status_flag = flag

    @staticmethod
    def getlist():
        """
        Metodo estatico que retorna la lista mendiante el contexto pasado como paramtero estilo filtro
        :return:
        """
        try:
            lista = ORMBot.getrecord("name")
            if len(lista) > 0:
                lista_formateada = list(map(lambda elem: "{number}) {name}"
                                            .format(number=elem[0]+1, name=elem[1][0]), enumerate(lista)))
                return "\n".join(lista_formateada)
            else:
                return "Lista vacia"
        except Exception as e:
            return "A ocurrido un error obteniendo la lista, por favor intente nuevamente"

    @staticmethod
    def deletelist():
        """
        Metodo estatico que retorna la lista mendiante el contexto pasado como paramtero
        :return:
        """
        try:
            ORMBot.deleteall()
            return True
        except Exception as e:
            return False

    @staticmethod
    def appendelem(elem):

        try:
            ORMBot.save(elem)
            return True
        except Exception as e:
            return False
