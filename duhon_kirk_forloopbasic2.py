def bign(arra):
    for x in range(len(arra)):
        if arra[x] > 0:
            arra[x] = 'big'    
    return arra

arrb=bign([-9,0,-3,4,1,-2,6,-23])
print(arrb)

def copo(arrc):
    suma = 0
    for x in range(len(arrc)):
        if arrc[x] > 0:
            suma+=1
    arrc[len(arrc)-1] = suma
    return arrc

arrd=copo([-5,2,-3,5,1,0,0,2,0,-3,0])
print(arrd)

def howhigh(arre):
    sumb = 0
    for x in range (len(arre)):
        sumb+=arre[x]
    return sumb

outa=howhigh([1,5,-5,2,3,10,-9,-8,10,3])
print(outa)

def avear(arrf):
    sumc = 0
    for x in range(len(arrf)):
        sumc+=arrf[x]
    return (sumc/len(arrf))

outb=avear([9,3,7,5,1,2,1,-4,-12,4])
print(outb)

def lear(arrg):
    return len(arrg)


print(lear([]))

def minar(arrh):
    if len(arrh) > 0:
        mina = 0
        for x in range(len(arrh)):
            if arrh[x] < mina:
                mina = arrh[x]
        return mina
    else:
        return "False"

outc=minar([1,10,-4,-30,23,14,-2])
print(outc)

def maxar(arrh):
    if len(arrh) > 0:
        maxa = 0
        for x in range(len(arrh)):
            if arrh[x] > maxa:
                maxa = arrh[x]
        return maxa
    else:
        return "False"

outd=maxar([1,10,-4,-30,23,14,-2])
print(outd)

def dictar(arri):
    sumc=0
    minb=0
    maxb=0
    dicta={}
    for x in range(len(arri)):
        if arri[x] > maxb:
            maxb = arri[x]
        if arri[x] < minb:
            minb = arri[x]
        sumc+=arri[x]
    dicta['sumTotal'] = sumc
    dicta['average'] = (sumc/len(arri))
    dicta['minimum'] = minb
    dicta['maximum'] = maxb
    dicta['length'] = len(arri)
    return dicta

oute=dictar([1,10,-4,-30,23,14,-2])
print(oute)

def revli(arrj):
    nulen = len(arrj)
    for x in range(len(arrj)-1,-1,-1):
        arrj.append(arrj[x])
    for y in range(0,nulen,1):
        del arrj[0]
    return arrj

print(revli([-1,2,0,7,9,12]))

