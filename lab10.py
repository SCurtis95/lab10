import sqlite3
import base64
import webbrowser
import curt0061Library as lib 

place = ''

#while (place != 'q'):
con = sqlite3.connect('week10.db')
cur = con.cursor()
cur.execute('SELECT id,Link FROM Lab10 ')
data = cur.fetchall()

db = {}

for key,code in data:
  db[key]= [code]


place = input("Please choose a number between 1-24 or press q to quit: ")
local = int(place)
for key,code in db.items():
  if local == key:
    utfCode = str(code)[2:-2]
    lib.openWeb(utfCode)
    city = input("What is the city name? ")
    country = input("What is the country's name? ")


    


    

    
    
    #utfCode = ''.join([db.get(t, "") for t in place])
    #print(utfCode)
   
   
