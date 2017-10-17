import re
import time

Month = {'JAN': "JANUARY",'FEB' :"FEBRUARY", 'MAR':"MARCH",
        'APR':"APRIL", 'MAY':"MAY", 'JUN' :"JUNE" ,
         'JUL' :"JULY" , 'AUG' :"AUGUST", 'SEP' :"SEPTEMBER",
         'OCT' :"OCTOBER", 'NOV':"NOVEMBER" , 'DEC':"DECEMBER" }




x=input("Enter the Format")
stri=input("Enter the string")
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
if int(myDate[dy]) in range(1,32):
   dat=myDate[dy]
   print ("valid Date",dat)

if int(myDate[yr]) in range(1900,3000):
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


from_date= mon+" "+dat+" "+yer

print(from_date)
print(val)
if not val:
 conv=time.strptime(from_date,"%m %d %Y")
 print(time.strftime("%Y/%m/%d",conv))
if val:
 conv=time.strptime(from_date,"%B %d %Y")
 print(time.strftime("%Y/%m/%d",conv))
