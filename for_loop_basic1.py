for x in range(151):
    print(x)

for x in range(5,1001,5):
    print(x)

for x in range(1,101):
    if x % 10 == 0:
        print("Coding Dojo")
    elif x % 5 == 0:
        print("Coding")
    else:
        print(x)

sum = 0
for x in range(500001):
    if x % 2 != 0:
        sum = sum + x
print(sum)

for x in range(2018,0,-4):
    print(x)

def flex(ln,hn,ml):
    for x in range(ln,hn):
        if x % ml == 0:
            print(x)


flex(1,50,7)