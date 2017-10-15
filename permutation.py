#code for counting the number of combinations



def permute(soFar, rest):
  if rest==" ":
      print (soFar)

  else:
      for i in range(len(rest))
       next =soFar+rest[i]
       remaining=rest[0:i+1] +rest[i+1]
       permute(next, remaining)



x= input()
permute("",x)
