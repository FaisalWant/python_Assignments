def generate_fibs():
      a, b= 0,1
      while True:
          a,b= b,a+b
          yield a
z=generate_fibs()
print(next(z))
print(next(z))
print(next(z))
print(next(z))
print(next(z))

print(max(next(z)))
