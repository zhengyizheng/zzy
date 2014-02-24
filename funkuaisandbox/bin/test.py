import datetime
import time
#from datetime import *  

startstr="2014-02-22"
endstr="2014-03-31"

start_date = datetime.datetime(* time.strptime(startstr, "%Y-%m-%d")[:6])
end_date =  datetime.datetime(* time.strptime(endstr, "%Y-%m-%d")[:6])

for n in range(int ((end_date - start_date).days+1)):
    cur = start_date + datetime.timedelta(n)
    print(cur.strftime('%Y-%m-%d'))
#print(date.today())
