#第一章 初识python

#1-3

import time
for i in range(31):
	print(i)
	time.sleep(1)

#第二章 变量 数据类型和运算符

#2-4数据类型转换

yue=20000
cunkuan="1000"
print("存款后，余额为：",yue+int(cunkuan))
a="35.23"
b=50
c=3.14
d=""
e=0
f=None
print("转换前：",type(b))
a=float(a)
print("转换后:",type(b))
a=1==1
b=3!=3
c=True
print(b)

#2-7

a=[1,2,3,4,"hello","世界"]
a[3]="张三"#列表定位的替换修改
#print(a)

#2-8

#列表的切片
#print(a[0:4])
#print(a[-4:-1])#逆向切片
#列表的添加与删除
a.append()
a.remove()
del a[]
a.pop()
a.insert(索引位置号,添加元素)
#获取列表长度
print(len(a))

#2-9元组和字典

#a=()同列表一样，只是不能改变其中的元素
#a={"name":"zhangsan","age":14.....}是一种大小可变的键值对集，键不允许重复

#2-10集合

a={}或者a=set([])集合里的元素不能重复
#列表的去重
list1=[1,1,2,2,3,3,4,4,5,5,6,6]
x=set(list1)
y=list(x)
a={} b={}
print(a-b)差集 (a|b)并集 (a&b)交集 (a^b)对称差(并集下的去交集)

第三章 选择结构（顺序，选择，循环）

3-1 if else
#第四章 循环结构
#4-1

for i in range(1000,步长 ):
	print("hello world")

#4-3案例 求和与最大值

summ=0
for x in range(0,101,2):
	summ=summ+x
print(summ)
a=[465411,6,5641,64,64,5634,6978974,654848]
maxx=a[0]
for x in range(0,len(a)-1):
	if maxx<=a[x+1]:
		maxx=a[x+1]
print(maxx)

#4-4while循环

i=0#初始值
while i<=100:#循环条件
	print(i)
	i=i+1#改变初始值

#4-5循环嵌套


i=1
summ=0
while i<=20:#外层循环总共执行20次
	print("第",i,"年到了...")
	if i==10:
		print("今年你受伤了，就不用给了！")
		i=i+1
		#continue#结束本次循环，直接开始下一次循环
		#break#结束所有循环
	j=1
	while j<=12:#嵌套循环是外层循环每执行1次，它就执行12次。
		summ=summ+1200
		if j==6:
			j=j+1
			#continue
			#break
		print("第",i,"年,第",j,"月,支付彩礼1200！累计共支付",round(summ,2),"元")
		j=j+1
	i=i+1

#4-7无限循环

while1==1

#4-8 银行存款案例

card1="1001"
pwd1="123456"
ban1=10000
card2="1002"
pwd2="123456"
ban2=10000
card3="1003"
pwd3="123456"
ban3=10000
print("欢迎来到中国银行！")
times=1
while True:
	card=input("请输入银行卡号：")
	pwd=input("请输入密码：")
	ban=0
	if card==card1 and pwd==pwd1:
		ban=ban1
	elif card==card2 and pwd==pwd2:
		ban=ban2
	elif card==card3 and pwd==pwd3:
		ban=ban3
	else:
		times=times+1
		if times>=3:
			print("卡号密码输入错误！请联系柜台！")
			break
		else:
			print("卡号密码第",times,"次输入错误！请重新输入！")
			continue
	while True:
		num=input("请输入您要办理的业务：1.存款 2.取款 3.退卡")
		if num=="1":
			inn=float(input("请输入您的存款金额："))
			if inn<=0:
				print("存款金额请大于0！")
				continue
			else:
				ban=ban+inn
				print("存款成功！存入：",inn,"余额为:",ban)
		elif num=="2":
			out=float(input("请输入您的取款金额："))
			if out>ban:
				print("余额不足！")
				continue
			else:
				ban=ban-out
				print("取款成功！取出：",out,"余额为:",ban)
		elif num=="3":
			print("请收好您的卡片！")
			break
		else:
			print("输入有误！")
			continue

第五章 函数和模块
5-1

def f1(a):#1.先定义一个名为f1的函数
	print(a,"方法f1被执行了")#3.通过函数f1(a)拿到了666
f1("666,")#2.把666赋给了a
def add(a,b,c,d):
	e=a+b+c+d
	return e
print("本次相加的结果为：",add(132,1,2,33))

5-4 函数的深入理解案例

def zzj(f):
	if f=="苹果" or f=="李子" or f=="桃子":
		print("正在榨汁！")
		print("两分钟后...")
		zhi="一杯"+f+"汁"
		return zhi
	else:
		print("不能榨取！")
zzj("")


