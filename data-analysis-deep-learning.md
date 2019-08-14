# 匿名函数
    用lambda关键字能创建小型匿名函数。这种函数得名于省略了用def声明函数的标准步骤。

    lambda [arg1, [,arg2,.....argn]] : expression

```python
    sum = lambda arg1, arg2 : arg1 + arg2

    def  test(a,b):
        return a+b

    print(test(22, 33))

    sum = lambda x,y:x+y
    print(sum(22, 33))

    def  test(a, b, func):
            result = func(a, b)
            return result

    print(test(22, 33, lambda x,y:x*y))

    stus = [{"name":"zs", "age": 22}, {"name":"laowang ", "age":33},{"name":"asdasdasdas", "age":13}]
    stus.sort(key=lambda x:x["name"])
    print(stus)
 ```

# 初始化方法___init__
```python
    class Person:
        # __new__()构造对象方法->已经得到了一个对象->__init__(self)
        def __init__(self, name, age, height):
            """初始化对象方法,不是构造对象方法"""
            self.name = name
            self.age = age
            self.height = height

        def introduce(self):
            print("姓名:%s,年龄为:%s" % (self.name, self.age))


    if __name__ == '__main__':
        p1 = Person("aa", 18, 1.71)
        p1.introduce()
```

# 类的魔术方法
    __new__ 构造方法 该方法必须返回当前类的对象
    __init__ 初始化方法
    __str__ toString()
    __del__ 销毁方法
    __call__ 将一个类当做方法调用时会调用该类的__call__方法

    执行流程 __new__ > __init__ >__del__

    总结
        当有1个变量保存了对象的引用时,此对象的引用计数就会加1 a = User() b = a
        当使用del删除变量指向的对象时,如果对象的引用计数不是1比如3,那么此时只会让这个引用计数减1,变成2
        当再次调用del时,变为1,如果再调用1次del,此时会真的把对象进行删除

# 方法和属性前面修饰符
    方法和属性前面
        _ 表示 private 不能被继承
        不带_这个的表示 公共属性 可以被继承

    property用法
        为私有属性添加getter和setter方法
        使用property升级getter和setter方法
            money = property(getMoney, setMoney)
        使用property取代getter和setter方法
            @property
            @money.setter
```python
    class Test(object):
        def __init__(self):
            self.__num = 100

        @property
        def num(self):
            return self.__num

        @num.setter
        def num(self, num):
            if num < 100:
                self.__num = num


    if __name__ == '__main__':
        t = Test()
        t.num = 20
        print(t.num)
```

# 属于类的属性和方法
    多个对象共用这个属性,在内存中只有一份,相当于java中的静态属性
    相当于java中 public static
    对象是不能修改和删除类属性,只有类才能修改和删除类属性,
    总之类的属性归类来管理,对象的属性归对象来管理,两者没有关系

    类的方法一定要加在方法的上面加上一个修饰器@classmethod(java注解),类方法的参数cls,代表当前的类

    @staticmethod 静态方法属于类,没有默认传递的参数,可以通过类对象来调用,也可以通过类名来调用
```python
class User(object):
    name = "zs"  # 公共属性
    __password = "123456"  # 私有属性

    def __new__(cls, sex, username):  # 该方法必须返回当前类的对象
        print("User类对象开始构建")
        return object.__new__(cls)

    def __init__(self, sex, username):
        self.sex = sex
        self.username = username

    def to_string(self):
        print("姓名:%s,密码:%s,性别:%s,名字:%s" % (self.username, User.__password, self.sex, User.name))

    @classmethod # 类的方法一定要加在方法的上面加上一个修饰器(java注解),类方法的参数cls,代表当前的类
    def test(cls):
        cls.name = 'ww'
        print("---test---")

    @staticmethod # 静态方法属于类,没有默认传递的参数,可以通过类对象来调用,也可以通过类名来调用
    def test2():
        User.name = 'ls'
        print("---静态方法---")


    if __name__ == '__main__':
        user1 = User("男", "goldbin")
        user1.to_string()
        user2 = User("女", "kevin")
        user2.to_string()
        user1.test()
        User.test()
        User.test2()
        print(User.name)
```

