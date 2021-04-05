#1 
# prints 5 because value return.
def a():
    return 5
print(a())

#2
#prints 10 because both returned values are numbers
def a():
    return 5
print(a()+a())

#3
#prints 5 because function ends at return.
def a():
    return 5
    return 10
print(a())

#5
#prints 5 at x definition because x = a() runs function.
#prints null because no return is given to put a value in x
def a():
    print(5)
x = a()
print(x)

#6
#prints 3, then 5, then error becaue there is no return for the print.
#commented out the call to allow pass for future problems
def a(b,c):
    print(b+c)
#print(a(1,2) + a(2,3))

#7
#prints 25 because of string conversion return.
def a(b,c):
    return str(b)+str(c)
print(a(2,5))

#8
#prints 100, 10. Because of linear return statement
def a():
    b = 100
    print(b)
    if b < 10:
        return 5
    else:
        return 10
    return 7
print(a())

#9
#prints 7, 14, 21 because there are return values that can be added.
def a(b,c):
    if b<c:
        return 7
    else:
        return 14
    return 3
print(a(2,3))
print(a(5,3))
print(a(2,3) + a(5,3))

#10
#prints 8 because linear return.
def a(b,c):
    return b+c
    return 10
print(a(3,5))

#11
#prints 500, 500, 300, 500 because it did not pass value out of function
b = 500
print(b)
def a():
    b = 300
    print(b)
print(b)
a()
print(b)

#12
#prints 500,500,300,500 because variable is not passed out of function
b = 500
print(b)
def a():
    b = 300
    print(b)
    return b
print(b)
a()
print(b)

#13
#prints 500,500,300,300 because variable is passed out of function with return to b.
b = 500
print(b)
def a():
    b = 300
    print(b)
    return b
print(b)
b=a()
print(b)

#14
#prints 1,3,2 because of call mid function.
def a():
    print(1)
    b()
    print(2)
def b():
    print(3)
a()

#15
#prints 1, 3, 5, 10 because of static print values and returns.
def a():
    print(1)
    x = b()
    print(x)
    return 10
def b():
    print(3)
    return 5
y = a()
print(y)

