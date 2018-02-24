from datetime import datetime
import ephem
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging

date = datetime.now()
date_str = date.strftime('%Y/%m/%d')
planets = ['Mercury','Venus','Earth','Mars','Jupiter','Saturn','Uranus','Neptune']


logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log'
                    )

def greet_user(bot, update):
    print('Вызван /start')
    print(update)
    text = 'Вызван /start'
    print(text)
    update.message.reply_text(text)

def planet_ep(bot, update, args):
	print('Вызван /planet')
	if args in planets:
		ephem_planet = getattr(ephem, args)
		ephem_planet_date = ephem_planet(date_str)
		print(ephem_planet_date)
		m = ephem_planet_date
		update.message.reply_text(ephem.constellation(m))	
	else:
		text = 'Такой планеты нет'
		update.message.reply_text(text)



def main():
    updater = Updater("540429828:AAEj5WiGOKNyn0i_UcdwbVpdJZ-RSktC-ng")
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(CommandHandler("planet", planet_ep, pass_args=True))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))
    updater.start_polling()
    updater.idle()
    
def talk_to_me(bot, update):
    user_text = update.message.text 
    print(user_text)
    update.message.reply_text(user_text)

main()