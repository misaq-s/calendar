import threading 
import datetime
import time as t
  
def Allarm():  
  with open("allarms.txt",'r') as f:
   
    lines=f.readlines()
   
    while True:
      try:
        now = datetime.datetime.now()
        year = '{:02d}'.format(now.year)
        month = '{:02d}'.format(now.month)
        day = '{:02d}'.format(now.day)
        hour = '{:02d}'.format(now.hour)
        minute = '{:02d}'.format(now.minute)
        time = '{}-{}\n'.format(hour, minute)
      
        if time in lines:
          print("\nAllaaaaaaaaaaaaarrrrrrrrrrrmmmmmmmmmmmm")
          t.sleep(60)
        
      except  KeyboardInterrupt:
       
        break
        
def addAllarm():
  with open("allarms.txt",'r+w') as f:
    lines=f.readlines()
    hour=input("enter hour:")
    minute=input("enter minute:")
    time = '{}-{}\n'.format(hour, minute)
    f.write(time)
     
txt=""" for set new allarm enter 1
for see list of allarms enter 2
"""
if __name__ == '__main__':
    t1 = threading.Thread(target=Allarm)  
    t1.start()
    while True:
      
      try:
        print(txt)
        num=input("enter number:")
        if num==1:
          addAllarm()
        elif num==2:
          with open("allarms.txt",'r') as f:
            allarms=f.readlines()
            print(allarms)
          
      except KeyboardInterrupt:

        break
        
