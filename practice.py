# code for displayin only the single occurance of an element

word_list= ['dog','cat','rabbit']


list =[]

for word in word_list:
  for each in word:
      if each in list:
          print ()
      else:
        list.append(each)


print (list)

#using list comprehension this can be done as
def square(n):

    return n**2

#defining the square root using newtons formula
def square_root(n):
    root= n/2 #initial guess will be 1/2
    for k in range(20):
     root=(1/2) *(root+(n/root))

    return root

x=square(3)
print (x)

y=square_root(27)

print(y)
