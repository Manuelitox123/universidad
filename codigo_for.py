u=1;d=1;c=1
for c in range(9):
    c+=1
    for d in range (9):
        d+=1
        for u in range (9):
            u+=1
            if (c+u+d) > 20:
                print (str(c),str(u),str(d)) 
                d+= (c+u+d)


