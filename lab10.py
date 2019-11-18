import sqlite3
import base64
import webbrowser
import curt0061Library as lib 

place = ''

while (place != 'q'):
  con = sqlite3.connect('week10.db')
  cur = con.cursor()
  cur.execute('SELECT id,Link FROM Lab10 ')
  data = cur.fetchall()
  db = {}

  for key,code in data:
    db[key]= [code]

  
  place = input("Please choose a number between 1-24 or press q to quit: ")
  if place == 'q':
    break
  elif int(place) == key:
    for key,code in db.items():
      utfCode = str(code)[2:-2]
      lib.openWeb(utfCode)
      id = str(key)
      city = input("What is the city name? ")
      country = input("What is the country's name? ")
      cur.execute("""UPDATE Lab10 SET City = ? , Country = ? WHERE id = ?""", (city,country,key))
      con.commit()
      con.close()
 
    
    


    
   
    






    

    
    
    #utfCode = ''.join([db.get(t, "") for t in place])
    #print(utfCode)
   
   
