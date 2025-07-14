a=[1,2,3,4]
op = input("Enter Operator: ")
num = input("Enter Number: ")
num = int(num)
if op=='+':
    a.append(num)
elif op=='-':
    if num in a:
        a.remove(num)
    else:
        print("Number not found into list")
else:
    print("Operator Not Supported") 

print(a)   