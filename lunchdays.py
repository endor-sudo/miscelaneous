import datetime
import time
import threading
from twilio.rest import Client

"""improve the str-int flow"""

#function for sending message thread with trigger
def send_message():
    weekDay={0:'Segunda-feira',1:'Terça-feira',2:'Quarta-feira',3:'Quinta-feira',4:'Sexta-feira'}
    while True:
        today=datetime.datetime.now()
        print(today.hour, today.minute, today.month, month)
        if today.hour==20 and today.minute==18 and today.month==int(month):
            if today.day+1 in lunchDays_list_int:
                #send message 
                """
                accountSID="ACa2f8c346d9e569497ccc5aa332132aaa"
                authToken="b6ef51b7d2417aa17c4455f2c0f5441d"
                dest=Client(accountSID, authToken)
                myTwilioNumber='+12034635590'
                myCellPhone='+351910304364'
                sms=f"Amanhã {today.day+1} do {today.month} o filhote almoça lá!"
                dest.messages.create(body=sms,from_=myTwilioNumber,to=myCellPhone)
                """
                print(f"Amanhã, {weekDay[today.weekday()]}dia {today.day+1} do {today.month} o filhote almoça lá!")
            time.sleep(86400)
            continue
        time.sleep(1)

startTime=datetime.datetime.now()

print(f"program started running: {startTime.hour}:{startTime.minute},"
    f" {startTime.day}/{startTime.month}/{startTime.year} ")

print("'update' to insert new dates")

while True:
    respo=input()
    if respo=='update':
        month=input("what's the month?")

        lunchDays=input("which days of the month do you have lunch at school?"
        "dd,dd,dd,...")

        lunchDays_list=lunchDays.split(',')

        lunchDays_list_int=[]

        for day in lunchDays_list:
            lunchDays_list_int.append(int(day))

        print("Is this right?:")
        for day in lunchDays_list_int:
            print(day)
        print("type 'y' to run program or 'n' to insert new dates:")
        respo=input()
        if respo=='y':
            notify=threading.Thread(target=send_message)
            notify.start()
            print(f"program started running: {startTime.hour}:{startTime.minute},"
                f" {startTime.day}/{startTime.month}/{startTime.year} ")
    else:
        print('Theese are the current dates:')
        for day in lunchDays_list_int:
            print(day)
        print("'update' to insert new dates")