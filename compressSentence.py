

x= "the one bumble bee one bumble the bee"
y=x.split()
new_dict=dict()
list = [element.upper() for element in y]

for i in range(len(list)):
    if list[i] in new_dict.keys():
        print()
    else:
        new_dict[list[i]]=i

print (new_dict)

he=" "

for j in range(len(y)):
    he+=str(new_dict.get(list[j]))

print(he)
