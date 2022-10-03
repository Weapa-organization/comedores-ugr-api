import telebot
import datetime
import requests
import logging as log
import signal
import time
import sys
import os

bot = telebot.TeleBot(os.environ.get('BOT_TOKEN'), parse_mode=None)
url = "http://localhost:8000/api/v1/menus/date/"

class FoodStructure:
    name: str
    allergens: list
    type: str

    def __init__(self, name, allergens, type):
        self.name = name
        self.allergens = allergens
        self.type = type

    def __str__(self):
        return f"name : {self.name}, allergens : {self.allergens}"

    def render_json(self):
        return {
            "nombre": self.name,
            "alergenos": self.allergens
        }

class MenuModel:
    starter: FoodStructure
    main: FoodStructure
    second: FoodStructure
    extra: FoodStructure
    dessert: FoodStructure
    date: str

    def __init__(self, starter, main, second, extra, dessert, date):
        self.starter = starter
        self.main = main
        self.second = second
        self.extra = extra
        self.dessert = dessert
        self.date = date

@bot.message_handler(commands=['start', 'help'])
def welcome_message(message):
    msg = "Este bot publica el menu de comedores de la Universidad de Granada"
    msg = msg + "\n\n"
    msg = msg + "Para ver el menu de hoy, escribe /hoy"
    msg = msg + "\n\n"
    msg = msg + "Para ver el de otro dia de la semana, escribe /martes o el dia que quieras"

    bot.send_message(message.chat.id, msg)

@bot.message_handler(commands=['hoy'])
def send_menu(message):
    bot.send_message(message.chat.id, get_menu('hoy'))

def get_menu(day):
    # Obtain date format as 'YYYY-MM-DD'
    date = ""
    if day == 'hoy':
        date = datetime.datetime.now().strftime('%Y-%m-%d')
    elif day == 'mañana':
        date = (datetime.datetime.now() + datetime.timedelta(days=1)).strftime('%Y-%m-%d')

    # Obtain menu from API

    r = requests.get(url + date)

    if r.status_code == 200:
        menu = r.json()[0]
        msg = f"Menu del {menu['date']}"
        msg = msg + "\n"
        msg = msg + f"Entrante: {menu['entrante']['nombre']}"
        msg = msg + "\n"
        msg = msg + f"Principal: {menu['principal']['nombre']}"
        msg = msg + "\n"
        msg = msg + f"Postre: {menu['postre']['nombre']}"

        return msg

    return r.status_code

def main():
    log.basicConfig(level=log.INFO,
                    format='%(asctime)s %(levelname)s %(message)s')

    signal.signal(signal.SIGINT, signal_handler)

    while True:
        try:
            log.info('Starting bot polling...')
            bot.polling()
        except Exception as err:
            log.error("Bot polling error: {0}".format(err.args))
            bot.stop_polling()
            time.sleep(30)


def signal_handler(signal_number, frame):
    print('Received signal ' + str(signal_number)
          + '. Trying to end tasks and exit...')
    bot.stop_polling()
    sys.exit(0)

if __name__ == "__main__":
    main()