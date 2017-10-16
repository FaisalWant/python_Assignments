#pallindromes

def ispallindrome(rest):
   if len(rest)<=1:
    return True

   else:
     return rest[0]==rest[-1] and ispallindrome(rest[1:-1])




print(ispallindrome("faisal"))
