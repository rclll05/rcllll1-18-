x = 10>30 and 50<100
y = 10<30 and 50<100
z = 100>200 and 50<(3/0) #发生短路，后面代码不被执行
print(x)
print(y)
print(z)

#k = 100<200 and 50<(3/0)  与发生短路的情况对比，报错
#print(k)

f = 200
g = 50<f<500
g2 = 50<f and f<500
print(g)
print(g2)