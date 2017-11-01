from fuzzywuzzy import fuzz
from fuzzywuzzy import process

import csv

def correct_road(List,roadname,indx):
   #if roadname in List:  # might want to make this a dict for O(1) lookups
    #    return roadname

   new_name, score = process.extractOne(roadname,List[0:indx]+List[indx+1:])
   print("roadname",roadname)
   print("new_name",new_name,score)
   if score <80:
        return roadname
    #,score
   else:
        return new_name
    #,score
#df['corrected'], df['score'] = correct_road("clonazepalm")






#df= dict()
new_list=list()
new_list2=list()
#list2 = ["Bayer Aspirin","asprn","aspirin","xelzange","Bayer Aspirinn","Bayir Aspirin","lyrica","lyreca","Xelzange Maven" ,"Xelzange","aspirin","Pfizer Aspirin" , "Aspirin", "Bayer Aspirin"]
list2=["crocin","crocen","advil"]
#mylist= ['clonezpam','esprin','codeine','cymbalta']
List2= [i.lower() for i in list2]
print("step 1:",List2)
mySet=set(List2)
myList=list(mySet)
print("step: 2 duplicate Eliminated",myList)
# exampleFile = open('drug3.csv')
# exampleReader = csv.reader(exampleFile)
# exampleData = list(exampleReader)
#print(exampleData)

for index, var in enumerate(myList):
    new_list.insert(index,correct_road(myList,var,index))
my_set=set(new_list)
list2=list(my_set)


###############################################
print("list conversion",list2)

target_list=[]
source_list=[]
for items in list2:
     element=items.split()
     if len(element)>1:
      source_list.append(element)

#print ("source_list",source_list)
#for element in source_list:
#    for sublist in element:
#        if sublist in

for items in list2:
     element=items.split()
     if len(element)==1:
         target_list.append(items)
#print("target_list",target_list)

for element in source_list:
    for vale in element:
      if vale in target_list:
          target_list.remove(vale)
         # print(vale)
          #target_list.remove(vale)


#print("Target_list",target_list)
list3= source_list+target_list
#print(list3)
#combining the strings
for index,value in enumerate (list3):
    if isinstance(value,list):
        list3[index]= " ".join(value)
print("step :3 displaying list3 combined",list3)


#  Applying fuzzy again
for ind, varn in enumerate(list3):
    new_list2.insert(ind,correct_road(list3,varn,ind))

flist=set(new_list2)
print("step :4 displaying new_list2",flist)

listx=process.dedupe(flist,threshold=40)
print(list(listx))
