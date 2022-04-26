# 猜年龄小游戏
# 1.允许用户最多尝试3次
# 2.每尝试3次后，如果还没猜对，就问用户是否还想玩，如果回答Y和y，就继续让其猜3次，以此往复，如果回答N和n就直接退出
# 3.如果猜对了就直接退出
me='21'
index=0 # 初始值
while index<3:
    if me==int(input('猜下我的年龄：')):
        print('猜对啦！')
        break # 中断循环
    else:
        print('猜错了哦！')
        if index==2:
            Q=input('再试试？') # 三次全部猜错
            if Q=='y' and 'Y':
                print('再试一次吧！')
                index=0 # 重置为初始值
                continue # 跳过这次循环，目的是为了跳过index+=1
            elif Q=='n' and 'N':
                print('游戏结束')
                break
    index+=1
# 标准答案
# times=0
# count=3
# while times<=3:
#     age=int(input('请输入您要猜的年龄...')) # int是因为数字是整形的
#     if age==25:
#         print('猜对了')
#         break # 直接中断循环
#         pass
#     elif age>25:
#         print('猜大了，请再试试')
#         pass
#     else:
#         print('猜小了，请再试试')
#         pass
#     times+=1
#     if times==3:
#         choose=input('想不想继续猜呢？Y/N')
#         if choose=='Y' or choose=='y':
#             times=0
#             pass
#         elif choose=='N' or choose=='n':
#             times=4
#             pass
#         else:
#             print('请输入正确的格式...')
#     pass
