from datetime import datetime,date, timedelta

dt_now = datetime.now()
delta1 = timedelta(days=1)
delta2 = timedelta(days=30)
print(dt_now - delta1)
print(dt_now)
print(dt_now - delta2)
date_string = '01/01/17 12:10:03.234567'
date_dt = datetime.strptime(date_string, '%m/%d/%y %H:%M:%S.%f')
print(date_dt)