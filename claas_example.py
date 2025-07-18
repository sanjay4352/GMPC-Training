class Human:   # Human class name, use class keyword to create class
    def __init__(self,person_name, person_age:int):  #__(Double underscore) init (Constructor), person_name - variable
        self.name = person_name      #  Values initialize, self.name-> class properties/variable
        self.age = person_age
    
    def greet(self):

        g = f"Welcome {self.name}, you are {self.age} years old."
        print(g)

    def getAgeArea(self):
        if self.age >18 and self.age <=60:
            return "Adult"
        elif self.age > 60:
            return "Senior Citizen"
        else:
            return "Child"

human = Human("Sanjay",80)  #human ->object
# print(human.name)  #use dot to call prop/function
# print(human.age)
# human.greet()
ageGreet = human.getAgeArea()
print(ageGreet)





