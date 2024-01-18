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
Explanation: 
-> A class "Student" is been used to create the class. 
-> Under that class, we've defined a constructor (__init__) and a method (talk())
-> then, with the help of reference variable, we'ver created a object on line no- 19
-> After that, we have seen the output by printing the properties present inside the constructor. 
-> If you cann se, we have also printed the method "talk()" without using the print() function, just by pointing the method to the reference variable -> s. 

Hope you've understood this basic concept of class, object, method, reference variable
'''