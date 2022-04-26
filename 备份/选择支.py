# 假设主人公是ALPHA，给出如下选项
# A='选择Alpha'
# B='选择Sigma'
count=1
while count<=10:
    me=input('A=选择Alpha B=选择Sigma 你要选择谁:')
    print(me) #检查输出
    if me=='A':
        print('ALPHA:我一直相信着你！')
        pass
    elif me=='B':
        print('ALPHA:你背叛我了呢...')
        pass
    else:
        print('...你在说什么？')
        pass
    count+=1