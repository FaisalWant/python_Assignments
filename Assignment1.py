n= int(6)

if(n%2 != 0):
   print ("Weird")
else:
    if n in range(2,6):
        print("Not Weird")
    if n in range(6,21):
         print ("Weird")
    if n>20 and n%2==0 :
        print("Not Weird")
