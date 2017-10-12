

x= input()
y=x.split()
new_dict=dict()

for i in range(len(y)):
    if y[i] in new_dict.keys():
        print()
    else:
        new_dict[y[i]]=i

print (new_dict)

he=" "

for j in range(len(y)):
    he+=str(new_dict.get(y[j]))

print(he)
