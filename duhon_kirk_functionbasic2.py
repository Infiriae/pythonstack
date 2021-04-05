def cndo(fir):
    farr = []
    for x in range(fir,-1,-1):
        farr.append(x)
    return farr

print(cndo(7))

def prre(a,b):
    print(a)
    return b

prre(2, 8)

def filen(ar):
    if type(ar) == list:
        print(ar[0] + len(ar))
    else:
        print("AR should be array or list")

filen([1,2,3,4,5])

def newnu(arr):
    numt = []
    if len(arr) > 2:
        for x in arr:
            if x > arr[1]:
                numt.append(x)
        print(len(numt))
        return numt
    else: 
        return "False"

print(newnu([1,2]))
print(newnu([9,4,2,5,7,6,9,12]))

def mtar(si,va):
    outarr = []
    for x in range(si):
        outarr.append(va)
    return outarr

print(mtar(5,3))
