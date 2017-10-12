#combination function in python
def RecSubsets(soFar, rest):
if rest==" ":
  print(soFar)

else:
    RecSubsets(soFar+rest[0],rest[1:])
    RecSubsets(soFar, rest[1:])

x =input()
RecSubsets("", x)
