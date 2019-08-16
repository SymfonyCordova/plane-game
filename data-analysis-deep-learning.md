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

# 内建属性和内建函数
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
| __bases__         | 类的所有父类             | 类名.__bases__           |

    dir(__builtins__)
    range(start,stop[,step])计数从start开始,默认是从0开始,到stop结束,但不包括stop,每次跳跃的间距,默认1
    map(function,sequence[,sequence,...])根据提供的函数对指定序列做映射
    filter(function or Nore, sequence)对指定序列执行过滤操作
    reduce(function, sequence[, initial]) 对参数序列中元素进行累积
        在python3里,reduce()函数已经被从全局名字空间移除了,它现在被放置在functools模块里
        *args func(1,2,3,4) 传元祖
        **args func(a='python', b='json') 传的是字典

# 调试器
    执行时调试
        python -m pdb some.py
    交互式调试
        import pdb
        pdb.run('testfun(args)')
    程序里埋点
        import pdb
        pdb.set_trace()

| 命令 | 简写命令 | 作用 |
| ----------- | ----------- | ----------- |
|  break       |     b     |    设置断点          |
|  continue    |     c     |  继续执行程序         |
|  list        |     l     |  查看当前执行的代码段  |
|  step        |     s     |  进入函数            |
|  return      |     r     |  执行代码直到从当前函数返回 |
|  quit        |     q     |  中止并退出 |
|  next        |     n     |  执行下一行 |
|  print       |     p     |  打印变量的值 |
|  help        |     h     |  帮助 |
|  args        |     a     |  查看传入参数 |
|  回车         | 重复上一条命令 |           |
|  break       |     b     |  显示所有断点  |
|  break lineno |     b lineno     |  在指定行设置断点  |
|  break file lineno |     b file lineno     |  在指定文件行设置断点  |
|  clear num  |          |  删除指定断点  |
|   bt  |          |  查看函数调用栈帧  |

# 多进程和多线程
    fork
    进程之间不能共享全局变量
    多个fork的问题
```python
    import os
    import time

    num = 100  # 进程之间不能共享全局变量
    pid = os.fork()
    if pid < 0:
        print("fork()调用失败")
    elif pid == 0:
        time.sleep(2)
        num += 1
        print("子进程,pid:%d, 父进程id:%d,num:%d" % (os.getpid(), os.getppid(), num))
    else:
        time.sleep(3)
        print("父进程,pid:%d子进程id:%d,num:%d" % (os.getpid(), pid, num))
```
    由于Python是跨平台的,自然也应该提供一个跨平台的多进程支持
    multiprocessing模块就是跨平台版本的多进程模块
    multiprocessing模块提供了一个Process类来代表一个进程对象
    创建子进程时,只需要传入一个执行函数和函数的参数,创建一个Process实例,用start()方法启动,这样创建进程比fork()还要简单
    Process([group[,target[,name[,args[,kwargs]]]]])
        target:表示这个进程实例所调用的对象
        args:表示调用对象的位置参数元组
        kwargs:表示调用对象的关键字参数字典
        name: 为当前进程实例的别名
        group: 大多数情况下用不到
    join()方法可以等待子进程结束后再继续往下运行,通常用于进程的同步
    Process类常用方法:
        is_alive(): 判断进程实例是否还在执行
        join([timeout]): 是否等待进程实例执行结束,或等待多少秒
        start(): 启动进程实例(创建子进程)
        run(): 如果没有给定target参数,对这个对象调用start()方法时,就执行对象中的run()方法
        terminate(): 不管任务是否完成,立即终止
    Process类常用属性:
        name: 当前进程实例别名,默认为Process-N,N为从1开始递增的整数
        pid: 当前进程实例的PID值
    创建新的进程还能够使用类的方式,可以自定义一个类,继承Process类,每次实例化这个类的时候,就等同于实例化一个进程对象
        需要重写run方法
