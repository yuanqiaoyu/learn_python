#廖雪峰python教程笔记

#要从机器码反推出C语言代码是不可能的，凡是编译型的语言都不存在这个问题。而解释型的语言要让人家拿去运行就必须把源代码给人家。
#python解释器之：1 CPython 由于是用C语言写的所以叫CPython,python的官方解释器。2 IPython 升级交互方式的CPython，不同于
#CPython的>>>提示符，IPython的提示符是In[序号]: 3 PyPy 它的目标是运行速度，可以对python进行动态编译（注意：不是解释），
#而且PyPy与CPython是有一些不同的。4 JPython JAVA平台的解释器，可以将python代码编译成JAVA字节码。5 IronPython 微软.NET
#平台的python解释器。

#直接运行.py文件 在windows上是不能像.exe文件那样直接运行.py文件的，而在mac和linux 上则可以。方法是在.py文件的第一行加上
#  #/usr/bin/env python3 后再给文件赋予权限 $ chmod a+x xxx.py

#input()输入后默认是字符串

#变量本身类型不固定的语言称为动态语言。另外，请改变根深蒂固的数学思维，python中的"="是赋值。python中变量在计算机中的内存表示
#如：a=abc，这时计算机干了两件事，一是在内存中创建了abc，二是创建了a，把a指向了abc。如果a=b，则b也指向了abc。后期改变了a的值
#变量b是不会跟随一起变化的。

#在python中用全部大写表示常量，但是python没有任何机制保证这个常量不会被改变。

#如何输出格式化的字符串
#print('%d-%d'%(3,1))
#作业1：练习
#小明的成绩从去年的72分提升到了今年的85分，请计算小明成绩提升的百分点，并用字符串格式化显示出'xx.x%'，只保留小数点后1位：
#s1=75
#s2=82
#r=(82-75)/85*100
#print('%.1f%%'%r)

#要搞清楚Unicode和UTF-8的区别：Unicode是全球通用的编码格式，可以编码显示所有的文本。而UTF-8是文本转换成bytes的编码格式。
#python通过encode和decode方法支持多种编解码。如GB2312，ASCII

#把元素插入到列表指定的位置：A.insert(位置索引，元素) 删除用pop（）同理
#注意：定义只有一个元素的tuple必须在元素后面加一个","。在显示的时候同样要显示这个","因为一个括号里面一个元素没有逗号会与数学
#上计算括号产生冲突。tuple里面有列表的话，列表里面的元素是可以变化的。所谓的tuple一旦创建不能改变是指指向不变。
#列表中包含另外的列表，取其中的元素方法：
'''L = [
    ['Apple', 'Google', 'Microsoft'],
    ['Java', 'Python', 'Ruby', 'PHP'],
    ['Adam', 'Bart', 'Lisa']
]
print(L[0][0])'''

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





