L=0 #插值结果

n=5 #插值数据个数

x_arry=[] #插值点的x坐标

for k in range(n):
    x_arry.append(k+1)

x=2.5 #代入的x值

l=1 #循环计算的l(k)值

for i in range(n):
    
    for j in range(n):
        
        if(i!=j):
            
            l*=(x-x_arry[j])/(x_arry[i]-x_arry[j])
            print("l结果为:"+str(l))
                    
    y=x_arry[i]*2+3 #函数式，求函数值
    print("y结果为:"+str(y))
    
    L+=l*y
    
print("插值估计结果为:"+str(L))