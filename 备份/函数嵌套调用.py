# 函数嵌套
def fun1():
    print('-------------------fun1 start-----------------------')
    print('-------------------执行代码省略-----------------------')
    print('-------------------fun1 end-----------------------')
    pass

def fun2():
    print('-------------------fun2 start-----------------------')
    # 调用第一个函数
    fun1()
    print('-------------------fun2 end-----------------------')
    pass

fun2() #调用函数2

# 函数的分类：根据函数的返回值和函数的参数
# 有参数无返回值
# 有参数有返回值
# 无参数有返回值
# 无参数无返回值