# 导入内置的模块，练习一下

import sys

# 导入sys模块后，我们就有了变量sys指向该模块，利用sys这个变量，就可以访问sys模块的所有功能

# sys模块有一个argv变量，用list存储了命令行的所有参数。argv至少有一个元素，因为第一个参数永远是该.py文件的名称

print(sys.argv)

# 可以在命令行运行 python2 module.py 会打印包含该文件的名字的list

# 也可以运行 python3 module.py tsl 会打印有两个元素的list
