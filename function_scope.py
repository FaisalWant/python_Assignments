#Function scopes

x=2
def foo(y):
  z=5
  x=7
  print(locals()['x'])
  print(globals()['x'])
  print(x,y,z)

foo(3)
