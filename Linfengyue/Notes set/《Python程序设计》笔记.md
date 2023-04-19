# 第八周 2023-4-10 Afternoon 

#### Python分析统计作业要求：

>【本周需做】
>本周用word写调查计划书
>可视化要做成 词云图
>
>【问卷星相关】
>用问卷星来调查，在“统计分析”处下载调查数据
>留一个开放性问题，并设置为必填
>
>【上届学生调查数据data.xlsx 存在的问题】
>- 分清楚应设置成单选还是多选，比如性别

#### Notes

!= 是不等于号
以下代码可以把数字转为字符串，即str()函数
```Python
n=int(input())
new_n=str(n)
```


- 在函数内部定义的变量叫**局部变量**
	函数外的叫**全局变量**


- 函数可以提高代码可读性，降低编程复杂度
- 0 是False  1 是 True



# 第九周 2023-4-17 Afternoon

“虽然你们不是专业弄这个（计算机专业）的，但我希望你们能用python去做一些专业的事情。”    ——支高英

```Python
# 调用函数的四种方法

function()

b=function()

print(function())

if function():
```

参数传递有哪几种方式？

format六字口诀：添对宽，分精类

#### 用一个标准的定义函数求最大公约数题，展现在python中使用占位符：
```Python
# 如何在python中使用占位符

# 这是第二道题
# 穷举法求两数的最大公约数，最大公约数不会超过两数中的较小值

def hcf(u,v):

    if u>v:

        m=v

    else:

        m=u

    for i in range(m,0,-1):   # 此处必须是从m遍历到0，因为两个质数的最大公约数是1

        if (u%i==0) and (v%i==0):

            return i  

  

u=int(input("请输入第一个整数："))

v=int(input("请输入第二个整数："))

h=hcf(u,v)                                      # 按照地址传递参数

print("%d和%d的最大公约数为：%d"%(u,v,h))
```

用穷举法写个鸡兔同笼问题


break continue return 都可以使for循环提前结束

index用法：

```Python
lis=[]

target=input()

for i in lis:

    if i=target:

    k=lis.index(target)   #k是target在列表lis中的位置

    return k
```


#### Python中的异常处理
---
比如说逻辑错误

```python
# 除数为0的情况

ls=eval(input())
s=0
for num in ls:
	s=s+num
avg=s/len(ls)

"""
错误之处：ls如果是空列表，那就不能作为被除数
"""
```

开发者要提前进行异常处理，并留一些端口，以便增加后续功能

python有哪些常见异常类型？