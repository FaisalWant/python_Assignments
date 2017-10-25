
# data structures in python
class Stack():
 def__init__(self):
  self.__stack=[]
 def isEmpty(self):
   return len(self.__stack)==0

  def push(self, object):
    self.__stack.append(object)

  def pop(self):
    if self.isEmpty():
     return 0
     else:
      objectToReturn=self._stack[len(self.__stack)-1]
      self.__stackpop(len(self.__stack)-1)
      return objectToReturn

    def peek(self):
    return self.__stack[len(self.__stack)-1]

    def search(self, object):
      return self.__stack.index(object)

    def size(self):
      return len(self.__stack)
