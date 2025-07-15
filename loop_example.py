# a=[10,20,"abc","56",789.50]

#sequence can be List, Tuple, Range, String
#  for value in sequence:
#     print(value)

# for x in a:
#     print(x)

# 3*1
# 3*2
# 3*3
# 3*4

user_input = input("Enter number to print Table: ") # user_input will be in string

user_input = int(user_input) # Type Cast to multiply with number

# tableNumbers=[1,2,3,4,5,6,7,8,9,10]
tableNumbers = range(1,11)

for x in tableNumbers:
    print(x*user_input)




