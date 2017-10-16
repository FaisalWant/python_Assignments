""" square root of the function using the bisection search method"""


x=1/2
epsilon, numGuesses,low = 0.01,0,0.0
high= max(1.0, x)

ans =(high+low)/2.0

while abs(ans**2-x) >=epsilon:
     print ('low=', low, 'high=', high,'ans=', ans)

     numGuesses+=1
     if ans**2 < x:
       low =ans
     else:
       high=ans

     ans=(high+low)/2.0

print('numGuesses=',numGuesses)
print (ans, 'is close to square root of',x)
