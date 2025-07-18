myVar = "This is demo String"

# print(len(myVar)) #Get length of string
# print(myVar[-2]) #get char by index. Negative index will start from -1, that fetch from right side of string
# print(myVar[1]) #get char by index. Positive index will start from 0, that fetch string left side


# print(myVar[1:5]) #slicing : start index, end index
# print(myVar[5:15]) #slicing : start index, end index


# print(myVar.upper()) #upper function will convert string into uppercase
# print(myVar.lower()) # lower function will convert string into lowercase
# for x in myVar:
#     print(x.upper()) #convert into uppercase



x ="My city is patna"
# print(x)
# print(x.strip()) # Remove extra space from left and right of string

# x=x.replace("demo","class") # you have to store into another varible. provide old and new value into replace function
# print(x)

wordslist = x.split("city is") #split convert into list by breaking string of given literal
print(wordslist)


# print(x.find("is")) # find will give you first found string into given string

# print(x.find("america")) # if not found then it will return -1


# a="first"
# b="second"

# c = a+b # concat string using symbol +
# print(c)


# name="Sanjay"
# roll=1234
# gender="male"

# c = f"My name is {name} and having roll number is {roll}. My gender is {gender}" # for formatted string use f char at starting of string.
# use variable using {} inside the string
# print(c)