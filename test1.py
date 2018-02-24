from datetime import datetime
import ephem
planets = ['Mercury','Venus','Earth','Mars','Jupiter','Saturn','Uranus','Neptune']
chat_data = 'Earth'
date = datetime.now()
date_str = date.strftime('%Y/%m/%d')


def planet(chat_data):
	
	if chat_data in planets:
		ephem_planet = getattr(ephem, chat_data)
		c = ephem.repr(chat_data)(date_str)
		ephem_planet_date = ephem_planet(date_str)
		print(ephem_planet_date)
		m = ephem_planet_date
		print(ephem.constellation(m))
	else:
		print('Takoi planeti net')

'''
def planet(chat_data):
	if chat_data == 'Venus':
		m = ephem.Venus(date_str)
		print(ephem.constellation(m))
	else:
		print('Такой планеты нет')
'''
planet('Venus')
planet('fsfsfs')


ephem_planet = getattr(ephem, 'Mars')
ephem_planet_date = ephem_planet(date_str)

