li=[3,1,1,2,0,0,2,3,3]
li_1=li[:]
li=list(set(li))

i=0
di={}
for i in range(0,4):
    di[i]=li_1.count(i)
    i+=1
print (di)
