
import datetime
import random
import time
st = '2015-11-16 16:47:59.1'
st = str(st)
dateSplit = st.split('.')

registertime = datetime.datetime.strptime(dateSplit[0], "%Y-%m-%d %H:%M:%S")

print(registertime.second )

print( random.randrange(0,4) )


for i in range(0,5):
    print i
    time.sleep(0.7)
