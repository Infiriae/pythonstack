def sortasc(arra):
    print('Starting array composition:',arra)
    for x in range(len(arra)):
        mina = x
        for y in range(x+1, len(arra)):
            if arra[mina] > arra[y]:
                mina = y    
        arra[x], arra[mina] = arra[mina], arra[x]
        print('Step',x+1,'completed:',arra)
    return arra


print('Finished Array Composition:',sortasc([9,3,6,5,3,2,8,1,0,9]))