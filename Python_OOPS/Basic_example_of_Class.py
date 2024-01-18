''' This is the example of just understanding the class,method,object,reference variable
Concepts of these (4) terms are discussed in the "Tutorial_OOPS.md file -> Go and check it there '''

class Student: 
    #defining the constructor
    def __init__(self): 
        self.name="James"
        self.roll_number=101
        self.marks=90

    #now, below are all the methods (functions) defined
    def talk(self):
        print("Hello I'm: ",self.name)
        print("My Roll_no: ",self.roll_number)
        print("My Marks are: ",self.marks)
    

#defining the object. 
s=Student()

print(s.name, s.roll_number, s.marks)
print("---------------------------------")
s.talk()


'''
How to run this code: 
1. First go into the directory of your source code by using the command : cd
2. Then at the terminal type: python file_name
e.g. -> python Basic_example_of_Class.py (in this file name is: Basic_example_of_Class.py that's present inside the Python_OOPS folder)

NOTE: if the pointer is not present in this directory, then you might see the error like: NO such file or directory, 
to avoid that, check your directory where the source code is present.

'''
'''
Explanation: 
-> A class "Student" is been used to create the class. 
-> Under that class, we've defined a constructor (__init__) and a method (talk())
-> then, with the help of reference variable, we'ver created a object on line no- 19
-> After that, we have seen the output by printing the properties present inside the constructor. 
-> If you cann se, we have also printed the method "talk()" without using the print() function, just by pointing the method to the reference variable -> s. 

Hope you've understood this basic concept of class, object, method, reference variable
'''
if s1==s2: 
    return True 
else: 
    return False 