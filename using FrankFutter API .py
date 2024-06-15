import sys
import requests

if len(sys.argv)>4:
    print("Too many Arguments")
elif len(sys.argv)<4:
        print("Missing arguments")
else:
    def myOutput(TO,FROM,date):
        response=requests.get(f"https://api.frankfurter.app/{date}?from={FROM}&to={TO}")
        inverse=requests.get(f"https://api.frankfurter.app/{date}?from={TO}&to={FROM}")
        print(f"The conversion rate on {date} from {FROM} to {TO} was {response.json()['rates'][TO]}.The inverse rate was {inverse.json()['rates'][FROM]}.")
        
    LIST=sys.argv
    date=str(LIST[1])
    if date[4]!='-' or date[7]!='-':
        print("Incorrect date formate!")
        exit()
    FROM=str(LIST[2]).upper()
    TO=str(LIST[3]).upper()
    dictionary=requests.get(f"https://api.frankfurter.app/currencies")
    currencies=dictionary.json()
    splitted_date=date.split("-")
    year,month,day=(int(0),int(0),int(0))
    year=int(splitted_date[0])
    month=int(splitted_date[1])
    day=int(splitted_date[2])
    flag=False
    if FROM in currencies and TO in currencies:
        flag=True
    else:
        print("Incorrect Currency!")
        exit()
    if year>=1999 or month <= 12 or day<=31 and flag==True:
        myOutput(TO,FROM,date)
        exit()
    else:
        print("Incorrect date")
        exit()
    