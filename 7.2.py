# BMI=体重/(身高**2)
# 和7.1相比，跟新了防呆瓜功能，详见32-33
import sys

user_weight = float(input("请输入你的体重（单位：kg）："))
if user_weight > 1000:
    print("玩你M呢!!")
    sys.exit()              #指直接结束进程

user_height = float(input("请输入你的身高（单位：m）："))
if user_height > 3:
    print("玩你M呢!!")
    sys.exit()

BMI = user_weight / user_height ** 2

if BMI < 18.5:
    user_like = "你怎么瘦的和泥志豪一样！！"
elif 18.5 <= BMI < 24:
    user_like = "你好壮哦，和大猩猩一样，我好喜欢！！"
elif 24 <= BMI < 28:
    user_like = "好大，和狒狒一样，好喜欢。。"
elif BMI >= 28:
    user_like = "肥猪！！"

print("你的BMI值为："+str(BMI))
user_want=input("想知道自己和那种动物更像？(输入yes/no):")
if not user_want!="no":
    print("这不是你想不知道就不知道的，"+user_like)
elif not user_want!="yes":                               #“not”+“!=”不就是等于吗，哈哈，我真聪敏
    print("请允许我夸夸你，"+user_like)
elif user_want!="yes"and"no":
    print("玩你M呢!!")