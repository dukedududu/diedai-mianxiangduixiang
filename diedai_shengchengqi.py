'''
list=[1,2,3,4]
i=iter(list)#创建迭代器的对象 iter()
print(next(i))#输出迭代器的下一个对象
print(next(i))
for x in i:
    print(x)
'''

   #迭代器&面向对象
'''
class shuzi:
    i=[1,2,3,4,5]
    def f(self):
    #使用 def 关键字来定义一个方法
        return("hello world!")
x=shuzi()
print('类的属性i为：',x.i)
print('类的函数f功能为:',x.f())
'''

'''
class Complex:
    def __init__(self,grade,gores):#定义构造方法
    #类的方法与普通的函数只有一个特别的区别
    #它们必须有一个额外的第一个参数名称, 按照惯例它的名称是 self。
        self.r=grade
        self.o=gores
x=Complex(3,-2)
print(x.r)
print(x.o)
'''

'''
class people:
    #定义基本属性

    #相当于 是定义name是str型   age是int型
    name = ''
    age = 0
    #定义构造方法
    def __init__(self,name,age,weight):
        self.n=name
        self.a=age
        self.w=weight
        #定义私有属性,私有属性在类外部无法直接进行访问
        __weight = 0
    def speak(self):
        print('%s说：我%d岁'%(self.n,self.a))
        #实例化 类
p=people('erfan',18,50)
p.speak()

#单继承
class teacher(people):
    high=0
    def __init__(self,name,age,weight,high):
        people.__init__(self,name,age,weight)#调用父类构造函数
        self.h=high
    def f(self):
        print('%s说：我今年%d岁，我%dcm'%(self.n,self.a,self.h))
t=teacher('李梅老师',42,50,167)
t.f()
'''

#关于__init__()函数

#????????