5-4 参数的传入
#几种参数设定方法：顺序传入 关键词 默认参数 不定长参数
def show(name,age,sex,hobby):#形参
	print("我叫：",name,"年龄：",age,"性别：",sex,"爱好：",hobby)
show("张三",18,"男","打球")#实参 #顺序传入
show("张三",sex="男",hobby="看书",age=18)#关键词传入
show(name,sex,hobby,age=18):#默认参数传入 必须列在最后面 但如果手动在实参中定义的参数与形参有冲突 则优先级在实参
def addd(*args):#主要是* 后面用其他名也可以，习惯性用args 之后会在函数内部形成一个以元组形式的封装
	summ=0
	for i in args:
		summ=summ+i
	return summ
print(addd(3,213,166))

5-6 内置函数

maxx=max(s)
import random#生成随机数的模块
a=random.random()#用random模块调用了它自己的方法 即模块.方法
b=random.choice()#这个例子调用了random模块中的另外一个函数方法choice
#5-7
#from random import choice#这种引入方式不需要random.choice()直接print(choice[])这时候只能用choice一种方法
#from random import N种方法或则from random import *
from random import *#import*与import random的区别在于在print的时候就不需要random.randint(),即直接方法名执行就行了
print(randint(1,1000))#生成一个1到1000的随机整数
def f1():
	print("方法f1被执行了！")#自定义模块以被调用

5-9实用内置模块

from urllib import request
url="http://www.baidu.com"
data=request.urlopen(url).read()
print(data.decode())#最基本的一个爬虫
import os
os.system(r"C:\Program Files (x86)\Adobe\Acrobat Reader DC\Reader\AcroRd32.exe")
#打开应用程序
os.rename()#重命名
import webbrowser
webbrowser.open("https://www.baidu.com/")
从网站下载下来的.whl文件用cmd 路径加pip install 文件名安装

第六章 文件读写
fh1=open("文件路径","r")#fh1为文件的句柄 "w"代表文件的写入
data=fh1.read()#write("")这种方式是覆盖了原文本，如果不想清除则用"a" apend追加写入
data1=fh1.readline()#按行读取
datas=fh1.readlines()#按行读取所有，与fh1.read()的区别是把文档读取生成一个列表，这样就可以对列表进行操作。
print(data)
fh1.close()
for i in fh1:#这种读写方式适合大文件，与fh1.readlines相比不占用计算机资源
	print(i)

6-4 读写二进制文件

fh1=open("文件路径","rb")#读取fh1=open("文件路径","wb")#粘贴
data=fh1.read()#data=fh1.write()
print(data)

第七章 面向对象
面向对象是相对于面向过程来讲的，之前几章学的都是面向过程。面向过程的思维方式是根据想要的
结果，通过大脑思维构想出事件的先后顺序写入代码，代码执行也是根据这个顺序来执行。
在编程中，面向对象中的对象可以是万事万物。而对象都可以归为一“类”，比如狗是一个“类”，而指定地方指定人物家的狗就是一个对象。
就像我们写文章一样，有事情起因经过结果，也有人物地点各种性格特点等。描述事物的角度和侧重点会有所不同。
7-2 创建类

class Dog(object):#class定义一个类，obiect代表Dog默认继承的类，当然也可以去定义这个object。
	typee="宠物"#类变量
	"""docstring for ClassName"""
	def __init__(self,name,age,color):#初始化方法 self表示当前对象__init__是函数名
		#super(ClassName, self).__init__()
		self.name=name#实例变量或者实例属性
		self.age=age
		self.color=color
	def eat(self):#普通方法
		print(self.name,"狗狗在啃骨头！")
	def run(self,speed):#普通方法 speed为后期加上
		print(self.name,"狗狗在飞快的跑！速度:",speed)
#实例化对象：首先类是一个抽象的概念，本身不能做任何操作，如果要去拿取其中的变量就要实例化对象
#即从这个抽象的狗类里边拿取一个具体的狗，才能拿到具体的变量。
dog=Dog("小黑",3,"白色")#用dog去接收，即对象的名字=类名（参数列表）self这个参数为隐式参数
dog.color="黑色"#对属性进行修改
print(dog.name)#访问属性
dog.eat()#调用类里边所定义的方法
dog.run("3m/s")#从外部传入参数
class Card(object):
	"""docstring for Card"""
	def __init__(self, num,pwd,ban):
		self.num = num
		self.pwd = pwd
		self.__ban = ban#加两个下划线就变成了私有属性，只能在类的内部被访问
	def cun(self):
		print("存款！")
	def getBan(self,numm,pwdd):
		if numm==self.num and pwdd==self.pwd
			return self.__ban
		else:
			return "输入错误！"
		#super(Card, self).__init__()
