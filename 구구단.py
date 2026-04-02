for i in range(2,10):
    print("#", i ,"단 #",end = '\t ')

for j in range(1,10):
    for k in range(2,10):
        print("%d X %d = %2d"%(k,j,j*k),end = '\t ')