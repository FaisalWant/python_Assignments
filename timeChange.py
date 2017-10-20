
import re
import time
text = "11/26/2014"
date=" "
month=" "
year=" "
list= re.split(':|,|-|/', text)
print(list)
for i in range(len(list)):
  if list[i].isdigit():

      if len(list[i])==2:

          if int(list[i]) in range(1,31):
            date= list[i]
            print("date",date)

            if int(list[i]) in range(1,12):
              month= list[i]
              print("month",month)

      elif len(list[i])==4:

          if int(list[i]) in range(1900,3000):
              print(list[i])
              year=list[i]
              print("year",year)

from_date= month+" "+date+" "+year
print(from_date)
conv=time.strptime(from_date,"%m %d %Y")
print(time.strftime("%Y/%m/%d",conv))

conv=time.strptime(from_date,"%B %d %Y")
return(time.strftime("%Y/%m/%d",conv))

  #else:
    # list.extend(char)
#print (list)
#print(list)
