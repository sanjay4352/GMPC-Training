file = open("demo.txt","r+")

# a=["This is demo string 1","This is demo string 2"]
file.write("\nThis is demo string additonal data")  #single string data write
# file.writelines(a) # multiple string data write

# print(file.readlines()) # convert all lines into list


# print(file.readline()) # read first line from file, return string

print(file.read()) # read all data from file


file.close()