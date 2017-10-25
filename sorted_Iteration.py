#sorted iteration

basket=[ 'pear','banana','orange','pear','apple']
for fruit in sorted(basket):
     print(fruit)


print(sorted(basket))


x= ["hello","MY","NamE","Is","FaIsAL"]
y=[i.upper() for i in x if len(i)==4]
print("power of list comprehension",y)
