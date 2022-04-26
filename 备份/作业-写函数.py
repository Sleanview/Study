# 写函数，接收n个数字，求这些参数数字的和
def sumFunc(*args):
    # 处理接收的数据
    result=0
    for item in args:
        result+=item
        pass
    return result
# 调用
rs=sumFunc(1,2,3,4)
print('rs={}'.format(rs))  # format 格式化输出
# print('总和是%d'%(x))

# 写函数，找出传入的列表或元组的奇数位对应的元素，并返回一个新的列表
def process_Func(con):
    listnew=[]
    index=1
    for i in con:
        if index%2==1: # 判断奇数位
            listnew.append(i)
            pass
        index+=1
        pass
    return listnew

rs3=process_Func([1,2,3,4,5,6,7])
print(rs3)
# 写函数，检查传入字典的每一个value的长度，如果大于2，那么仅保留两个长度的内容，并将新内容返回给调用者。
# PS：字典中的列表只能是字符串或列表