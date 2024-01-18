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


(3) Constructors: 
    -> It's a (special) method, where name of constructor is always __init__().
    -> Since, name of the constructor is always __init__(), we can't use the property of (method overloading) in the python. 
    -> We're not required to call constructor (explicitly) and it will be (executed automatically) when we're (creating an object). 
    -> per object constructor will be executed only (once); so for every-time constructor will be executed only once for a single object. 
    -> Main purpose of constrcutor is to (declare) and (initlialize instance variables): __init__() means initialization. 
    -> Constructors should take atleast (1) positional argument. 
    -> Within the python class, constructor is (optional) and if we're not providing constructor: by-default constructor will be provided by PVM. 
    -> We can call constructor explicitly then, it would be executed just like a normal method and new object won't be created. 
    -> Python does not support "method overloading" but it gives a support of "operator overloading".
        and, if you're trying to declare multiple constructors, PVM will always consider only last constructor. 
    

(4) Method vs Constructor: 
    -> Method: 
        -> Method name can be anything. 
        -> Methods won't be executed automatically, we have to call them explicitly. 
        -> per object, we can call method any number of times. 
        -> Inside method, we can write business logic based on our requirement. 

    -> Constructor: 
        -> Constructor name should be __init__().
        -> Constructor will be executed automatically whenever we're creating an object. 
        -> Per obejct constructor will be executed only once. 
        -> Inside constructor, we have to write code to declare & initialize (instance variables). 
