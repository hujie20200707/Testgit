#s = input('birth:')
#birth = int(s)
#if birth < 2000:
    #print('00前')
#else:
    #print('00后')
height = 2.75; weight = 80.5;
BMI = weight/(height**2);
print('BMI为:',BMI)
if BMI < 18.5:
    print('过轻')
elif BMI < 25:
    print('正常')
elif BMI < 28:
    print('过重')
elif BMI < 32:
    print('严重肥胖')
