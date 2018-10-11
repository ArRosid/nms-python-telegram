#!/usr/bin/python2
import telepot
import pyping


def ping_server(ip):
    response = pyping.ping(ip)
    if response.ret_code == 0:
        send_telegram('Server {} up!'.format(ip))
    else:
        send_telegram('Server {} down!'.format(ip))


def send_telegram(pesan):
    telegram_token = 'your_telegram_token'
    chat_id = 'your_chat_id'
    bot = telepot.Bot(telegram_token)
    bot.sendMessage(chat_id, pesan)


if __name__ == '__main__':
    ping_server('your_server')
