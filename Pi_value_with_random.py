import random
soma=0
k=0
for i in range(10000000000):
    y=random.random()
    y2=random.random()
    x=2*y-1
    x2=2*y2-1
    j=(x**2)+(y**2)
    k=k+1
    if j<=1:
        soma=soma+1
numero=soma/k
pi=numero*4
print(pi)

    
