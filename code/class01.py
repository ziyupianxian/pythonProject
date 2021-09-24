#https://gist.github.com/ziyupianxian/
## 2021.9.19
# s=input('->')
# print(s)
# import math
# print(math.floor(32.9))
# print(int(32.9))
# print(0b0100)
# from math import pi
# print('%f'%pi)
# print('%20f'%pi)
# print('%-20f'%pi)
# print('文')
# print(ord('文'))
# print(chr(25991))
# print(hex(ord('文')))
# temp=30
# print("温度是"+str(temp)+"度")
# print("温度是"+repr(temp)+"度")

# print('123'.__repr__())
# print('123'.__str__())
#
# import datetime
# # today=datetime.date.today()
# # print(str(today))
# # print(repr(today))
# datetime.date(2021,9,19)
#
# datetime.date(2021,9,19)
# numbers=[1,2,3,4,5,6]
# print(numbers)
# print(1,2,3,4)
# list=['adscg','SRGRG','igr','Brggst']
# print(list.sort())
# print(list.sort(key=str.lower))
# print(list.sort(key=str.lower))
# b=(1,2,3,4)
# print(b)
# aDict={'host':'earth'}
# aDict['port']=80
# print(aDict)
# print(aDict.keys())
# print(aDict.values())
# print(aDict['host'])
# for key in aDict:
#     print(key,aDict[key])
# aDict.clear()
# print(aDict.keys())
# x={'username':'admin','machines':['foo','bar','baz']}
# y=x.copy()
#
# y['machines'].remove('foo')
# print(y)
# print(x)
# print(2**4)
# print(17/4)
# print(17//4)
# a=1
# b=1
# c=a is not b
# print(c)

# lambda_fun =lambda  x,y,z:x*y*z
# print(type(lambda_fun))
# print(lambda_fun(2,3,4))
# ll=[1,2,3,4]
# def filter_fun(i):
#     return i if i>3 else None#定义filter_fun函数
# for i in ll:
#     print(filter_fun(i))
# print("Next!")
# print(list(filter(filter_fun,ll)))#把自定义过滤函数和处理对象作为参数给过滤函数
# ll2=[i for i in ll if i>3]#第三种过滤方法
# print(ll2)
#
# list3=[1,2,3,4]
# def map_fun(i):
#     return "{}.txt".format(i)
# result=map(map_fun,list3)
# print(list(result))

# def fun(x,y):
#     return x*y,x+y,x/y
# m,a,s=fun(1,2)
# print(m,a,s)