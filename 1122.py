score=int(input('请输入你的分数：'))
if score>100 or score<0:
    print('输入错误！')
elif score<60:
    print('不及格！')
else:
    print('ok!')

