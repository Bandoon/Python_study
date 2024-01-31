#input函数的使用+if函数的应用

#解决一元二次方程的程序
a=float(input("请输入二次项的系数："))
b=float(input("请输入一次项的系数："))
c=float(input("请输入常数值："))
xa=(-b+b**2-(4*a*c)**1/2)/2*a
xb=(-b-b**2-(4*a*c)**1/2)/2*a
x1=float(input("请输入你计算的x1的值："))
x2=float(input("请输入你计算的x2的值："))
if x1>xa or x1<xa or x2>xb or x2<xb:
    print("我妈，这都能算错了，怎搞哦（老夏音）！！！")
else:
    print("哇，你真棒（菲菲公主音）")