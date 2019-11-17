#!/usr/bin/env python
import urllib.request


if __name__ == "__main__":
    contents = urllib.request.urlopen("https://ru.wowhead.com/world-quests/bfa/eu").read().decode('utf-8')
    id = "56017"
    if id in contents:
        urllib.request.urlopen("https://api.telegram.org/bot343228570:AAHWvNfSyL-O5QgnkQXWK7DDTWL70_XHTcw/sendMessage?chat_id=129934507&text=https://ru.wowhead.com/quest=%s" % id)