class Human:
    def __init__(self,name,gender):
        self.name=name
        self.gender=gender

    def introduce(self):
        greet= f"Welcome {self.name}!!!"
        return greet

    

obj = Human("Ram","Male")

print(obj.introduce())