# 面向对象属性和方法总结

### 属性
| 属性叫法 | 变量叫法    |  描述   |
| ----------------- | --------| :-----------------------: |
| 类属性(私有和公有)  | 类变量   | 所属对象共享同一份类属性    |
| 实例化(私有和公有)  | 成员变量  | 每个不同对象,有不一样值的实例属性   |

### 方法
| 方法的类别 | 语法 | 描述 |
| ----------- | ----------- | ----------- |
| 类方法       |   @classmethod       |   第一个参数是cls,默认传递   |
| 静态方法     |   @staticmethod      |       没有默认传递的参数      |
| 对象方法     |   del 方法名          |   第一个参数是self,默认传递   |

### 为对象动态添加属性
```python
    class Person(object):
        def __init__(self,name,age):
            self.name = name
            self.age = age


    if __name__ == '__main__':
        p = Person("xiaoming", 20)
        p.sex = 'male'
        print(p.sex)
        dir(p)
        p2 = Person("xiaohong",19)
        p2.sex = 'man'
        print(p2.sex)
        Person.addr = 'beijing'
        print(p.addr)
        print(p2.addr)
        #  对象new出来指向了一个引用(指针) 所以给该对象的引用添加一个属性,这个属性只属于这个对象的引用
        #  给类加属性那么每个new出来的对象都有这个属性
```

### 为对象动态添加实例方法
```python
    import types

    class Person(object):
        def __init__(self, name, age):
            self.name = name
            self.age = age

        def eat(self):
            print("eat method")

    def showInfo(self):
        print(self.name)
        print(self.age)

    if __name__ == '__main__':
        p = Person("xiaoming", 20)
        p2 = Person("xiaohong", 18)
        p.showInfo = types.MethodType(showInfo, p)
        p.showInfo()
        # p2.showInfo()  # AttributeError: 'Person' object has no attribute 'showInfo'
        p2.showInfo = types.MethodType(showInfo, p2)
        p2.showInfo()
```
### 为类添加静态方法和类方法
```python
    import types

    class Person(object):
        def __init__(self, name, age):
            self.name = name
            self.age = age

        def eat(self):
            print("eat method")

    @classmethod
    def fun1(cls):
        print("classMethod")

    @staticmethod
    def fun2(a, b):
        return a + b

    if __name__ == '__main__':
        p = Person("xiaoming", 20)
        p2 = Person("xiaohong", 18)
        Person.fun1 = fun1
        p.fun1()
        p2.fun1()
        Person.fun2 = fun2
        print(p.fun2(2, 3))
        print(p2.fun2(2, 3))
```

### 限制类的属性的添加
    要注意, __slots__定义的属性仅对当前类实例起作用,对继承的子类是不起作用的
```python
    class Student(object):
        __slots__ = ("name", "age")

    if __name__ == '__main__':
        student = Student()
        student.name = "john"
        student.age = 20
        print(student.name)
        print(student.age)
        # student.sex = "male"  # AttributeError: 'Student' object has no attribute 'sex'
```

# 多继承
```python
    class A:
        def test(self):
            print("A-----test()")


    class B:
        def test(self):
            print("B-----test()")


    class C(B, A): # 执行的顺序和继承的顺序有关系
        def test(self):
            print("C-----test()")


    if __name__ == '__main__':
        c = C()
        print(C.__mro__) # 打印执行的顺序
        c.test()
```

# 单例
```python
    class User(object):
        __instance = None

        def __init__(self, name):
            self.name = name

        def __new__(cls, name):  # __new__的参数和__init__的参数数量一样
            if not cls.__instance:  # 保证object.__new__(cls)方法只会调用一次
                cls.__instance = object.__new__(cls)
            return cls.__instance


    if __name__ == '__main__':
        u1 = User("zs")
        u2 = User("ls")
        u3 = object.__new__(User)
        print(u1 == u3)
        print(u3)
        print(u1 == u2)
        print("u1对象的内存地址: %s,u2对象的内存地址:%s" % (id(u1), id(u2)))
        print(u1.name)
```

