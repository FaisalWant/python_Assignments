#implementing switch in python
class SimpleProgrm:
  def funtionThree(self):
    self.outIfStatementExamples()
    self.ourListExamples()
    print self.__stringSwitch("TwoIn")
    print self.__integerSwitch(3)


  def __stringSwitch(self, argument):
    return {
      "OneIn": "OneOut",
      "TwoIn": "TwoOut",
      "ThreeIn":"Threeout",
      "FourIn":"FourOut",
      }[argument]

  def ourIfStatementExamples(self):
    x=3
    y=23
    if x>y:
      print "X is larger that Y"
    elif x==y:
       print "X equals to Y"

    elif x<y:
     print "x is smaller than Y"

    else
     print "None of the above are true"


  def ourListExamples(self):
      for x in range(0,5):
        print x
        array= ["one","two", "three"]
        for value in array:
          print value

        for letter in "anyword":
         print letter

   def __integerSwitch(self, argument):
         return {
         1:"one",
         2:"Two",
         3:"Three",
         4:"Four",
                }[argument]

    run =SimpleProgram()

    run.functionThree()
