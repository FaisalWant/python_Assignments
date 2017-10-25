# list comprehension

y= ["hello" ,"my" ,"name","is", "Faisal"]
x=[i.upper() for i in  y if len(i)==4]
z=[(i) for i in y if len(i)>2]
print(x)
print(z)
d=[(x,x**2,x**3) for x in range(1, 10)]
print(d)
f= [(x+1) for x in range(1,10)]

print(f)
t=[(i,j) for i in range(5) for j in range(i)]
print(t)

s= [i for i in range(100) if i%2!=0 ]
print(s)