```python
    code1
        from multiprocessing import Process
        import os
        import time

        def fun(name):
            time.sleep(3)
            print("子进程id:%d,父进程id:%d,name:%s" % (os.getpid(), os.getppid(),name))

        print("父进程")
        #  创建子进程
        p = Process(target=fun, args=("test",))
        #  开始执行子进程
        p.start()
        #  父进程等待子进程结束
        p.join()
        print("子进程已经结束")
    code2
        from multiprocessing import Process
        import time

        def fun(name, num, **kwargs):
            time.sleep(2)
            print("子进程: name:%s,num:%d" % (name, num))
            for k, v in kwargs.items():
                print("%s:%s" % (k, v))

        print("父进程")
        p = Process(target=fun, name="p1", args=("test", 10,), kwargs={'a': 10, 'b': 20})
        p.start()
        p.join(1)
        print("子进程的名字:%s,id:%d" % (p.name, p.pid))
        p.terminate()
        print("子进程已结束")
    code3
        from multiprocessing import Process
        import time
        import os

        # 定义自己的进程类
        class CustomProcess(Process):
            def __init__(self, interval):
                super().__init__()
                self.interval = interval

            def run(self) -> None:
                print("子进程")
                startTime = time.time()
                time.sleep(self.interval)
                stopTime = time.time()
                print("子进程id:%d,父进程id:%d,执行了%ds" % (os.getpid(), os.getppid(), stopTime-startTime))

        if __name__ == '__main__':
            print("主进程")
            startTime = time.time()
            p = CustomProcess(2)
            p.start()
            p.join()
            stopTime = time.time()
            print("子进程已结束,花费了%ds" % (stopTime-startTime))
```
    多个进程和进程池
    当需要创建的子进程数量不多时,可以直接利用multiprocessing中的Process动态
        生成多个进程,但如果是上百甚至上千的目标,手动的去创建进程的工作量巨大
        此时就可以用到multiprocessing模块提供的Pool方法
    初始化Pool时,那么指定一个最大进程数,当有新的请求提交到Pool中时,
        如果池还没有满,那么就会创建一个新的进程用来执行该请求;但如果池中
        的进程数已经达到指定的最大值,那么该请求就会等待,直到池中有进程结束,才会创建新的进程执行
    multiprocessing.Pool常用函数解析
        apply_async(func[,args[,kwds]]) 使用非阻塞方式调用func(并执行,堵塞方式必须等待
            上一个进程退出才能执行下一个进程),args为传递给func参数列表,kwds为传递给func的关键字参数列表
        apply(func[,args[,kwds]]) 使用阻塞方式调用func
        close() 关闭Pool,使其不再接受新的任务
        terminate() 不管任务是否完成,立即终止
        join() 主进程阻塞,等待子进程的退出,必须在close或terminate之后使用

```python
    code1
        from multiprocessing import Process
        import time
        import os

        # 定义自己的进程类
        class CustomProcess(Process):
            def __init__(self, interval):
                super().__init__()
                self.interval = interval

            def run(self) -> None:
                print("子进程")
                startTime = time.time()
                time.sleep(self.interval)
                stopTime = time.time()
                print("子进程id:%d,父进程id:%d,执行了%ds" % (os.getpid(), os.getppid(), stopTime-startTime))

        if __name__ == '__main__':
            print("主进程")
            startTime = time.time()
            childs = []
            for x in range(5):
                p = CustomProcess(x+1)
                p.start()
                childs.append(p)
                # p.join()  #这个很关键这个用来进程之前的同步 注释和不注释执行效果实不一样的
            for item in childs:
                item.join()
            stopTime = time.time()
            print("子进程已结束,花费了%ds" % (stopTime-startTime))
    code2
        from multiprocessing import Pool
        import time
        import os

        def worker(msg):
            print("子进程pid:%d" % os.getpid())
            startTime = time.time()
            time.sleep(2)
            stopTime = time.time()
            print("子进程msg:%s,花费的时间%d" % (msg, stopTime - startTime))

        if __name__ == '__main__':
            #  创建进程池,最大进程数3
            pool = Pool(3)
            for x in range(10):
                #  pool.apply_async(worker, (x,))  # 异步请求
                pool.apply(worker, (x,))  # 同步请求
            # 关闭进程池
            pool.close()
            #  父进程等待进程池的结束
            pool.join()
            print("进程池已结束")
```

# 进程间通信
    消息队列,管道
```python
    code1: 进程间使用管道通信
        from multiprocessing import Process, Queue
        import time, random

        def write(queue):
            """
            :type queue: Queue
            """
            for item in "ABC":
                print("正在往消息队列写入%s" % item)
                queue.put(item)
                time.sleep(random.random())

        def reader(queue):
            """
            :type queue: Queue
            """
            while True:
                if not queue.empty():
                    item = queue.get()
                    print("从消息队列读出%s" % item)
                else:
                    break

        if __name__ == '__main__':
            # 创建消息队列
            q = Queue()
            #  创建写入进程
            pw = Process(target=write, args=(q,))
            pw.start()
            pw.join()
            #  创建读进程
            pr = Process(target=reader, args=(q,))
            pr.start()
            pr.join()
            print("所有数据已经读完")

    code2: 进程池使用管道通信
        from multiprocessing import Pool, Manager
        import time, random

        def write(queue):
            """
            :type queue: Queue
            """
            for item in "ABC":
                print("正在往消息队列写入%s" % item)
                queue.put(item)
                time.sleep(random.random())

        def reader(queue):
            """
            :type queue: Queue
            """
            while True:
                if not queue.empty():
                    item = queue.get()
                    print("从消息队列读出%s" % item)
                else:
                    break

        if __name__ == '__main__':
            # 创建消息队列
            q = Manager().Queue()
            # 创建进程池
            pool = Pool(3)
            #  创建写入进程
            pool.apply(write, (q,))
            #  创建读进程
            pool.apply(reader, (q,))
            pool.close()
            pool.join()
            print("所有数据已经读完")
```

