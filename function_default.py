
def ask_yn(prompt, retries=4, complaint='Enter Y/N!'):
    for i in range(retries):
      ok =input(prompt)

      if ok== 'Y':
         return True
      if ok=='N':
          return False

      print(complaint)

def parrot( voltage,state='a stiff', action='voon', type='Norweigian blue'):
     print("__ this parrot wouldn\'t",state, action,type, end='')
     print("__ this thing will print the state", state)

#parrot(voltage=1000, state='...', action='...', type='dumbass')
#parrot(voltage=1000,action="kill that")
parrot(1000,"kill me")
#ask_yn("please enter your choice")
