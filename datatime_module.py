import datetime
import pytz

#print(datetime.date())
print(datetime.datetime.now())
print(datetime.datetime.now().year)
print(datetime.datetime.now().month)
print(datetime.datetime.now().day)
print(datetime.datetime.now().hour)
print(datetime.datetime.now().minute)
print(datetime.datetime.now().second)
print(datetime.datetime.today())
print(datetime.datetime.today().year)
print(datetime.datetime.today().strftime("%d-%M-%y"))
print(datetime.datetime.today().strftime("%d-%M-%Y"))
print(datetime.datetime.today().strftime("%D"))
print(datetime.datetime.today().strftime("%c"))
print(datetime.datetime.today().tzname)
#print(datetime.datetime.date())
#print(datetime.datetime.ctime())
#print(datetime.datetime.time())


req_time=pytz.timezone('Asia/Kolkata')
print(datetime.datetime.now(req_time))