def stringChange(x,stri):
 import re
 import time
 import datetime

 Month = {'JAN': "JANUARY",'FEB' :"FEBRUARY", 'MAR':"MARCH",
        'APR':"APRIL", 'MAY':"MAY", 'JUN' :"JUNE" ,
         'JUL' :"JULY" , 'AUG' :"AUGUST", 'SEP' :"SEPTEMBER",
         'OCT' :"OCTOBER", 'NOV':"NOVEMBER" , 'DEC':"DECEMBER" }

 now = datetime.datetime.now()
 baseYear=2000
 if x=="":
  x="d/m/y"  #default behaviour
 z=stri.upper()
 myDate =re.split(':|,|-|/', z)
 y= re.split(':|,|-|/', x)

 dy =y.index("d")
 print(dy)
 mn= y.index("m")
 print(mn)
 yr=y.index("y")
 print(yr)
 print(myDate)


 #myDate = filter(None,myDate)
 print (now.year)   # now.year returns the integer value
 #checks the empty condition
 print (myDate[yr])
 if myDate[yr] == "":
   myDate[yr]=str(now.year)
   print (now.year)

 if len(myDate[yr])==2:
    myDate[yr]=str(int(myDate[yr])+int(baseYear))
    print("added the base year",myDate[yr])

 if int(myDate[dy]) in range(1,32):
   dat=myDate[dy]
   print ("valid Date",dat)

 if (int(myDate[yr]) in range(1900,3000)) :
   yer=myDate[yr]
   print("valid year",yer)



 if myDate[mn].isdigit():
    if int(myDate[mn]) in range(1,13):
      mon=myDate[mn]
      val=False
      print("valid month",mon)
 elif myDate[mn] in Month:
      mon=Month[myDate[mn]]

      val=True
      print("valid month",mon)

 print (type(mon))
 print(type(yer))
 print(type(dat))
 from_date= mon+" "+dat+" "+yer

 print(from_date)
 print(val)
 if not val:
  conv=time.strptime(from_date,"%m %d %Y")
  print(time.strftime("%Y/%m/%d",conv))
 if val:
  conv=time.strptime(from_date,"%B %d %Y")
  print(time.strftime("%Y/%m/%d",conv))


x=input("Enter the Format")
stri=input("Enter the string")


stringChange(x,stri)