# 异常
    try:是异常捕获开始代码,try放在特别关系的那段代码前面
        pass
    except 异常类型 as ex: 捕获某种类型的异常
    except ... 多个except.按照顺序依次对比类型
    else: 没有异常时执行
    finally: 不管有没有异常都会执行

### 捕捉异常
```python
    a = "123"
    f = None
    try:
        f = open("text2.txt")
        f.write("hello\n")
        f.write("world %d" % a)
    except FileNotFoundError as ex:
        print(ex)
    except Exception as ex:
        print(ex)
    else:  # 没有异常情况会自动执行的代码
        print("else")
    finally:  # 最终要执行的代码,不管前面是否出现exception
        print("finally")
        if f:
            f.close()
```

### 自定义异常
```python
    class PasswordException(Exception):
        def __init__(self, password, min_lenth):
            self.password = password
            self.min_length = min_lenth

        def __str__(self):
            return "%s的密码错误,密码的最小长度为%s" % (self.password, self.min_length)


    def reg(username, password):
        if len(password) < 6:
            raise PasswordException(password, 6)  # 抛出你指定的异常
        else:
            print("用户名为: %s,密码为: %s" % (username, password))


    if __name__ == '__main__':
        try:
            reg("zs", "124")
        except Exception as ex:
            print(ex)
        except PasswordException as ex:
            print(ex)
```

# 补充内容

### 1.给程序传参数
```python
    import sys
    print(sys.argv) # ['python0001.py', '123', '456', 'asaa']
```

### 2.列表推导式
```python
    # 1.所谓的列表推导式,就是指的轻量级循环创建列表
    b = [1 for i in range(1, 10)]
    print(b)  # [1, 1, 1, 1, 1, 1, 1, 1, 1]
    a = [i for i in range(1, 10)]
    print(a)  # [1, 2, 3, 4, 5, 6, 7, 8, 9]
    c = [i**2 for i in range(1, 10)]
    print(c)  # [1, 4, 9, 16, 25, 36, 49, 64, 81]
    # 2.在循环的过程中使用if来确定列表中元素的条件
    e = [i for i in range(1, 30) if i % 2 == 0]
    print(e)  # [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28]
    # 3.2个for循环
    d = [x for x in range(1, 3) for y in range(0, 2)]
    print(d)  # [1, 1, 2, 2]
    # 4.3个for循环
    f = [(x, y) for x in range(1, 5) for y in range(0, 4) for z in range(6, 8)]
    print(f)
```
### 3 set:集合
| 类型 | 语法 | 描述 |
| ----------- | ----------- | ----------- |
| 列表(list)  | a=[]          | 先后顺序,有下标[index]可以重复,可变类型           |
| 元祖(tuple) | a=()          | 先后顺序,有下标[index]可以重复,不可变类型,只能查   |
| 字典(dict)  | a={key:value} | 没有先后顺序,没有有下标,key不可以重复,value可变类型 |
| 集合(set)   | a={}          | 没有先后顺序,没有下标,不可以重复,可变类型          |

    使用set类型可以快速的完成对类型list中的元素去重复的功能

```python
    a = [1, 3, 2, 1, 1, 1, 1]
    print(a)  # [1, 3, 2, 1, 1, 1, 1]
    b = set(a)
    print(b)  # {1, 2, 3}
    c = tuple(b)
    print(c)  # (1, 2, 3)
    d = list(c)
    print(d)  # [1, 2, 3]
```

### 导入模块的路径设置
    查看模块搜索路径
        import sys
        sys.path
    添加搜索路径
        sys.path.append('/home/sxt/xxx')
        sys.path.insert(0, '/home/sxt/xxx')
    重新导入模块
        from imp import *
        reload(模块名)
    查看安装的模块
        help("modules")

