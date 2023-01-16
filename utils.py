# -*- coding: utf-8 -*-
from ormbot import ORMBot


class UtilsBot(object):
    """
    Clase utils para el manejo de funciones correlativas al bot
    """

    # def __init__(self):
    #     # Bandera que indica si se puede escribir o no en la lista
    #     self.status_flag = False
    #
    # @property
    # def status_flag(self):
    #     return self.status_flag
    #
    # @status_flag.setter
    # def status_flag(self, flag):
    #     self.status_flag = flag

    @staticmethod
    def getlist():
        """
        Metodo estatico que retorna la lista mendiante el contexto pasado como paramtero estilo filtro
        :return: 
        """
        try:
            res = ORMBot.getall()
            lista = list(map(lambda x: x[1], res))
            lista_enumerada = list(enumerate(lista))
            lista_enumerada_formateada = list(map(lambda x: "{numero}) {valor}".format(
                numero=x[0]+1, valor=x[1]), lista_enumerada))

            lista_definitiva = "\n\n".join(lista_enumerada_formateada)

            if len(lista_definitiva) < 1:
                return "Lista vacia"
            else:
                return lista_definitiva
        except Exception as e:
            return "A ocurrido un error obteniendo la lista, por favor intente nuevamente."

    @staticmethod
    def deletelist():
        """
        Metodo estatico que retorna la lista mendiante el contexto pasado como paramtero
        :return:
        """

        if ORMBot.deleteall():
            return "Se ha eliminado la lista satisfactoriamente."
        else:
            return "A ocurrido un error eliminando la lista."


    @staticmethod
    def appendelem(elem, name, username, last_name):

        try:
            if username is None and last_name is None:
                # Aqui ordene la lista
                ORMBot.save(name + ": " + elem)
            elif name is None and last_name is None:
                ORMBot.save("@" + username + ": " + elem)
            elif username is None and name is None:
                ORMBot.save(last_name + ": " + elem)
            elif username is None:
                ORMBot.save(name + " " + last_name + ": " + elem)
            elif last_name is None:
                ORMBot.save("@" + username + " / " + name + ": " + elem)
            elif name is None:
                ORMBot.save("@" + username + " / " + last_name + ": " + elem)
            else:
                ORMBot.save("@" + username + " / " + name + " " + last_name + ": " + elem)

            return True
        except Exception as e:
            return False
