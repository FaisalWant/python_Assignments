items=[1,2,3,4,5,6]

def sqr(x) :return x **2

c=list(map(sqr,items))

print (c)


#passing lambda Function

d= list (map(lambda x: x **2,items))
print(d)
