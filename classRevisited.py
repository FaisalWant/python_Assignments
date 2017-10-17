class NameOfTheClass():
  classvar="hellouniverse"
  def nameOfTheMethod(self):
     print"HelloWOrld"

class SomeOtherClass():
  def someOtherMethod(self):
     instanceOfClassOne= NameOfTheClass()
     instanceOfClassTwo=NameOfTheClass()

     NameOfTheClass.classVar= "Changed value of class variable"   #modifying the value of the NameOfTheClass variable

     instanceOfClassOne.classVar="Created a New Instance of class var with new instance value"

  def printFunction():
      print(instanceOfClassOne.classVar)

instanceOfClass=SomeOtherClass()

instanceOfClass.printFunction()
