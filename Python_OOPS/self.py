'''
Let's understand "self" variable, not a keyword 😄.
Yeah, I know confusion would be there - b/w keyword and variable --> what is (self): No-worries, within minute, we would discuss this. 

1) 'self' is a (reference variable) which is always pointing to (current object).
    Within the python class, to access (current object), we need to "self".

'''
#e.g. >> 
class Test: 
    def __init__(self): 
        print("Address of object reference by self: ", id(self))

t=Test()
print("Address of object referenced by t: ",id(t))
print("------------------------------------------------------------------------")

'''
Now, if you'll see the addresses of both (t and self) would be same: 744 => this shows that like (t), 'self' is also a reference variable.

2) The first argument to constructor is always 'self'.
    The first argument to (instance method) is always 'self'.
    We're not required to provide value for 'self' variable, Python Virtual machine (PVM) itself provides (1) value

3) We can use (self) always within the clas only. 
    Inside [constructor] we can use (self) to declare (object related variables [instance variables])
    Inside [instance method] we can use (self) to access (values of instance variables) 
'''

'''
Now, let's see what is 'self' - variable or keyword.
As discussed above, I think you're well versed that 'self' is a reference variable, 
But is it keyword also?? 

Let's see: 
(4) 'self' is (not) a keyword, we can write any name like: delf,kelf, hello, whathever you wanna write on the first positional argument in constructor.
Because: in Python, 1st positional argument always gets treated like a 'self' keyword (or) reference keyword only.
Let's understand by the below example: 
'''
class Student: 
    def __init__(delf,name,roll_number):
        delf.name=name
        delf.roll_number=roll_number

s1=Student('Amit',101)
print(s1.name,s1.roll_number)
print("==================================================================================")
# So, once you run it: you'll get o/p as -> Amit 101 (that mentioned in line: 45).


# Let's take one more example where we'll take (1) method this time. 
class Student: 
    def __init__(delf,name,roll_number): 
        delf.name=name
        delf.roll_number=roll_number
    
    def activity(kelf):
        print("He's the person who scored 100 in cricket: ",kelf.name)
        print("He's having the roll_number: ",kelf.roll_number)
    
s1=Student('Jammy',101)
s1.activity()


'''
YOu run the above code, and see what you get, 
Hope you get the correct output without getting any typeError 😁.

After seeing, the above example where we have used delf inspite of 'self' we can say: 
(self) is not a [keyword] it's the [variable]

I think now, it's clear: what is (self) - a (keyword) or (variable) 
So, what is self -> keyword or variable 😄.

In the next file: constructor.py we would see what is __init__ and what is a constructor in detial.
'''

print("-----------------------------------------------------")