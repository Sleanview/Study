# 九九乘法表用for来实现
# for i in range(1,10):
#     for j in range(1,i+1):
#         print('%d*%d=%d'%(i,j,i*j),end=' ')
#         pass
#     print() # 控制换行
#     pass

# for-else的使用
# for item in range(1,11):
#     print(item,end=' ')
#     if item>=5:
#         break
#     pass
# else:
#     print('就是在上面循环当中只要出现break 那么else的代码不再执行')

# account='lbr'
# pwd='123'
# for i in range(3):
#     acc=input('请输入账号：')
#     pd=input('请输入密码：')
#     if account==acc and pwd==pd:
#         print('登陆成功')
#         break
#     print('账号或密码错误')
# else:
#     print('您的账户被锁定')

# while-else

index=1
while index<=10:
    print(index)
    if index==6:
        break
    index+=1
    pass
else:
    print('else执行了吗')