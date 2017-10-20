

  string ="11 12 2000"
  ind_dy=0
  ind_mn=1
  ind_yr =2
  curr_date_form=string.split()
  curr_date_form[0] = #represents the month
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
