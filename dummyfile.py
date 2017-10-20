

#validating for the default-case
def validate(date_text):
    try:
        if date_text != datetime.strptime(date_text, "%m %d %Y").strftime('%m %d %Y'):
            raise ValueError
        return True
    except ValueError:
        return False
def Month_to_index(Month_Name):
 return{
      'JANUARY' : 1, 'FEBRUARY' : 2,'MARCH' : 3,
      'APRIL' : 4,'MAY' : 5, 'JUNE' : 6,
      'JULY' : 7, 'AUGUST' : 8,'SEPT' : 9,
      'OCTOBER': 10,'NOVEMBER' : 11, 'DECEMBER': 12
}[Month_Name]
def output_string(string,ind_dy,ind_mn,ind_yr):
   import collections
   curr_date_form=string.split()
   curr_date_form[0]  #represents the month
   curr_date_form[1]  #represents the date
   curr_date_form[2]  #represents the year

 #collections representing the date at hand

   date=  collections.namedtuple('Date','index value')
   dt=date(index=ind_dy,value=curr_date_form[1])
   month=  collections.namedtuple('Month','index value')
   mh=date(index=ind_mn,value=curr_date_form[0])
   year=  collections.namedtuple('Year','index value')
   yr=date(index=ind_yr,value=curr_date_form[2])

   print (dt)
   print(mh)
   print(yr)
   stringnew=""
   a=dt.index
   b=mh.index
   c=yr.index
   if a< b and a < c:
       if (b <= c):
           print("a, b, c")
           print(dt.value+"/"+mh.value+"/"+yr.value)
       else:
           print( "a, c, b")
           print(dt.value+"/"+yr.value+"/"+mh.value)

   elif  b < a and b < c:
        if a < c:
           print("b, a, c")
           print(mh.value+"/"+dt.value+"/"+yr.value)
        else:
           print("b, c, a")
           print(mh.value+"/"+yr.value+"/"+dt.value)

   else:
      if a < b:
           print("c, a, b")
           print(yr.value+"/"+dt.value+"/"+mh.value)
      else:
           print("c, b, a")
           print(yr.value+"/"+mh.value+"/"+dt.value)

def stringFormat(z,op_format):
  import datetime
  import time
  import re


  Month = {'JAN': "JANUARY",'FEB' :"FEBRUARY", 'MAR':"MARCH",
          'APR':"APRIL", 'MAY':"MAY", 'JUN' :"JUNE" ,
           'JUL' :"JULY" , 'AUG' :"AUGUST", 'SEP' :"SEPTEMBER",
           'OCT' :"OCTOBER", 'NOV':"NOVEMBER" , 'DEC':"DECEMBER" }

  month2= ['JANUARY','FEBRUARY', 'MARCH','APRIL','MAY', 'JUNE','JULY', 'AUGUST','SEPTEMBER','OCTOBER', 'NOVEMBER', 'DECEMBER']
  month=""
  baseYear=2000
  disp=False
  #z= input()
  print(op_format)
  def_date="d/m/y"   #input default format
  x= z.upper()
  y= re.split(':|,|-|/|/s ', x)
  b= re.split(':|,|-|/',def_date)    #default dateformat
  op_fr=re.split(':|,|-|/',op_format)   #output format
  print(op_format)
  if op_format != " " :   #this step is done only if user supplies a new output format
    disp=True
    dy_op=op_fr.index("d")
    print("Output date at",dy_op)
    mn_op=op_fr.index("m")
    print("Output month at",mn_op)
    yr_op=op_fr.index("y")
    print("output year at",yr_op)


  dy =b.index("d")     #storing the value of default format
  print(dy)
  mn= b.index("m")
  print(mn)
  yr=b.index("y")
  print(yr)


  print(y)
  val= True
  for s in y:
    if not s.isdigit():
      val=False    #

  if val:
      for i in range(len(y)):
        if y[i].isdigit():



                if int(y[dy]) in range(1,32):
                  date= y[dy]
                  print("date",date)

                if int(y[mn]) in range(1,13):
                    month= y[mn]
                    print("month",month)

                if int(y[yr]) in range(1900,3000):
                    print(y[yr])
                    year=y[yr]
                    print("year",year)

                if len(y[yr]) ==2:                 #testing if the year field is give in just 2 letters
                    year = str(int(y[yr])+int(baseYear))
                    print("year",year)

      from_date= month+" "+date+" "+year
     #default output
      print(from_date)

      if disp:
        output_string(from_date,dy_op,mn_op,yr_op)
      else:
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


  month=str(Month_to_index(month))
  from_date= month+" "+date+" "+year
  print(from_date)

  if disp:
    output_string(from_date,dy_op,mn_op,yr_op)
  #default output
  else:
   conv=time.strptime(from_date,"%m %d %Y")
   return(time.strftime("%Y/%m/%d",conv))


z=input()
op_format=input("Enteroutputformat as d/m/y or y/m/d ....")
print(op_format)
print(stringFormat(z,op_format))
