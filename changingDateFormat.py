

def stringFormat(z):
  import datetime
  import time
  import re


  Month = {'JAN': "JANUARY",'FEB' :"FEBRUARY", 'MAR':"MARCH",
          'APR':"APRIL", 'MAY':"MAY", 'JUN' :"JUNE" ,
           'JUL' :"JULY" , 'AUG' :"AUGUST", 'SEP' :"SEPTEMBER",
           'OCT' :"OCTOBER", 'NOV':"NOVEMBER" , 'DEC':"DECEMBER" }

  month2= ['JANUARY','FEBRUARY', 'MARCH','APRIL','MAY', 'JUNE','JULY', 'AUGUST','SEPTEMBER','OCTOBER', 'NOVEMBER', 'DECEMBER']
  month=""

  #z= input()
  x= z.upper()
  y= re.split(':|,|-|/', x)
  print(y)
  val= True
  for s in y:
    if not s.isdigit():
      val=False

  if val:
      for i in range(len(y)):
        if y[i].isdigit():

            if len(y[i])==2:

                if int(y[i]) in range(1,31):
                  date= y[i]
                  print("date",date)

                  if int(y[i]) in range(1,12):
                    month= y[i]
                    print("month",month)

            elif len(y[i])==4:

                if int(y[i]) in range(1900,3000):
                    print(y[i])
                    year=y[i]
                    print("year",year)

      from_date= month+" "+date+" "+year
      print(from_date)
      conv=time.strptime(from_date,"%m %d %Y")
      return(time.strftime("%Y/%m/%d",conv))



  for k in month2:
      if k in y:
        month=k
        print(month)


  for k in Month:
      if k in y:
        month=Month[k]
        print(Month[k])


  for z in y:
       if z.isdigit():
        if len(z)==4:
              year=z
        elif len(z) in range(1,31) :
             date=z

  from_date= month+" "+date+" "+year
  print(from_date)
  conv=time.strptime(from_date,"%B %d %Y")
  print(time.strftime("%Y/%m/%d",conv))

   #return (x)


z=input()

print(stringFormat(z))
