'''
FAQ: State the difference between method overloading vs method overriding

     Method overloading:
                    if a same named method with different no of parameters
     and different datatype of parameters declared in the same
     class which create change in output is called method overloading.
    
     Method overloading is a part of compile time polymorphism
     as Python is an interpreted language which doesnot have compiler so it
     doesnot support method overloading.

     Even if we write the code in a manner of occuring method overloading 
     only last defined method gets executed by relacing older methods because of interpreter replaced them.
'''
class Test:
    def addNumbers(self,x:int,y:int)->int:
        return x+y
    def addNumbers(self,x:int,y:int,z:int)->int:
        return x+y+z
    def addNumbers(self,x:float,y:float)->float:
        return x+y
   
obj = Test()
print(obj.addNumbers(12,23,34))

'''
     if same named , same parametered method declared in the super class as well as in sub class,
     then sub class oriented method got the execution and super class oriented
     method automatically suppressed this happends during inheritance at runtime
     so it is known as "Runtime Polymorphism or Method Overriding".
'''
class A:
    def show(self):
        self.x=100
        print("A")
class B(A):
    def show(self):
        self.x=200#Overshadowing -> happening on variable
        print("B")
objB = B()
objB.show()
print(objB.x)

#Accessing overridden method by creating specific object of the class is called Ambiguity resolution.
objA = A()
objA.show()


'''Advanced defination of method overriding
   between common and duplicate data member python always used to cancel the inheritance,
   as a result each individual class stays with their own property which in another way
   expressed as sub class method overrides super class method actually it is a mutual cancellation
   between them.
'''