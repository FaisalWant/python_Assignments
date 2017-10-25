#variadic postional arguments

"""def product(*nums, scale=1):
  p= scale
  for n in nums:
    p*=n
  return p

def is_prime(n):


primes= [number for number in range(2,100) if is_prime(number)]

print(product(*primes))

"""
"""def authorize(quote, **speaker_info):
    print(">",quote)
    print("-" *(len(quote)+2))
    for k,v in speaker_info.items():
        print(k,v,sep=':')

speaker_info={ "name":"faisal",
                   "class":"10th",
                   "sec":"A",
                   "roll_no":10}

authorize("love in life",**speaker_info)
"""
"""
x=3
foo= 'fighter'
y=4
bar='bell'
z=5
print("{z}^2={x}^2 +{y}^2". format(**locals()))
"""

languages= ["python","java"]
"""lens=[map(len(s),s) for s in languages]
print(lens)
"""
"""def is_even(a):
    if a%2==0:
     return True
#print(map(len, languages))
print(filter(is_even,range(100)))
"""
"""print((lambda val:val ** 2)(3))
print((lambda x,y: x*y)(3,2))
lambda pair:pair[0]* pair[1]
triple = (lambda x: x * 3)(3)
print(triple)

print(map (lambda val:val**2, range(10)))"""


"""it =iter([1,2,3])
print(next(it))
print(next(it))
print(next(it))
"""
def generate_insts(n):
    for i in range(n):
        yield i

g= generate_insts(4)
print(g)    
