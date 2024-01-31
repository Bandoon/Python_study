#len函数
print(len("hallo"))        #输出的内容为字符串的长度，空格、数字、符号均会占据一个长度，但是完整的一个转义符才算一个长度（注意加双引号）

#检索功能
print("hallo"[3])          #[]有检索功能，里面的数字代表检索字符串中的第几个字符（从0开始数）

#布尔类型
b1=True
b2=False

#空值类型
girl_friend=None

print(type("hallo"))       #type函数用于确认需要输出的函数的类型,‘str’指字符串 ‘int’指整数 ‘float’指浮点数 ‘bool‘指布尔类型 ’NoneType‘指空值类型
print(type(b1))
print(type(b2))
print(type(girl_friend))
print(type(1.5))