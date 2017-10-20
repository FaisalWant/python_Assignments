def smaller(x,y):
    return x if x<y else y



string ="11 12 2000"
ind_dy=0
ind_mn=1
ind_yr =2
curr_date_form=string.split()
curr_date_form[0]
curr_date_form[1]  #represents the date
curr_date_form[2]  #re
import collections
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











if dt.index < smaller(mh.index,yr.index):
     stringnew=dt.value+"/"
elif mh.index <smaller(dt.index,yr.index):
    stringnew=mh.value+"/"
elif yr.index <smaller(dt.index,mh.index):
    stringnew= yr.value+"/"
