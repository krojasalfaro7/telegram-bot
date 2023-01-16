# -*- coding: utf-8 -*-

import os
import psycopg2

#DATABASE_URL = os.environ['DATABASE_URL']
#DATABASE_URL = "postgres://oxkeswxrrijeaq:9a796885f1af398e95ffda8af5d17024780df60fbe2df887990814c15388244f@ec2-34-202-65-210.compute-1.amazonaws.com:5432/d3ru22v5nu1v81"
DATABASE_URL = os.getenv('DATABASE_URL')


class ORMBot(object):

    @staticmethod
    def getall():

        try:
            conn = psycopg2.connect(DATABASE_URL, sslmode='require')
            cur = conn.cursor()
            cur.execute("""select * from public.bot""")
            query = cur.fetchall()
        except psycopg2.DatabaseError as e:
            query = "A ocurrido un error recuperando la lista"
        finally:
            cur.close()
            conn.close()
            return query

    @staticmethod
    def getrecord(*args):

        try:
            conn = psycopg2.connect(DATABASE_URL, sslmode='require')
            cur = conn.cursor()
            cur.execute("""select %s from public.bot;""" % ",".join(args))
            query = cur.fetchall()
        except psycopg2.DatabaseError as e:
            query = "A ocurrido un error recuperando la lista"
        finally:
            cur.close()
            conn.close()
            return query

    @staticmethod
    def save(value):

        try:
            conn = psycopg2.connect(DATABASE_URL, sslmode='require')
            cur = conn.cursor()
            cur.execute("""insert into public.bot(name) values('%s');""" % value)
            conn.commit()
        except psycopg2.DatabaseError as e:
            return False
        finally:
            cur.close()
            conn.close()
            return True

    def update(self):
        return

    @staticmethod
    def deleteall():

        try:
            conn = psycopg2.connect(DATABASE_URL, sslmode='require')
            cur = conn.cursor()
            cur.execute("""delete from public.bot;""")
            conn.commit()
        except psycopg2.DatabaseError as e:
            return False
        finally:
            cur.close()
            conn.close()
            return True