# 多线程
    python的thread模块是比较底层的模块
    python的threading模块是对thread做了一些包装的,可以更加方便的被使用
    使用threading模块时,往往会定义一个新的子类class,只要继承threading.Thread就可以了,然后重写run方法

    在一个进程内的所有线程共享全局变量,能够在不适用其他方式的前提下完成多线程之间的数据共享(这点比多进程要好)
    缺点就是,线程是对全局变量随意遂改可能造成多线程之间对全局变量的混乱(即线程非安全)
```python
    code1:一般线程代码
        import threading
        import time

        def fun(num):
            print("线程执行%d" % num)
            time.sleep(2)

        if __name__ == '__main__':
            for i in range(5):
                t = threading.Thread(target=fun, args=(i + 1,))
                t.start()
            print("主线程结束")
    code2: 查看当前线程数量
        import threading
        import time

        def sing():
            for i in range(3):
                print("我正在唱歌....")
                time.sleep(1)

        def dance():
            for i in range(3):
                print("我正在跳舞....")
                time.sleep(2)

        if __name__ == '__main__':
            st = threading.Thread(target=sing)
            dt = threading.Thread(target=dance)
            st.start()
            dt.start()
            while True:
                length = len(threading.enumerate())
                print("当前线程数量%d" % length)
                if length <= 1:
                    break
                time.sleep(0.5)
    code4: 线程的子类化
        import threading
        import time

        class CustomThread(threading.Thread):
            def __init__(self, num, str1):
                super().__init__()
                self.num = num
                self.str1 = str1

            def run(self) -> None:
                for i in range(3):
                    time.sleep(1)
                    msg = "I am %s@%s num:%d str1:%s" % (self.name, str(i), self.num, self.str1)
                    print(msg)

        if __name__ == '__main__':
            for i in range(5):
                t = CustomThread(10, "abc")
                t.start()
```
    线程使用全局变量
        注意:函数的值传递和引用传递的区别
```python
    import threading
    import time

    # 线程共享全局变量
    # 注意这三个全局变量的区别 一般的变量是值传递和其他的引用传递
    globalNum = 100
    listVar = [10, 20, 30]
    var = 10

    def worker1(listVar, var):
        """
        :type var: int
        :type listVar: list
        """
        global globalNum
        for i in range(3):
            globalNum += 1
            listVar.append(44)
            var += 10
            print("in worker1, globalNum=%d, listVar:%s, var:%d" % (globalNum, listVar, var))

    def worker2(listVar, var):
        """
        :type listVar: list
        :type var: int
        """
        global globalNum
        print("in worker2, globalNum=%d, listVar:%s, var:%d" % (globalNum, listVar, var))

    if __name__ == '__main__':
        # 主进程,globalNum=100 listVar:[10, 20, 30], var:10
        print("主进程,globalNum=%d listVar:%s, var:%d" % (globalNum, listVar, var))
        w1 = threading.Thread(target=worker1, args=(listVar, var))
        w1.start()
        time.sleep(1)
        w2 = threading.Thread(target=worker2, args=(listVar, var))
        w2.start()
        print("主进程,globalNum=%d listVar:%s, var:%d" % (globalNum, listVar, var))
        # 主进程,globalNum=103 listVar:[10, 20, 30, 44, 44, 44], var:10
```
    线程安全和线程同步
        当多个线程几乎同时修改某一个共享数据的时候,需要进行同步控制
        线程同步能够保证多个线程安全访问竞争资源,最简单的同步机制是引入互斥锁
        互斥锁保证了每次只有一个线程进行写入操作,从而保证了多线程情况下数据的正确性
        某个线程要更改共享数据时,先将其锁定,此时资源的状态为"锁定",其他线程不能更改
            直到该线程释放资源,将资源的状态变成"非锁定",其他的线程才能再次锁定该资源
        threading模块定义了Lock类,可以方便处理锁定
        创建锁
            mutex = threading.Lock()
        锁定
            mutex.acquire([blocking])
                如果设定blocking为True,则当前线程会阻塞,直到获取到这个锁为止
                    (如果没有指定,那么默认为True)
                如果设定blocking为False,则当前线程不会阻塞
        释放
            mutex.release()

        两把锁分别交叉嵌套容易造成死锁,线程相互等待,永远不能释放

        python的Queue模块中提供了同步的,线程安全的队列类,包括:
            FIFO(先进先出)队列Queue,
            LIFO(后进先出)队列LifoQueue
            优先级队列 PriorityQueue
        这些队列都实现了锁原语(可以理解为原子操作,即要么不做,要么就做完),能够在多线程中直接使用

        ThreadLocal变量
            一个ThreadLocal变量虽然是全局变量,但每个线程都只能读写自己线程独立副本,互不干扰.
                ThreadLocal解决了参数在一个线程中各个函数之间互相传递的问题
            可以理解为全局变量local_shool是一个dict,可以绑定其他变量
            ThreadLocal最常用的地方就是为每个线程绑定一个数据库连接,Http请求,用户身份信息等,
                这样一个线程的所有调用到的处理函数都可以非常方便地访问这些资源

