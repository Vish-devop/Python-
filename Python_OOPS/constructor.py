'''
Let's discuss about the Constructors in Python:- 

> It's a (special) method, where name of the constructor will always be __init__().
> We're (not) required to call constructor [explicitly]. It will be (executed automatically) when we're (creating an object).

'''
# > (per object) constructor will be executed only (once). e.g. is below-> 
class Test: 
    def __init__(self): 
        print("constructor execution.....")

t1=Test()
t2=Test() 
print(id(t1))
print(id(t2))
print("------------------------------------------------------------------------------")
# So, I've also tried you to show the addresses of the both the objects, as mentioned per object constructor will be executed only once, means in this (2) objects are defined, so (2) times constructor would be called. 

'''
> Main purpose of constructor is to (declare) and (initialize instance variables) {{ __init__() means initilization }}
> constructor should take atleast (1) positional argunment -> that is (self) 
'''

# > within the python class constructur is (optional), If we're not providing constructor (default) constructor will be (provided) by PVM; (let's see the example: )
class Student: 
    def m1(self): 
        print("Method execution......")

t=Student()
t.m1()
print("===========================================================================================")
# So, will the code blocks (25-29) would run? -> 
# Yes, because (default constructor) will be executed which is provided by PVM.

'''
> We can call constructor (explicitly) then it would be executed just like a normal method & new object won't be created.
'''
class Test: 
    def __init__(self): 
        print("Constructor execution...")

t=Test()
t.__init__()
print("----------------------------------------------------------------------------------------------")
# So, if you see the line no(44) you can easily understand that the constructor can also be called explicitly. 

'''
> One very important thing, need to keep in mind that: Python do not support (method overloading), but yeah - you can achieve (operator overloading)
    And, let's say if you still trying to declare multiple constructors PVM, will always consider only the last constructor... as python follows (Top-Bottom) approach -> where Bottom is always the priority. 
'''
class Test: 
    def __init__(self): 
        print("no-argument constructor.....")

    def __init__(self, x): 
        print("one - argument constructor......")
    
# t=Test() 
        
# So, if you try to run line no- 59: you can get the error that, (TypeError: Test.__init__() missing 1 required positional argument: 'x') 
# To avoid that, we need to define (1) positional argument, because we've declared that in 2nd constructor, and as mentioned python follows the recent delcared things. 
t=Test(10) 
print("===============================================================================================")

