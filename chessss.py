import random as r

w = r.randint(8,12)
h = r.randint(8,12)

m =[]
d = 1,0
q= 0
print(w, h)
while q < h/2:
    q = q + 1
    mm = [0,1]*((w+1)//2)
    ss = [1,0]*((w+1)//2)
    m.append(mm)#массив
    m.append(ss)


for aa in m:
    print(aa)
    

