#converting a multiple value list to single instance
my_list=["bayer Asprin", "Asprin", "xelzong", "lyrican","s","s"]
#jIndex= (i-1)%len(l)
set_list= set(my_list)
print("set conversion",set_list)
list=list(set_list)
#list.addAll(set_list);
#for i in range(len(list)-1):
print("list conversion",list)

target_list=[]
source_list=[]
for items in list:
     element=items.split()
     if len(element)>1:
      source_list.append(element)

print ("source_list",source_list)
#for element in source_list:
#    for sublist in element:
#        if sublist in

for items in list:
     element=items.split()
     if len(element)==1:
         target_list.append(items)
print("target_list",target_list)

for element in source_list:
    for vale in element:
      if vale in target_list:
          target_list.remove(vale)
         # print(vale)
          #target_list.remove(vale)


print("Target_list",target_list)
list= source_list+target_list
print(list)
