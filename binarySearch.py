

#code for binary search in python

def binarySearch(a_list,num):

 if len(a_list)==0:
     print(False)
     return False

 else:

   pos=end//2
   if a_list[pos]==num:
      print(True)
      return True
   else:
       if a_list[pos]>num:
         binarySearch(a_list[:pos],num)
       else:
        binarySearch(a_list[pos+1:],num)


def Search(a_list, num):

  return binarySearch(a_list,num)

a_list=[1,2,3,4,5,6,7,8,9]
x=Search(a_list, 0)
print (x)
