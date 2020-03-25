
import random
def chouyang(a,n):
    p=True
    while p:
        b=random.sample(a,n)
        b.sort()   #排序
        print(b)
        a=list(set(a).difference(set(b)))  #去除已抽样的数据
        if len(a)>0:
            p=True
        else:
            p=False
 
a=list(range(40723101,40723155))
n=5
chouyang(a,n)


