#Stopwatch/ Timer/number guess App basis
import time
import random
from datetime import date
from datetime import datetime
stopper=1

def timer(Sec,Min,Hour):
    while stopper!=0:
        Timer=Sec + ( Min * 60 ) + ( Hour * 120 )
        time.sleep(1)
        if Sec<=0 and Min==0 and Hour==0 :
            return "Time's up"
        elif Sec<=0 and Min>0:
            Sec+=60
            Min-=1
        elif Min==0 and Hour>0:
            Hour-=1
            Min+=60
        print( Sec,"Seconds", Min,"Minutes",Hour,"Hours","\r",end="")
        Sec-=1

def stopwatch():
    stopper=0
    sec=0
    min=0
    hour=0
    day=0
    today=date.today()
    print(datetime.now())
    while stopper!=1:
        time.sleep(1)
        sec+=1
        if sec>=60:
            sec=0
            min+=1
        elif min>=60:
            hour+=1
            min=0
        elif hour>=24:
            day+=1
        print("Today's date", today, "\r",end="")
        print( sec,"Seconds", min,"Minutes",hour,"Hours",day,"Days","\r",end="")

stopwatch()
