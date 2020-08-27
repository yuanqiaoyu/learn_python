#函数参数课后作业
#方案1：
def product(*args):
    if len(args)==0:
        raise TypeError
    else:
        pro=1
    for i in args:
        pro=pro*i
    return pro

#方案2：
import numpy
def product(*args):
    if len(args)==0:
        raise TypeError
    else:
        result=numpy.prod(tuple(args))
        return result

#方案3：
from functools import reduce
def product(*args):
    if len(args)==0:
        raise TypeError
    else:
        result=reduce((lambda x,y:x*y),tuple(args))
        return result


print('product(5) =', product(5))
print('product(5, 6) =', product(5, 6))
print('product(5, 6, 7) =', product(5, 6, 7))
print('product(5, 6, 7, 9) =', product(5, 6, 7, 9))
if product(5) != 5:
    print('测试失败!')
elif product(5, 6) != 30:
    print('测试失败!')
elif product(5, 6, 7) != 210:
    print('测试失败!')
elif product(5, 6, 7, 9) != 1890:
    print('测试失败!')
else:
    try:
        product()
        print('测试失败!')
    except TypeError:
        print('测试成功!')