### is和==
    is是比较两个引用是否指向了同一个对象(引用比较)
    ==是比较对象是否相等(值比较)

# 浅拷贝与深拷贝
    浅拷贝是对于一个对象的顶层拷贝,通俗的理解:拷贝了引用,并没有拷贝内容
    深拷贝是对于一个对象所有层次的拷贝(递归)
    import copy
        copy.deepcopy() #深拷贝
        copy.copy() #浅拷贝
    浅拷贝对不可变类型和可变类型的copy不同(例如列表和元祖)
    分片表达式可以赋值一个序列
    字典copy方法可以拷贝一个字典
    有内置函数可以生成拷贝(list)

# 生成器
    在python中,一边循环一边计算的机制,称为生成器: generator
        创建生成器:G = (x*2 for x in range(5))
        可以通过next()函数获得生成器的下一个返回值
        没有更多的元素时,抛出StopIteration
        生成器也可以使用for循环,因为生成器是可迭代对象
    创建生成器的另外一种方法:
        def fib(times): # 斐波拉契数列(Fibonacci)
            n = 0
            a, b = 0, 1
            while n < times:
                yield b # yield(放弃)函数执行到这个地方会交出cpu控制权,停止执行,调用next再继续
                a, b = b, a+b
                n += 1
            return 'done'
        g = fib(5)
        next(g) # 只有next函数调用才会得到值
    其他生成器方法:
        使用__next__()方法
        使用send()方法
            next()等价于send(None)
            def gen():
                i = 0
                while i < 5:
                    temp = yield i
                    print(temp)
                    i+=1
        生成器的特点:
            1.节约内存
            2.迭代到下一次的调用时,所使用的参数都是第一次所保留下的
    迭代是访问集合的一种方式.迭代器是一个可以遍历的位置的对象.迭代器只能往前不会后退
    可迭代对象(Iterable)
        集合数据类型, 如 list, tuple, dict, set , str 等
        生成器和带yield的generator function
    如何判断对象可迭代?
        from collections import Iterable
        isinstance([], Iterable)
    迭代器(Iterator):可以被next()
    迭代器(Iterator):可以被next()函数调用并不断返回下一个值的对象为迭代器
        from collections import Iterator
        isinstance((x for x in range(10), Iterator)
        iter()函数:将可迭代的对象转成迭代器

# 闭包和装饰器
    函数内部返回或者调用一个函数
    装饰器
        使用闭包,给一个函数作为参数,返回一个新的增强的函数
        使用@w1注解放到需要增强的函数
        装饰器的使用场景
            1.引入日志
            2.函数执行时间统计
            3.执行函数前预备处理
            4.执行函数后清理功能
            5.权限校验等场景
            6.缓存
```python
    def doca(func):
        def wrapper():
            # 函数之前
            print(func.__name__)
            func()
            # 函数之后
        return wrapper

    @doca # 可以有多个装饰 可以对有参函数进行装饰 可以对不定长参数函数进行装饰
    def fun():
        print("a")
```

# 类装饰器
    装饰器函数其实是这样的一个接口约束,它必须接受一个callable对象作为参数,然后返回一个callable对象
    一般callable对象都是函数,但也有例外.只要某个对象重写了___call__()方法,那么这个对象就是callable的
```python
    class Test(object):
        def __call__(self, *args, **kwargs):
            print("call me")

    if __name__ == '__main__':
        t = Test()
        t()


    class Test(object):
        def __init__(self, func):
            print("func:%s" % func.__name__)
            self.func = func

        def __call__(self, *args, **kwargs):
            print("附加功能...")
            self.func()


    @Test  # 生成一个Test对象,所以会调用__init__方法,并且把下面装饰的函数作为参数传进去
    def fun():
        print("fun")


    if __name__ == '__main__':
        fun()  # 调用Test的一个对象的__call__方法
        # func:fun 初始化方法调用
        # 附加功能...
        # fun
```

# 对象池
    python为了优化速度,使用了小整数[-5,257)对象池,避免为整数频繁申请和销毁内存空间
    同理,单个字符也提供对象池,常驻内存
    每一个大整数,均创建一个新的对象
    对于字符串,单个单词,不可修改,默认开启intern机制,采用引用计数机制共用对象,引用计数为0则销毁

# 垃圾回收GC
    Garbage collection(垃圾回收)
        为新生成的对象分配内存
        识别哪些垃圾对象
        从垃圾对象那里回收内存
    python采用的是引用计数机制为主,标记-清除和分代收集两种机制为辅的策略
    python里每一个东西都是对象,他们的核心就是一个结构体：PyObject
```c
    typedef struct object{
        int ob_refcnt;
        struct_typeobject *ob_type;
    }PyObject
    #define Py_INCREF(op)((op)->ob_refcnt++) //增加计数
    #define Py_DECREF(op)
        if(--(op)->ob_refcnt!=0)
            ;
        else
            __Py_Dealloc((PyObject *)(op))
```
    引用计数机制的优点:
        简单
        实时性: 一旦没有了引用,内存就直接释放了.不用像其他机制等到特定时机.
            实时性还带来一个好处:处理回收内存的时间分摊到了平时
    引用计数机制的缺点
        维护引用计数消耗资源
        循环引用
    导致引用计数+1的情况
        对象被创建                      例如 a = 23
        对象被引用                      例如 b = a
        对象被作为参数,传入到一个函数中    例如 func(a)
        对象作为一个元素,存储在容器中      例如 list1 = [a,a]
    导致引用计数-1的情况
        对象的别名被显示销毁              例如 del a
        对象的别名被赋予新的对象           例如 a = 24
        一个对象离开它的作用域,例如f函数执行完毕时,func函数中的局部变量(全局变量不会)
        对象所在的容器被销毁,或从容器中删除对象
    查看一个对象的引用的计数
        import sys
        a = "hello world"
        sys.getrefcount(a)
    有三种情况会触发垃圾回收:
        1.调用gc.collect()
        2.当gc模块的计数器达到阀值的时候
        3.程序退出的时候
    GC方法
        垃圾回收后的对象放在gc.garbage列表里面
        gc.get_threshold()获取的gc模块中自动执行垃圾回收的频率
        gc.set_threshold(threshold(),threshold1[,threshold2])设置自动执行垃圾回收的频率
        gc.get_count()获取当前自动执行垃圾回收的计数器,返回一个长度为3的列表
        gc.collect([generation])显示进行垃圾回收,可以输入参数
            参数
                0 代表只检查第一代的对象
                1 代表检查一二代的对象
                2 代表检查一二三代的对象
                不传参数 执行一个full collection 也就是等于传2
            返回值
                返回不可达(unreachable objects) 对象的数目
        gc模块唯一处理不了的时循环引用的类都是___del__方法,所以项目中要避免定义___del__方法

# 内建属性
| 常用专有属性 | 说明 | 触发方式 |
| ----------- | ----------- | ----------- |
| __init__           | 构造初始化函数          | 创建实例后赋值时使用在___new__后 |
| __new__            | 生成实例所需属性         | 创建实例时   |
| __class__          | 实例所在的类            | 实例 __class__ |
| __str__            | 实例字符串表示,可读性    | print(类的实例)如没实现,使用repr结果 |
| __repr__           | 实例字符串表示,准确性    | 类实例回车或者print(repr(类实例)) |
| __del__            | 析构                   | del删除实例                    |
| __dict__           | 实例自定义属性           | vars(实例___dict__)            |
| __doc__            | 类文档,子类不继承        | help(类或实例)           |
| __getattribute__   | 属性访问拦截器           | 访问实例属性           |
| __basses__         | 类的所有父类             | 类名.__basses__           |

# 安装库
    sudo pip3 install numpy -i https://mirrors.aliyun.com/pypi/simple/

# 科学计算库-Numpy