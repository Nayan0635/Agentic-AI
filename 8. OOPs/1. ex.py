class Calc:
    '''DOCSTRING
       we can use as Multiline string
    '''
    #Datamember creates automatically like TypeScript.
    #Python Short hand data member declaration.
    def sayHello(self)->str:
        self.__x=200    #_Calc__x mangled name1
        self.__y=300    #_Calc_y  manglaed name2
        return f'Hello world {(self.__x + self.__y)}'  

#MainScript -> from where Python starts to execute the program.
#We need to create an Object of the class.
obj = Calc()
print(obj.sayHello()) #-->Hello world
#FAQ: what is self keyword ?
#self is an object which holds the current properties of the class.
#It can be compared as this keyword in other programming Language.
#How to access docString
print('docString:',obj.__doc__)

#FAQ: Where is Access Specifier ?
#In generally Python doesnot promote access specifier or access modifier concept
#By default everything is public.
obj.__x=200
obj.__y=500
# print(obj.__x)#200

#Mangaling Effects :
#Instead of providing access specifier python encourage mangaling effects by which it can protect or hide the data by just change in the object name.
#_x -> protected
#__x-> private
#x ->public

#Accessing elements by mangled name
#Naming Convention : _ClassName__y private ,
#Protected Datamembers are not under mangaling effects, python only renames private or __variable into a new name
#This naming convention _x=>protected __X=>private x=>public ->is known as Mangaling Effects.
print(obj._Calc__x+obj._Calc__y)
print("")