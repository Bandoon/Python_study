#赋值操作
great="吃了吗您"
print(great)    #这样输出的great就是”吃了吗您“，但是注意输出的great前后不要加引号，否则输出的就是great
#给赋过值的函数以新的名称
great_chinese=great    #新的名称写在旧的名称前，这里是这里是给great重新命名为great_chinese，在这里great就是一个没有赋过的值
great_english="what\'up"
great=great_english      #重新赋值一个great_english，在将其赋值给great
print(great+" 张三")
print(great_chinese+" lisi")