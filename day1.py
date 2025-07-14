a = input("Enter  STring to check Palindrome: ")

if a[0]==a[3]:
    if a[1]==a[2]:
        print("It's a palindrome")
    else:
        print("Not a palindrome")
else:
    print("Not a palindrome")