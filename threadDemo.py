#threading in python


import threading, time
print('start of program')

def takeANap():
  time.sleep(0)
  print('wakeup')

threadObj= threading.Thread(target=takeANap)
threadObj.start()

print('end of program')
