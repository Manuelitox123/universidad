x=0; y =0 ; z= 0; intentos= 0; famas= 0 ; toques= 0; import random

N = 0


while N < 100 :
    N += 1
    A= random.randint(0, 9)
    B= random.randint(0, 9)
    C= random.randint(0, 9)
    while A == B or A == C : 
        A = random.randint(0, 9)
    while B == A or B == C : 
        B = random.randint(0, 9)
    while C == A or C == B : 
        C = random.randint(0, 9)
    if A == B or A == C or C == B :
        print("==========================================")
    print(A,B,C)

