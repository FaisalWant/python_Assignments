#code for counting the number of combinations



def permute(soFar, rest):
  if rest==" ":
      print (soFar)

  else:
      permute(soFar+rest[0],rest[1])
      permute(soFar, rest[1])



x= input()
permute("",x)
