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

    执行流程 __new__ > __init__ >__del__

    总结
        当有1个变量保存了对象的引用时,此对象的引用计数就会加1 a = User() b = a
        当使用del删除变量指向的对象时,如果对象的引用计数不是1比如3,那么此时只会让这个引用计数减1,变成2
        当再次调用del时,变为1,如果再调用1次del,此时会真的把对象进行删除

# 方法和属性前面修饰符
    方法和属性前面
        __ 表示 private 不能被继承
        不带__这个的表示 公共属性 可以被继承

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
|------|-----|-----|
| 列表(list)  | a=[]          | 先后顺序,有下标[index]可以重复,可变类型           |
| 元祖(tuple) | a=()          | 先后顺序,有下标[index]可以重复,不可变类型,只能查   |
| 字典(dict)  | a={key:value} | 没有先后顺序,没有有下标,key不可以重复,value可变类型 |
| 集合(set)   | a={}          | 没有先后顺序,没有下标,不可以重复,可变类型          |


# 安装库
    sudo pip3 install numpy -i https://mirrors.aliyun.com/pypi/simple/

# 科学计算库-Numpy