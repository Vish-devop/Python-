1. OOPS is a programming paradigm where we use "CLasses", "Objects", "Methods", "Reference Variables".

1.a> So, what do you mean by the terms: Classes, Object, Methods, Reference Variables. 
-> Class is a [Blueprint/Plan/model/design] for "Objects".
    Syntax of a class is: class name_of_class
    {and for each class, there are (2) things that's present: 
        1. Properties (variables)
        2. Methods (actions) those properties can take. -> and, [functions defined inside a class are called "Methods"]}

-> Objects: 
    1. These are realtime entities. 
    2. This is a physical existence of a class. 
    3. Every object has properties and behavoir. 
        3.a) Properties (data) are specified by variables. 
        3.b) Behavior can be specified by Methods (functions defined inside the class)

    ** There are (3) Types of variables present: 
    1) Instance Variable (Object level variables)
    2) Static Variable (Class Level Variables)
    3) Local Variable (Method Level Variables)

-> Methods: 
    1. In a very simple lamen term: Methods are the functions defined inside the class.
    2. These are of (3) types: 
        2.a) Instance Methods
        2.b) Class Methods
        2.c) Static Methods

-> Reference Variables: 
    1. These are used to "refer objects". 
    2. By using this, we can invoke "functionality of objects".
    3. For a (single object), we can create (multiple reference variables)
    4. Could we can define "objects" without using "Reference variables" ? ? 
        -> Yes, ofcourse. 
    5. Syntax of defining the Reference Variables: 
        reference_variable=Class name() 
        e.g. -> s=Student()
        #Here, s -> reference variable || Student() -> Class name. 

-> Let's take an example of all the above things: Class, method, object, reference variable {{ Example: Basic_example_of_class.py -> go and check the exmaple there.}}

(2) Self keyword:
    -> 'self' is a reference variable, which is always pointing to current object. 
        Within the python class, to access current object, we can use 'self'.
    
    -> The first argument to constructor is always 'self'.
        THe first argument to instane method is always 'self'.
        We're not required to provide value for (self) variable, PVM (python virtual machine) itself provide value. 

    -> We can use (self) always within the class only. 
        Inside (constructor) we can use (self) to declare object related variables (instance variables)
        Inside (Instance method), we can use (self) to access the values of instance variables. 

    -> "self" is (not) a keyword, we can write any name like: delf, kelf, helf, etc.. becuase 
        (1st positional argument in python will always be 'self' only.)
    
    -> To understand better about self: checkout -> self.py file in folder. 

