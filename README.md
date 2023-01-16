# Telegram Python Bot
Bot de Telegram en Python alojado en Heroku 

## Pasos de instalacion

Creacion del entorno virtual:
    
    
    $ python3 -m venv telegrambot
Activar el entorno:


    $ source telegrambot/bin/activate

Instalar API telebot y Flask:


    $ pip3 install pyTelegramBotAPI Flask psycopg2-binary
    
## Ejecutar el bot:

    (telegrambot) $ python3 start.py
    
## Elementos utiles para el manejo de la base de datos en Heroku
Para obtener informacion de los campos y columnas de la tabla actual, incluyendo el nombre
completo de como se puede llamar shema.tablename listado en la parte superior de la respuesta..

    \d tablename
    
Para obtener informacion del table_catalog y nombre de la table_shema

    SELECT table_catalog, table_schema FROM information_schema.tables WHERE table_name = 'tablename';
    
