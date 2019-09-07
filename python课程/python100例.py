#!/usr/bin/env python
# coding: utf-8

# In[2]:


'''第一题：
有四个数字：1、2、3、4，能组成多少个互不相同且无重复数字的三位数？各是多少？'''
a=range(1,5)
for i in a:
    for j in a:
        for k in a:
            if i!=j and j!=k and k!=i:
                print(i,j,k)


# In[6]:


'''第二题：利润提成'''
arr=[1000000,600000,400000,200000,100000,0]
rat=[0.01,0.015,0.03,0.05,0.075,0.1]
i=input('净利润：')
r=0
for ii in range(0,6):
    if int(i)>arr[ii]:
        r+=(int(i)-arr[ii])*rat[ii]
print(r)


# In[12]:


'''第三题：i,j都是>=2的偶数
'''
for i in range(2,85):
    if 168%i==0:
        j=168/i
        if i>j and (i+j)%2==0 and (i-j)%2==0:
            m=(i+j)/2
            n=(i-j)/2
            x=n**2-100
            print(x)


# In[5]:


'''第五题：
排序'''
a=[]
for i in range(0,3):
    x=int(input('请输入:\n'))
    a.append(x)
a.sort()
print(a)


# In[17]:


'''第六题：
斐波那契数列'''
def fbo(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fbo(n-1)+fbo(n-2)
    return fbo(n)
a=[]
for i in range(0,10):
    a.append(fbo(i))
print(a)


# In[19]:


'''第七题：
将一个列表的数据复制到另一个列表中'''
a=[1,2,3,4]
b=a[:]
print(b)


# In[46]:


'''输出 9*9 乘法口诀表'''
#矩阵表格
#i,j;i<j
for i in range(1,10):
    print('\t')
    for j in range(1,i+1):
            print('%d×%d=%d'%(j,i,i*j),end=' ')


# In[73]:


'''暂停一秒输出'''
import time
dict1={'a':1,'b':2}
for key,val in dict1.items():
    print (key,val)
time.sleep(1)
print(time.time())
print(time.localtime())
print(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime()))#格式化时间
print(time.strptime('2019-09-04 22:08:48','%Y-%m-%d %H:%M:%S'))#逆操作


# In[1]:


'''判断因子'''
from math import sqrt 
from math import floor
a=int(input('请输入一个100到200以内的数:'))
for i in range(2,a):
    if a%i==0:
        print(i)


# In[23]:


'''判断素数'''
print('------>输出100-200内所有素数')

def divisor(x):
    count=0
    for i in range(2,floor(sqrt(x))):
        if x%i==0:
            count+=1
    if count==0:
        return x
for num in range(100,201):
    if divisor(num)!=None:
        print(divisor(num),end=' ')


# In[25]:


'''第13题：
水仙花数'''
for i in range(100,1000):
    str_i=str(i)
    a=int(str_i[0])
    b=int(str_i[1])
    c=int(str_i[2])
    if a**3+b**3+c**3==i:
        print(i)


# In[10]:


'''第14题：
因式分解'''
from numpy import arange
def reducenum(n):
    print('{}='.format(n),end='')
    if not isinstance(n,int) or n<=0:
        print('请输入一个正确的数字！')
    elif n==1:
        print('{}'.format(n),end='')
    while n!=1:
        for i in arange(2,n+1):
            if n%i==0:
                n=n/i
                if n==1:
                    print('%d'%i,end='')
                else:
                    print('%d*'%i,end='')
    
print(reducenum(160))     
print(reducenum(1020))


# In[30]:


'''第15题：'''
score=int(input('请输入分数:'))
if score>100:
    print('error!')
elif score>=90 and score<=100 :
    grade='A'
elif score<89 and score>=60:
    grade='B'

else:
    grade='C'
print('%d is grade %s'%(score,grade))


# In[38]:


'''如果a，b是数值变量， 则&， |表示位运算， and，or则依据是否非0来决定输出，'''
#bin转二进制
a=25
b=12
c=a&b
d=a|b
print(c)
print(d)
a_bin=bin(a)
b_bin=bin(b)
print(a_bin,b_bin)


# In[45]:


'''第17题：
统计字符串英文，数字，空格，其他符号的个数'''
from string import *
str1=input('please input the string:')
alphas=0
digits=0
space=0
others=0
for i in range(0,len(str1)):
    if str1[i].isalpha():
        alphas+=1
    elif str1[i].isdigit():
        digits+=1
    elif str1[i].isspace():
        space+=1
    else:
        others+=1
print("alphas:%d\ndigits:%d\nspace:%d\nothers:%d"%(alphas,digits,space,others))


# In[50]:


