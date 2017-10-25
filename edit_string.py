


# edit string in python

def edit_distance(s1, s2):
  """if len(s1) > len(s2):
      s1, s2 = s2, s1

  distances = range(len(s1) + 1)
  for i2, c2 in enumerate(s2):
      distances_ = [i2+1]
      for i1, c1 in enumerate(s1):
          if c1 == c2:
              distances_.append(distances[i1])
          else:
              distances_.append(1 + min((distances[i1], distances[i1 + 1], distances_[-1])))
      distances = distances_
  return distances[-1]
"""
  len_rw=len(s1)+1
  len_col=len(s2)+1
  x=[[ 0 for d in range(len(s1)+1)] for t in range(len(s2)+1) ]
  #print(x)
  for i in range (len(s1)+1):
    x[0][i]=i

  for j in range(len(s2)+1):
    x[j][0]=j
  for d in range(len_col):
    for e in range(len_rw):
        print(x[d][e])
        if  x[e-1]==x[d-1]:
            x[d][e] = x[d-1][e-1]

        else:
            x[d][e]=min(x[d-1][e]+1,x[d][e-1]+1,x[d-1][e-1]+1)

  print(x)






x= input("enter string one")
y= input ("enter string two")
z=edit_distance(x,y)
print(z)
#i= len(x)
#j=len(y)
