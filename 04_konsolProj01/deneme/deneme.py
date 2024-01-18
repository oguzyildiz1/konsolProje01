import datetime as d
import time as t


print(d.date.today())
print(d.datetime.now())

tarih = d.date.today()
simdi = d.datetime.now()

print(tarih.strftime("%m/%d/%y"))

while True:
    simdi = d.datetime.now()
    print(simdi.strftime("%H:%M:%S"))
    t.sleep(1)



