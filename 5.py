#input函数的使用

#解决一元二次方程的程序
a=float(input("请输入二次项的系数："))
b=float(input("请输入一次项的系数："))
c=float(input("请输入常数值："))
x1=(-b+b**2-(4*a*c)**1/2)/2*a
x2=(-b-b**2-(4*a*c)**1/2)/2*a
print("X1的值为："+str(x1))        #注意，在输出的时候，需要把x1，x2用“str（）”转换为字符串才能输出
print("X2的值为："+str(x2))