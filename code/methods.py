# -*-coding:utf-8-*-
#一、遍历
# astr='hello'
# for ch in astr:
#     print(ch)
# for index,ch in enumerate(astr):
#     print(astr[index])
# alist=[10,20,30]
# for item in alist:
#     print(item)
# atuple=('bob','tom','alice')
# for item in atuple:
#     print(item)
# adict={'name':'join','rage':23}
# for key,value in adict.items():
#     print("{}->{}".format(key,value))

#二、字符串方法
# py_str2='a   dd  Hello world!  f b'
# py_str2=py_str2.lstrip()
# print(py_str2)
# py_str2=py_str2.rstrip()
# print(py_str2)
# py_str='adsgvfg'
# print(py_str.capitalize())#首字母大写
# print(py_str.title())#标题格式
# print(py_str.center(50))
# print(py_str.center(50,'#'))
# print(py_str.count('d'))
# print(py_str.endswith('b'))
# print(py_str.startswith('a'))
# print(py_str.islower())
# print(py_str.isupper())
# print('how are you ? '.split())
# print('hello.tar.gz'.split('.'))
# print('.'.join(['hello','tar','gz']))
# print('-'.join(['hello','tar','gz']))
#三、列表方法
# alist=[1,2,3,'bob','alice']
# print(alist[2])
# print(alist[2:4])
# print(alist[2:])
# alist.append('hello')
# print(alist)
# alist.remove('hello')
# print(alist)
# alist.insert(3,4)#前面插入
# print(alist)
# b=alist.pop()
# print(alist)
# print(b)
# print(alist.pop(3))
# print(alist)
# list2=[2,5,2,1]
# print(list2.sort())
# print(list2)
# print(list2.reverse())
# print(list2)
# list3=[3,5,2,1,1,2]
# list2.append(list3)#添加一个元素
# print(list2)
# list2.pop()
# print(list2)
# # list2=list2+list3#与下方同
# list2.extend(list3)
# print(list2)
# print(len(list2))
# 四、tuple方法
# tuple1=(1,2,3)
# tuple2=(4,5,6)
# tuple2=tuple2+tuple1
# print(tuple2*2)
#五、字典方法
# adict=dict()
# print(adict)
# adict=dict(['ab','cg'])
# print(adict)
# bdict=dict([('name','bob'),('age',25)])
# print(bdict)
# edict={}.fromkeys(['zhangsan','lisi','wangwu'],11)
# print(edict)
# del edict['zhangsan']
# print(edict)
# edict.pop('wangwu')
# print(edict)
# edict.clear()
# print(edict)
#六、集合set
# myset=set('aaaaa')#不可重复
# print(len(myset))
# for ch in myset:
#     print(ch)
# aset=set('abc')
# bset=set('cde')
# print(aset.intersection(bset))
# print(aset.union(bset))
# print(aset.difference(bset))
# aset.add('new')
# print(aset)
# aset.update(['aaa','bbb'])#添加
# print(aset)
#七、类型间相互转换
# str='hello'
# print(str)
# ll=list(str)
# print(ll)
# ll2=['1','2','f','g','j']
# str=''.join(ll2)
# print(str)
# tt=tuple('hello')
# print(tt)
# # ll=list(str)
# # print(ll)
# ll=list(tt)
# print(ll)
#八、列表实现斐波那契数列
# fib=[0,1]
# for index in range(2,100):
#     fib.append(fib[index-1]+fib[index-2])
# print(fib)
#九、逐步实现列表解析
# list2=[i for i in range(100) if i%2==0]
# print(list2[0:10])
# list=[10+5]
# print(list)
# list2=[10+5 for i in range(10)]
# print(list2)
# list=[10 + i for i in range(10) if i%2==1]
# print(list)
# list=[10 + i for i in range(1,11)]
# print(list)
# ips=['192.168.1.%s'% i for i in range(1,255)]
# print(ips)
