'''
OKay, as you have learnt basics in OOPS, so let's try to implement that Basics what we've have learnt till now.
Just a spoiler alert: Up till now, We have learnt the following -> 
1. Class, object, reference variable
2. Use of (self variable) and (costructor)
'''

'''
Idea is to print the Movie information, where we would be taking the input from the user as: title, hero_name, heroine_name
'''
class Movie: 
    # Constructor is required to define the properties.
    def __init__(self, title, hero, heroine):
        self.title=title
        self.hero=hero
        self.heroine=heroine
    
    # now, creating a method which will print the details of movie. 
    def info(self):
        print("The Movie name is: ",self.title)
        print("The Hero name is: ",self.hero)
        print("The Heroine name is: ",self.heroine)


# Now, let's take the user_input()
list_of_movies=[]
while True: 
    title=input("Enter the movie name: ")
    hero=input("Enter the hero name: ")
    heroine=input("Enter the heroine name: ")

    m=Movie(title,hero,heroine)
    list_of_movies.append(m)

    option=input("Do you want to provide more details about movie: [Yes/No] ? ")
    print() 
    if option.lower()=='no':
        break 
    print()


# Let's print the movie information stored inside the list. 
for movie in list_of_movies:
    movie.info() 
    print()