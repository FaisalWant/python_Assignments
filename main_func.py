
for color in enumerate(['red','green','blue']):
  print(color)



v=([1,2,3],['a','b','c'])
print (v[0].append(4))
print(v)
x=[1,2,3,4]
x.append(5)
x.append([6,7,8,9])
x.extend([6,7,8,9])
print(x)
empty_set=set()

set_output= set([1,2,3,4,5])
print(set_output)
questions= ['name','quest','favourite color']
answer= ['faisal','learning python','blue']
for q, a in zip(questions, answer):
  print('what is your{0} ? {1}'.format(q,a))
