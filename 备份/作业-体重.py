# 小王 height:175 weight:80.5 BMI=weight/height**2 使用if-elif
# height=1.75
# weight=80.5
# BMI=weight/height**2
# if BMI<18.5:
#     print('BMI=',BMI,'过轻')
# elif 18.5<=BMI<25:
#     print('BMI=',BMI,'正常')
# elif 25<=BMI<32:
#     print('BMI=',BMI,'肥胖')
# elif BMI>32:
#     print('BMI=',BMI,'严重肥胖')
#     pass

height=1.75
weight=80.5
BMI=weight/height**2
if BMI<18.5:
    print('BMI=%d,过轻'%(BMI))
elif 18.5<=BMI<25:
    print('BMI=%d,正常'%(BMI))
elif 25<=BMI<32:
    print('BMI=%d,肥胖'%(BMI))
elif BMI>32:
    print('BMI=%d,严重肥胖'%(BMI))
    pass