'''第18题:
求和'''
num=int(input('请输入元素个数:'))
a=int(input('请输入一个0-9的数字:'))
temp=0
x=0
for i in range(1,num+1):
    temp+=(i*a)*10**(num-i)
    x+=a*10**(i-1)
    print('{}'.format(x))
print('-----------')
print(temp)


# In[55]:


'''第19题：完数'''
for num in range(2,1001):
    a=[]
    for i in range(1,num):
        if num%i==0:
            a.append(i)
    if sum(a)==num:
        print(num)
        print(a)
        print('-------')


# In[64]:


'''第22题：匹配'''
'''对应关系转为等于关系'''
for i in range(ord('x'),ord('z')+1):
    for j in range(ord('x'),ord('z')+1):
        if i!=j:
            for k in range(ord('x'),ord('z')+1):
                if k!=i and k!=j:
                    if i!=ord('x') and k!=ord('x') and k!=ord('z'):
                        print('order is a---%s\tb---%s\tc---%s'%(chr(i),chr(j),chr(k)))


# In[90]:


'''第23题：画菱形'''
from sys import stdout
for i in range(0,4):
    for j in range(3-i):
        print(' ',end='')
    for k in range(2*i+1):
        print('*',end='')
    print('')
for i in range(0,3):
    for j in range(i+1):
        print(' ',end='')
    for k in range(5-2*i):
        print('*',end='')
    print('')#本来就带一个'\n’,不用加了


# In[92]:


'''第24题：求序列之和'''
a=2
b=1
s=0
arr=[]
for i in range(0,21):
    s+=a/b
    arr.append(a/b)
    t=a
    a=a+b
    b=t#交换之前，而不是之后
print(arr)


# In[94]:


'''格式转化'''
print('%06.2f'%(5/3))#不足的补0
print('%6.2f'%(5/3))#长度为6，不足的补空格


# In[112]:


'''第25题：阶乘'''
def factorial(n):
    s=1
    for i in range(1,n+1):
        s*=i
    return s
print(factorial(20))
sum_arr=0
for j in range(1,21):
    sum_arr+=factorial(j)
print(sum_arr)


# In[115]:


'''阶乘'''
def factorial2(n):
    if n==1:
        return 1
    else:
        return n*factorial(n-1)
factorial(4)


# In[3]:


'''第27题'''
def output(string,length):
    if length>0:
        print(string[length-1])
        return output(string,length-1)
string='asdcz'
output(string,len(string))


# In[16]:


'''第29题'''
#1
def output(string,length):
    if length>0:
        print(string[length-1])
        return output(string,length-1)
str1=input('请输入一个数字：')
length=len(str1)
print('the number of the digit is:%d'%length)
output(str1,length)
#2
num=int(input('please input a number :'))
a=num//10000
b=num//1000%10
c=num//100%10
d=num//10%10
e=num%10
if len(str(num))==5:
    print(e,d,c,b,a)
elif len(str(num))==4:
    print(e,d,c,b)
elif len(str(num))==3:
    print(e,d,c)
elif len(str(num))==2:
    print(d,c)
else:
    print(c)


# In[21]:


'''第30题：
回文数'''
str1=input('请输入一个五位数:')
length=len(str1)
count=0
for i in range(0,length):
    if str1[i]!=str1[length-i-1]:
        count+=1
if count!=0:
    print('%s 不是回文数'%str1)
else:
    print('%s 是回文数'%str1)


# In[25]:


'''第32题'''
a=['one','two','three']
for i in a[::-1]:#此处为一个迭代器
    print(i)
print(a[:-1])


# In[42]:


'''第33题：
按逗号分隔列表'''
list1=[1,2,3,4,5]
a=','.join([str(n) for n in list1])#jion后面必须是一个字符串序列
print(a)
a=[str(n) for n in list1]
print(a)


# In[48]:


'''第34题:'''
#   格式：\033[显示方式;前景色;背景色m
#   说明:
#
#   前景色            背景色            颜色
#   ---------------------------------------
#     30                40              黑色
#     31                41              红色
#     32                42              绿色
#     33                43              黃色
#     34                44              蓝色
#     35                45              紫红色
#     36                46              青蓝色
#     37                47              白色
#
#   显示方式           意义
#   -------------------------
#      0           终端默认设置
#      1             高亮显示
#      4            使用下划线
#      5              闪烁
#      7             反白显示
#      8              不可见
#
#   例子：
#   \033[1;31;40m    <!--1-高亮显示 31-前景色红色  40-背景色黑色-->
#   \033[0m          <!--采用终端默认设置，即取消颜色设置-->]]]
print('\033[4m'+'asd'+'')


# In[96]:


