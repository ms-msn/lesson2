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
	if args[0] == 'Venus':
		text = ephem.Venus(date_str)
		print(text)
		text1 = ephem.constellation(text)
		print(text1)
		update.message.reply_text(text1)
	elif args[0] == 'Mercury':
		text = ephem.Venus(date_str)
		print(text)
		text1 = ephem.constellation(text)
		print(text1)
		update.message.reply_text(text1)
	elif args[0] == 'Earth':
		text = ephem.Earth(date_str)
		print(text)
		text1 = ephem.constellation(text)
		print(text1)
		update.message.reply_text(text1)
	elif args[0] == 'Mars':
		text = ephem.Mars(date_str)
		print(text)
		text1 = ephem.constellation(text)
		print(text1)
		update.message.reply_text(text1)
	elif args[0] == 'Jupiter':
		text = ephem.Jupiter(date_str)
		print(text)
		text1 = ephem.constellation(text)
		print(text1)
		update.message.reply_text(text1)
	elif args[0] == 'Saturn':
		text = ephem.Saturn(date_str)
		print(text)
		text1 = ephem.constellation(text)
		print(text1)
		update.message.reply_text(text1)
	elif args[0] == 'Uranus':
		text = ephem.Uranus(date_str)
		print(text)
		text1 = ephem.constellation(text)
		print(text1)
		update.message.reply_text(text1)
	elif args[0] == 'Neptune':
		text = ephem.Neptune(date_str)
		print(text)
		text1 = ephem.constellation(text)
		print(text1)
		update.message.reply_text(text1)	
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