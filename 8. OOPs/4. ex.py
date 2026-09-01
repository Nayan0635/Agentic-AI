class User:
    '''DOC String
       What is Consttuctor ?
       Constructor is a function which creates object.
       Means in other way we can say Constrtuctor is a birth mother of
       all objects that we are creating.
       we can classified constructor under 2 categories
       1)Default/Zero Args Constructor
         which only creates object & called first when we create object.

       2)Parameterized constructor :
         constructor who can create object as well as send values at the same time.

       Generally , in most of language Constructor are named after class name
       but Python doesnot follow this naming convention.
       Here in Python constructor are created using a magic keyword
       __init__(self)  ->initializer method.    
    '''
    #Defaulr constructor
    def __init__(self):
        print("Default Constructor")
    #user defined custom function.
    def sayHello(self)->str:
        return 'Hello world'
#MainScript
user1 = User()
print(user1.sayHello())