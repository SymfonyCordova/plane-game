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
    __new__ 构造方法
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

# 属于类的属性
    多个对象共用这个属性,在内存中只有一份,相当于java中的静态属性
    相当于java中 public static
    对象是不能修改和删除类属性,只有类才能修改和删除类属性,
    总之类的属性归类来管理,对象的属性归对象来管理,两者没有关系
```python
    class User(object):
        name = "zs"  # 类的公共属性
        __password = "123456"  # 类的私有属性

        def __init__(self, sex, username):
            self.sex = sex
            self.username = username

        def to_string(self):
            print("姓名:%s,密码:%s,性别:%s,名字:%s" % (self.username, User.__password, self.sex, User.name))


    if __name__ == '__main__':
        user1 = User("男", "goldbin")
        user1.to_string()
        user2 = User("女", "kevin")
        user2.to_string()
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

# 安装库
    sudo pip3 install numpy -i https://mirrors.aliyun.com/pypi/simple/

# 科学计算库-Numpy