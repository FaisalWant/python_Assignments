

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
  def_date="d/m/y"
  x= z.upper()
  y= re.split(':|,|-|/', x)
  b= re.split(':|,|-|/',def_date)

  dy =b.index("d")
  print(dy)
  mn= b.index("m")
  print(mn)
  yr=b.index("y")
  print(yr)
#print(myDate)



  print(y)
  val= True    # if the input is in integer format
  for s in y:
    if not s.isdigit():
      val=False    #

  if val:
      for i in range(len(y)):
        if y[i].isdigit():

           if len(y[i])==2:

                if int(y[dy]) in range(1,31):
                  date= y[dy]
                  print("date",date)

                if int(y[mn]) in range(1,12):
                    month= y[mn]
                    print("month",month)

           elif len(y[yr])==4:

                if int(y[yr]) in range(1900,3000):
                    print(y[yr])
                    year=y[yr]
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
  return(time.strftime("%Y/%m/%d",conv))




z=input()

print(stringFormat(z))
