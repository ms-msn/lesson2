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

def word_count(bot, update):
    user_text = update.message.text
    user_text = user_text.replace("/wordcount ", "")
    user_text = user_text.strip()
    print(user_text)
    if user_text[0] == '"' and user_text[-1] == '"' and len(user_text) > 0 :

        user_text = user_text.replace(".","").replace(",", "").replace("?", "")
        splitted_text = user_text.split(" ")
        
        splitted_text = str(len(splitted_text)) + ' слова'
        update.message.reply_text(splitted_text)
    else:
        update.message.reply_text("Неправильный ввод")


def main():
    updater = Updater("540429828:AAEj5WiGOKNyn0i_UcdwbVpdJZ-RSktC-ng")
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(CommandHandler("planet", planet_ep, pass_args=True))
    dp.add_handler(CommandHandler("wordcount", word_count))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))
    updater.start_polling()
    updater.idle()
    
def talk_to_me(bot, update):
    user_text = update.message.text
    word_number = { "ноль" : 0,
                    "один" : 1,
                    "два" : 2 ,
                    "три" : 3 ,
                    "четыре" : 4 ,
                    "пять" : 5 ,
                    "шесть" : 6 ,
                    "семь" : 7 ,
                    "восемь" : 8 ,
                    "девять" : 9 ,
                    "десять" : 10,
                    "на" : "на"
                    }
    omen = {"минус" : "-",
            "умножить" : "*",
            "сложить" : "+",
            "разделить" : "/"
           } 
    print(user_text)
    user_text = user_text.strip()
    print(user_text)
    splitted_text = user_text.split(" ")
    if splitted_text[-1] == "="  :
        
        
        if splitted_text[0].isnumeric  and splitted_text[2].isnumeric:
            number1 = float(splitted_text[0])
            number2 = float(splitted_text[2])
            if splitted_text[1] == "-":
                otvet = number1 - number2
                update.message.reply_text(otvet)
            elif splitted_text[1] == "+":
                otvet = number1 + number2
                update.message.reply_text(otvet)
            elif splitted_text[1] == "*":
                otvet = number1 * number2
                update.message.reply_text(otvet)
            elif splitted_text[1] == "/":
                if number1 != 0:
                    otvet = number1 / number2
                    update.message.reply_text(otvet)
                else:
                    update.message.reply_text("деление на ноль")

        
    if splitted_text[0] == "сколько" and splitted_text[1] == "будет":
        splitted_text = user_text.split(" ")
        print(splitted_text)
        print("proval 2")
        if splitted_text[2] in word_number and splitted_text[4] in word_number and splitted_text[3] in omen:
            print("proval 2")
            number1 = word_number[splitted_text[2]]
            if splitted_text[4] != "на" :

                number2 = word_number[splitted_text[4]]
                if omen[splitted_text[3]] == "-":
                    otvet = number1 - number2
                    update.message.reply_text(otvet)
                elif omen[splitted_text[3]] == "+":
                    otvet = number1 + number2
                    update.message.reply_text(otvet)
            elif splitted_text[4] == "на":
                number2 = word_number[splitted_text[5]]
                if omen[splitted_text[3]] == '*' :
                    otvet = number1 * number2
                    update.message.reply_text(otvet)
                elif omen[splitted_text[3]] == "/":
                    if number1 != 0:
                        otvet = number1 / number2
                        update.message.reply_text(otvet)
                    else:
                        update.message.reply_text("деление на ноль")

        
    else:
        update.message.reply_text(user_text)

main()