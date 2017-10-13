""" As in the solution of this problem
quotient represents no of commas and remainder represents no of digits in the
left side"""



y=input()
x=len(y)
N_of_dig_lef=x%3
N_of_commas=x//3
def stringComma(sofar, rest):
    if rest==" ":
     print(sofar)
     break
    if len(sofar)%3==1:
        sofar+=","+rest[0]
        stringComma(sofar,rest[1])
    else:
        stringComma(sofar+rest[0],rest[1])


stringComma(" ", y)
