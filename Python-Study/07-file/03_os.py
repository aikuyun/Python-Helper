
import os
import shutil

# 文件重命名
def rename(oldname, newname):
    os.rename(oldname, newname)


# 文件重命名super
def renames(oldname, newname):
    os.renames(oldname, newname)


# 文件删除
def delete(path):
    os.remove(path)


# 创建文件夹
def mkdir(path):
    os.mkdir(path)
    # 删除文件夹
    # os.rmdir(path)

# 文件的拷贝
def copy(src, dest):
    # 复制文件
    shutil.copyfile(src, dest)
    # 复制文件到文件或者目录
    # shutil.copy(src, dest)

# 文件夹移动或者删除
def move(src, dst):
    shutil.move(src, dst)

def rmtree(path):
    shutil.rmtree(path)

if __name__ == '__main__':
    # rename("test02_1.txt", "test01.txt")
    # 除了改名还可以移动文件夹,如果文件夹不存在自动帮我们创建
    # renames("test01.txt", "test100/test01.txt")
    # delete("test100/test01.txt")
    # mkdir("test_02")
    # copy("test02_2.txt", "test02_1.txt")
    # 除了改名还可以移动文件夹,如果文件夹不存在则报错
    # move("test02_2.txt", "test_02/test01.txt")
    # input = raw_input("请输入数据：")
    # print "有人输入了：",input
    rmtree("test_02")