#双层字典结构
STYLE={'fore':#前景色
       {#注意逗号间隔开
           'black':30,
           'red':31,
           'yellow':32,
           'green':33,
           'blue':34,
           'purple':35,
           'cyan':36,
           'white':37
       },
       'back':#背景色
       {
           'black':40,
           'red':41,
           'yellow':42,
           'green':43,
           'blue':44,
           'purple':45,
           'cyan':46,
           'white':47
       },
       'mode':
       {
           'mormal':0,
           'bold':1,
           'underline':4,
           'blink':5,
           'invert':7,
           'hide':8
       },
    'default':
       {
         'end':0
       }
        
       }
'''格式：\033[显示方式;前景色;背景色m'''
def usestyle(string,mode='',fore='',back=''):#要对参数赋默认值
    mode='%s'%STYLE['mode'][mode] if mode in STYLE['mode'] else '' #三目运算，找到对应的颜色字符串
    fore='%s'%STYLE['fore'][fore] if fore in STYLE['fore'] else ''
    back="%s"%STYLE['back'][back] if back in STYLE['back'] else ''#变成字符串
    style=';'.join(s for s in [mode,fore,back] if s)
    style='\033[%sm'%style if style else ''
    end='\033[%sm'%STYLE['default']['end'] if style else '' 
    return style+string+end
def testcolor():
    print('正常显示')
    print('-----------------------------------------')
    print(usestyle('高亮',mode='bold'),end=' ')
    print(usestyle('下划线',mode='underline'),end=' ')
    print(usestyle('闪烁',mode='blink'),end=' ')
    print(usestyle('反白',mode='invert'),end=' ')
    print(usestyle('不可见',mode='hide'))
    print('-----------------------------------------')
    print(usestyle('黑色',fore='black'),end=' ')
    print(usestyle('红色',fore='red'),end=' ')
    print(usestyle('绿色',fore='green'),end=' ')
    print(usestyle('黄色',fore='yellow'),end=' ')
    print(usestyle('蓝色',fore='blue'),end=' ')
    print(usestyle('紫色',fore='purple'),end=' ')
    print(usestyle('青色',fore='cyan'),end=' ')
    print(usestyle('白色',fore='white'))
    print('-----------------------------------------')
    print(usestyle('黑色',back='black'),end=' ')
    print(usestyle('红色',back='red'),end=' ')
    print(usestyle('绿色',back='green'),end=' ')
    print(usestyle('黄色',back='yellow'),end=' ')
    print(usestyle('蓝色',back='blue'),end=' ')
    print(usestyle('紫色',back='purple'),end=' ')
    print(usestyle('青色',back='cyan'),end=' ')
    print(usestyle('白色',back='white'),end=' ')
testcolor()


# In[ ]:


'''py3无has_key，可以使用in'''
dict1={'color':'red'}
print('name' in dict1)
print('color' in dict1)


# In[ ]:


mode='invert'
mode='%s'%STYLE['mode'][mode] if mode in STYLE['mode'] else '' 
print(mode)


# In[90]:


print('\033[1;31;40m'+'asd')


# In[114]:


'''第36题：
求指定范围的素数'''
#用户输入数据
lower=int(input('请输入上限：'))
upper=int(input('请输入下限：'))
count=0
for i in range(lower,upper+1):
    if i>1:
        count+=1
        for j in range(2,i):
            if i%j==0:
                break#仅破坏当前循环
        else:
            print(i)


# In[126]:


'''
1.如果模块是被导入，__name__的值为模块名字
2. 如果模块是被直接执行，__name__的值为’__main__’'''
'''通过'''
'''python一切皆对象，所以python的模块也是对象'''
'''一个.py文件，如果是自身在运行，那么他的__name__值就是"__main__"；

如果它是被别的程序导入的（作为一个模块），比如：
import re
那么，他的__name__就不是"__main__"了。

所以，在.py文件中使用这个条件语句，可以使这个条件语句块中的命令只在它独立运行时才执行
'''


# In[125]:



a=[]
for i in range(0,3):
    a.append([])
    for j in range(0,3):
        a[i].append(float(input('num:')))
print(a)
sum=0
for i in range(0,3):
    for j in range(0,3):
        sum+=a[i][j]
print(sum)


# '''原因是这样的，字符串是不可变对象，
# 当用操作符+连接字符串的时候，每执行一次+都会申请一块新的内存，
# 然后复制上一个+操作的结果和本次操作的右操作符到这块内存空间，
# 因此用+连接字符串的时候会涉及好几次内存申请和复制。
# 而join在连接字符串的时候，会先计算需要多大的内存存放结果，
# 然后一次性申请所需内存并将字符串复制过去，这是为什么join的性能优于+的原因'''
# 

# In[ ]:





# In[ ]:




