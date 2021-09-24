# -*-coding:utf-8-*-
import os
import shutil
folder=r"/home/dongdi/文档/python_course"
if __name__=='__main__':
    files=os.listdir(folder)#所有文件名字
    index=0
    for file in files:#对于每一个名字
        index+=1
        src=os.path.join(folder,file)#文件夹+文件名
        # if os.path.isdir(src):
        #     continue
        if "python" in file:
            new_file=file.replace("python","Python")#文件名有old_word,就产生一个新的字符串
            dest=os.path.join(folder,new_file)#src更新为文件夹和新文件名
            shutil.move(src,dest)#dest代替src
            print("处理文件：{}".format(file))