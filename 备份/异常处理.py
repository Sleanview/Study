# try:
#     x=eval(input('请输入整数'))
#     print(x)
# except:
#     print('输入格式错误')

# 例2
try:
    num = eval(input('请输入整数'))
    print(num*2)
except NameError:
    print('输入不是整数')