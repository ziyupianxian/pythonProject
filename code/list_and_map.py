# -*-coding:utf-8-*-
if __name__=='__main__':
    map={}
    map['name']='张三'
    map[2]='男'
    map['studentNo']=200154524657
    for key,value in map.items():
        print("{}->{}".format(key,value))
    for key in map.keys():
        print("{}->{}".format(key,map.get(key)))