```python
    code1:普通操作
        import threading

        gNum = 0
        # 创建互斥锁
        mutex = threading.Lock()

        def worker():
            global gNum
            for x in range(2000000):
                # 加锁
                lock = mutex.acquire(True)
                if lock:
                    gNum += 1
                    # 解锁
                    mutex.release()

        if __name__ == '__main__':
            threads = []
            for i in range(2):
                t = threading.Thread(target=worker)
                t.start()
                threads.append(t)
            for t in threads:
                t.join()
            print("main thread:gNum=%d" % gNum)
    code2: 类操作
        from threading import Thread, Lock

        class CustomThread(Thread):
            num = 0
            mutex = Lock()

            def run(self) -> None:
                for i in range(1000000):
                    lock = CustomThread.mutex.acquire(True)
                    if lock:
                        CustomThread.num += 1
                        CustomThread.mutex.release()

        if __name__ == '__main__':
            threads = []
            for i in range(2):
                t = CustomThread()
                t.start()
                threads.append(t)
            for t in threads:
                t.join()
            print("main thread:gNum=%d" % CustomThread.num)
    code3: 死锁
        import time
        from threading import Thread, Lock

        class CustomThread(Thread):
            mutexA = Lock()
            mutexB = Lock()

            def run(self) -> None:
                if self.name == 'threadA':
                    CustomThread.runThreadA()
                else:
                    CustomThread.runThreadB()

            @staticmethod
            def runThreadA():
                if CustomThread.mutexA.acquire():
                    print("threadA do something...")
                    time.sleep(2)
                    if CustomThread.mutexB.acquire():
                        print("threadA get mutexB...")
                        CustomThread.mutexB.release()
                    CustomThread.mutexA.release()

            @staticmethod
            def runThreadB():
                if CustomThread.mutexB.acquire():
                    print("threadB do something...")
                    time.sleep(2)
                    if CustomThread.mutexA.acquire():
                        print("threadB get mutexA...")
                        CustomThread.mutexA.release()
                    CustomThread.mutexB.release()

        if __name__ == '__main__':
            threadA = CustomThread(name="threadA")
            threadB = CustomThread()
            threadA.start()
            threadB.start()
    code4: 线程安全的队列类
        import time
        from threading import Thread
        from queue import Queue

        class Producter(Thread):
            def __init__(self, queue):
                """
                :type queue: Queue
                """
                super().__init__()
                self.queue = queue

            def run(self) -> None:
                while True:
                    if self.queue.qsize() < 1000:
                        for x in range(100):
                            msg = "产品" + str(x)
                            print("%s创建了%s" % (self.name, msg))
                            queue.put(msg)
                        time.sleep(1)

        class Consumer(Thread):
            def __init__(self, queue):
                """
                :type queue: Queue
                """
                super().__init__()
                self.queue = queue

            def run(self) -> None:
                while True:
                    if self.queue.qsize() > 100:
                        for x in range(3):
                            msg = self.queue.get()
                            print("%s消费了%s" % (self.name, msg))
                        time.sleep(0.5)


        if __name__ == '__main__':
            queue = Queue()
            for i in range(500):
                msg = "产品" + str(i)
                queue.put(msg)
            for i in range(2):
                t = Producter(queue)
                t.start()
            for i in range(5):
                c = Consumer(queue)
                c.start()
    code5:ThreadLocal变量
        import threading

        #  创建threadLocal变量
        localSchool = threading.local()

        def processStudent():
            name = localSchool.student
            print("hello %s in %s" % (name, threading.current_thread().name))

        def processThread(name):
            localSchool.student = name
            processStudent()

        if __name__ == '__main__':
            t1 = threading.Thread(target=processThread, args=("张三",), name="t1")
            t2 = threading.Thread(target=processThread, args=("老王",), name="t2")
            t1.start()
            t2.start()
```
# 安装库
    sudo pip3 install numpy -i https://mirrors.aliyun.com/pypi/simple/

# 科学计算库-Numpy