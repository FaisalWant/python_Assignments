#combination function in python
def RecSubsets(soFar, rest):
<<<<<<< HEAD
 print(soFar)
 if rest ==" " :
   print(soFar)
=======
 if rest==" ":
  print(soFar)
>>>>>>> 498ae796299a0d2e1dee0b2ed0e1afd01451e9da

 else:
    RecSubsets(soFar+rest[0],rest[1:])
    RecSubsets(soFar, rest[1:])

x =input()
<<<<<<< HEAD
RecSubsets(" ", x)
=======
RecSubsets("", x)
>>>>>>> 498ae796299a0d2e1dee0b2ed0e1afd01451e9da
