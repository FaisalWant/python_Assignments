#cloning

def removeDups(L1,L2):
  for e1 in L1:
     if e1 in L2:
        L1.remove(e1)
L1 =[1,2,3,4,7,23,64]
L2= [1,2,5,6,7,23,64]
removeDups(L1, L2)

print ('L1=' , L1)
