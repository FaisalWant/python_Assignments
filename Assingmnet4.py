x= int(input())

if((x%4==0) and ((x%100)!=0) and (x%400==0)):
  print ("it is a leap year")

else:
     print("sorry not a leap year")
