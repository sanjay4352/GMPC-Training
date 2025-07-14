a=20
b=24
c=30

a_multiplier = int(a*b*c/a)
b_multiplier = int(a*b*c/b)
c_multiplier = int(a*b*c/c)

list_a=[]
list_b=[]
list_c=[]

for x in range(1,a_multiplier+1):
    list_a.append(a*x)

for x in range(1,b_multiplier+1):
    list_b.append(b*x)

for x in range(1,c_multiplier+1):
    list_c.append(c*x)

