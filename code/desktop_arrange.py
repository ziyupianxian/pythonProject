# -*-coding:utf-8-*-
import os
import shutil
desktop=r"/home/dongdi/桌面"
files=os.listdir(desktop)
file_need_process=[file for file in files
                   if not os.path.isdir(os.path.join(desktop,file))
                    and not file.endswith(".lnk")
                    and  not file.endswith(".ini")]
types=set()
for file in file_need_process:
    ext=file[file.rfind(".")+1:]
    types.add(ext)
for type in types:
    os.mkdir(os.path.join(desktop,type))

for file in file_need_process:
    ext=file[file.rfind(".")+1:]
    src=os.path.join(desktop,file)
    dest=os.path.join(desktop,os.path.join(ext,file))
    print("移动文件：{}->{}".format(src,dest))
    shutil.move(src,dest)
