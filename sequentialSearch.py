def sequential_search(a_list, item):
  pos=0
  found= False
  while pos<len(a_list)and not found:
     if a_list[pos]==item:
        found=True
     else:
      pos=pos+1

  return found
test_list=[1,3,2,4,5,6,7,8,9,10,11]
print (sequential_search(test_list,3))
print(True)
