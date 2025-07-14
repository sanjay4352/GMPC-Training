class Calculator:

    def __init__(self, first_number=None, second_number=None):
        self.first_number=first_number
        self.second_number=second_number

    def add(self):
        return self.first_number+self.second_number
    def sub(self):
        return self.first_number-self.second_number
    


calc = Calculator()

calc.first_number=10
calc.second_number=20

print(calc.sub())
# print(calc.second_number)