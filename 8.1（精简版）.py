#项目8存在的bug（已发现的）：
#在进入循环后，在询问“还想买什么？”时在输入除“y/n”以外的字符没有提醒
#不够精简

#做一个购物清单
import sys

shopping_list=[]                                    #变量名+“[]”为列表
a=input("请输入你想要买的东西：")                        #购买的第一件商品

if  not a !="枪" or not a!="刀":                     #禁止购买违禁物品
    print("FBI WARNING")
    sys.exit()

a_money=float(input("这个商品预计花费为(rmb)"))         #预计花费用浮点数！！
shopping_list.append(a)                             #使用变量名+“.append”指在列表中添加。。
money=a_money                                       #money指总的花费

still_have=input("还有吗？？（输入y/n）")

while not still_have != "y":  # 循环开始，当一直输入yes时。。
    x = input("还想买什么呢？？")  # 购买的第X件商品

    if not x != "枪" or not x != "刀":  # 禁止购买违禁物品
        print("FBI WARNING")
        sys.exit()

    x_money = float(input("这个商品预计花费为(rmb)"))
    shopping_list.append(x)
    money = money + x_money  # 第二个money第一次运算是指帝26行的money，后面的就是指37行第一个money
    still_have = input("还有吗？？（输入y/n）")

if not still_have!=("n"):
    print ("你想买的东西有："+str(shopping_list))
    print("数量为" + str(len(shopping_list)))
    print("预计花费为："+str (money))

else:
    print("玩你M呢！！")