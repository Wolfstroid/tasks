# 第零周学习总结
## 一.搭建windows&ubuntu双系统
这周在windows10的基础上安装了ubuntu18.04系统  
可以说过程比较曲折  
最先的时候对照教程安装ubuntu有一点看错了,导致E盘数据丢失，有点惨痛  
后来装好主要出现了两个问题  

1.无法连接wifi适配器  
2.无法正常关机  

问题一通过开机输入`sudo modprobe -r ideapad_laptop`解决  
问题二有点麻烦，有一次导致磁盘数据损坏，重装了一次,修改grub解决  
安装了一些 ubuntu 需要的软件，掌握一部分linux指令

## 二.学习git
主要是学习廖雪峰的git教程  
学会了git仓库的 add commit checkout log push branch 等操作
注册了github，照着教程建了两个库，配置了SSH，顺便申请了git的学生包  

## 三.学习python
在ubuntu上配置了python的开发环境，用的是VScode  
一开始总是提示没有 pip installer，但系统已经安装了pip，搜索得知那是python的pip，还得安装python3-pip
学习廖雪峰的教程  
写代码还是踩了些坑  
list的传参问题,比如 
```python
def flush(arr): #没用
    arr = []
def real_flush(arr): #有用
    while len(arr):
        arr.pop()
```
## 四.学习markdown语法
见本篇