card=Card("1001","123456",1000)#开卡
print(card.getBan())
print(card._Card__ban)
#7-6类的继承和多态
class Animal(object):#Animal类继承object类
	"""docstring for Animal"""
	def __init__(self, color):
		self.color = color
	def eat(self):
		print("动物在吃！")
	def run(self):
		print("动物在跑！")
class Cat(Animal):#Cat类继承Animal类
	def eat(self):
		print("小猫在吃鱼！")
cat=Cat("黄色")
cat.eat()
cat.run()#cat继承父类即Animal的属性

class Dog(Animal):
	"""docstring for Dog"""
	def __init__(self, name,age,color):
		super(Dog, self).__init__(color)#调用父类(super)的初始化方法 本质上是在子类的方法上加上父类的一种方法。
		self.name = name
		self.age = age
	def eat(self):#eat方法跟父类重名了，但是优先级同样在子类
		print("狗狗在啃骨头！")
dog=Dog()#优先级在Dog类而不是Animal类
总结：初始化方法和普通方法优先级都在子类！儿子的独立意见听儿子的，儿子没有主见听爹的。
类的三种特性：封装 继承 多态
在python里边，多态不是一个很重要的内容。因为python里面没有一个真正意义上的多态思维。
只是在形式上去实现了多态的功能。什么是多态？一个类或者对象拥有多种形态。
def feed(obj):
	obj.eat()#obj.eat()的时候暂时还不知道要调用谁的eat方法，
an=Animal("黄")
cat=Cat("橘色")
dog=Dog("小黑",10,"黑色")
feed()#这个时候feed()里面传入谁就用谁的方法。通过上面建立的一个函数可以起到以点带面的作用。

案例：股票提醒系统

import tushare
import time
def getrealtimedata(share):#获取股票数据
	dataNow=tushare.get_realtime_quotes(share.code)
	share.name=dataNow.loc[0][0]
	share.price=float(dataNow.loc[0][3])
	share.high=dataNow.loc[0][4]
	share.low=dataNow.loc[0][5]
	share.volumn=dataNow.loc[0][8]
	share.amount=dataNow.loc[0][9]
	share.openToday=dataNow.loc[0][1]
	share.pre_close=dataNow.loc[0][2]
	share.timee=dataNow.loc[0][30]
	#print(dataNow)
	share.describe="股票名:"+share.name,"当前价格："+str(share.price)#"最高价：",high,"最低价：",low,"成交量：",volumn,"成交额：",amount,"开盘价：",openToday,"收盘价：",pre_close,"时间：",timee,)
	return share
#股票类
class Share():
	def __init__(self,code):
		self.name=""
		self.price=""
		self.high=""
		self.low=""
		self.volumn=""
		self.amount=""
		self.openToday=""
		self.pre_close=""
		self.timee=""
		self.describe=""
		self.code=code
def main(code,buy,sale):
	share=Share(code)
	sss=getrealtimedata(share)
	print(sss.describe)
	if sss.price<=buy:
		print("达到买点!")
	elif sss.price>=sale:
		print("达到卖点!")
	else:
		print("耐心等待!")
while 1==1:
	main("002747",9,12)
	time.sleep(5)
	break






'''from urllib import request
url="https://https://www.baidu.com/"
data=request.urlopen(url).read()
print(data.decode())
import pymysql
#打开数据库连接需要：主机地址 端口号3306 用户名 密码 数据库名
db=pymysql.Connect(host="localhost",port=3306,user="YJ",passwd="Charlene0211",db="stu",charset="utf8")
#创建一个游标对象cursor()
cursor=db.cursor()
print(db)
#第十三章 进阶补充

#13-1 日期和时间类型
import datetime
#获取当前日期
now=datetime.datetime.now()
print(now)
#获取一个指定的日期
d=datetime.datetime(2019,10,1,12,23,40)
print(d)
#日期转字符串
now=datetime.datetime.now()
d=now.strftime("%Y-%m-%d %H:%M:%S")
print(d)
#字符串转日期
s="2020-8-15 2:30:20"
d=datetime.datetime.strptime(s,"%Y-%m-%d %H:%M:%S")
print(d)
#13-2
#json
#简单来讲，json就是js中的对象
#{key:value,key:value,......}
#本质上讲，json就是有特定结构的字符串'''
# import json
# j='{"city":"北京","name":"熊猫"}'
# p=json.loads(j)
# print(type(p))
python转json:json.dumps
json转python:json.loads

# a='我爱北京天安门'
# b=a.encode()
# c=b.decode()
# print(c)
# import datetime
# a=datetime.datetime.now()
# print(a)
