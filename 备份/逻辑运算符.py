# 逻辑运算符 and or not
# and 条件比较严格 两边结果必须为Ture 否则False
# 定义四个变量
a,b,c,d=23,18,10,3
print(a+b>c and c<d) #False
print(c>d and a>b)
# or 一个条件满足即可
print(a<b or b>d)
# not 取反 真假切换
print(not a>b)
# 优先级
# ()->not->and->or
print(2>1 and 1<4 or 2<3 and 9>6 or 2<4 and 3<2)
# 赋值运算符
# += -= *= /= %= **=
a,b,c,d=23,18,10,3
a+=c
# 加法赋值运算符 a+=c 等效于 a=a+c
a**=2
# 幂赋值运算符  a**=c 等效于 a=a**c
print(a) #赋值后a就刷新了
# print()