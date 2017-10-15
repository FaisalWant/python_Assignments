<<<<<<< HEAD


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
=======


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
>>>>>>> 498ae796299a0d2e1dee0b2ed0e1afd01451e9da
