# 游戏开放的诀窍
    把一些静止的图片绘制到游戏窗口中
    根据用户的交互或其他情况,移动这些图像,产生动画效果
    根据图像之间是否发生重叠,判断敌机是否被摧残等其他情况

# 开发游戏之前先知道如何建立游戏窗口
    1.游戏的初始化和退出
        pygame.init() 导入并初始化所有pygame模块,使用其他模块之前,必须先调用init方法
        游戏代码
        pygame.quit() 卸载所有pygame模块,在游戏结束之前调用
    2.理解游戏中的坐标系
        原点在左上角(0,0)
        x轴水平方向向右,逐渐增加
        y轴垂直方向向下,逐渐增加
        要描述一个矩形区域有四个要素:左上角的点(x, y)+(width, height)
        pygame专门提供了一个类pygame.Rect用于描述矩形区域 Rect封装了pygame.init()了
    3.创建游戏主窗口
        pygame专门提供了一个模块pygame.display用于创建管理游戏窗口
        pygame.display.set_mode(resolution=(0,0), flags=0, depth=0) 初始化现实窗
            resolution 指定屏幕的宽和高,默认创建的窗口大小和屏幕大小一致
            flags 参数制定屏幕的附加选项,例如是否全屏等等,默认不需要传递参数
            depth 参数表示颜色的位数，默认自动匹配
        pygame.display.update 刷新屏幕的内容,稍后使用
    4.简单的游戏循环
        为了做到游戏程序启动后,不会立即退出,通常会在游戏程序中增加一个游戏循环
        所谓游戏循环就是一个无限循环
        在创建游戏窗口代码下方，增加一个无限循环
            注意:游戏窗口不需要重复创建
            screen = pygame.display.set_mode((480,700))
            while True:
                pass

# 理解图像并实现图像绘制
    1.在游戏中,能够看到的游戏元素大多都是图像
        图像文件初始是保存在磁盘上的,如果需要使用,第一步就需要被加载到内存
    2.要在屏幕上看到某一个图像的内容,需要按照三个步骤:
        1.使用pygame.image.load()加载图像的数据
        2.使用游戏屏幕对象,调用blit方法将图像绘制到指定位置
        3.调用pygame.display.update方法更新整个屏幕的显示
        pygame.image.load(file_path)->pygame.Suface.blit(图像,位置)->pygame.display.update()
        提示:要想在屏幕上看到绘制的结果,就一定要调用pygame.display.update()方法
    3.透明图像
        png格式的图像是支持透明的
        在绘制图像时,透明区域不会显示任何内容
        但是如果下方已经有内容,会透过透明区域显示出来
    4.理解update()方法的作用
        可以在被screen对象完成所有blit方法之后,统一调用一次display.update方法,同样可以在屏幕上看到最终绘制结果
        使用display.set_mode()创建screen对象是一个内存中屏幕数据对象
            可以理解成油画的画布
        screen.blit方法可以在画布上绘制很多图像
        display.update()会将画布的最终结果绘制在屏幕上,这样可以提高屏幕绘制效率,增加游戏的流畅度

# 游戏中的动画实现原理
    跟电影的原理类似,游戏中的动画效果,本质上是快速的在屏幕上绘制图像
        电影是将多张静止的电影胶片连续、快速的播发,产生连贯的视觉效果
    一般在电脑上每妙绘制60次,就能够达到非常高品质的动画效果
        每次绘制的结果被称为帧Frame

# 游戏循环
    游戏的两个组成部分
        游戏循环的开始就意味着游戏的正式开始
    游戏初始化
        设置游戏
        绘制图像初始位置
        设置游戏时钟
    游戏循环
        设置刷新帧率
        检测用户交互
        更新所有图像位置
        更新屏幕显示
    游戏循环的作用
        1.保证游戏不会被直接退出
        2.变化的图像位置--动画效果
            每隔1/60秒移动一下所有图像的位置
            调用pygame.display.update()更新屏幕显示
        3.检测用户交互--按钮、鼠标等...

# 游戏时钟
    pygame专门提供了一个类pygame.time.Clock可以非常方便的设置屏幕绘制速度--刷新帧率
    要使用时钟对象需要两步:
        1.在游戏初始化创建一个时钟对象
        2.在游戏循环中让时钟对象调用tick(帧率)方法
    tick方法会根据上次被调用的时间,自动设置游戏循环中的延时

# 英雄动画的简单实现
    1.在游戏初始化定义一个pygame.Rect()的变量记录英雄的初始位置
    2.在游戏循环中每次让英雄的y-1 -- 向上移动
    3.y <= 0 将英雄移动到屏幕的底部
        提示: 每次调用update()方法之前，需要把所有的游戏图像都重新绘制一遍
        而且应该最先重新绘制背景图像

# 在游戏循中监听事件
    事件event
        就是游戏启动后,用户针对游戏所做的操作
        例如: 点击关闭按钮,点击鼠标,按下键盘...
    监听
        在游戏循环中,判断用户具体的操作
        只有捕获到用户的操作,才能有针对性的做出响应
    代码实现
        pygame中通过pygame.event.get()可以获得 用户当前所做动作的事件列表
            用户可以同一时间做很多事情
        提示: 这段代码非常固定,几乎所有的pygame 游戏都大同小异！
```python
    # 游戏循环
    while True:
        clock.tick(60)

    # 事件监听
    for event in pygame.event.get():
        
        # 判断用户是否点击了关闭按钮
        if event.type == pygame.QUIT:
            print("退出游戏")
            # 卸载所有模块
            pygame.quit()
            # 直接退出系统
            exit()
```

# 精灵和精灵组
    在刚刚完成的案例中,图像加载、位置变化、绘制图像都需要程序员编写代码分别处理
    为了简化开放步骤, pygame提供了两个类
        pygame.sprite.Sprite -- 存储图像数据image和位置rect对象
        pygame.spritye.Group
    
    精灵(需要派生子类)
        image 记录图像数据
        rect 记录在屏幕上的位置
        update(*args): 更新精灵位置
        kill(): 从所有组中删除

    精灵组
        __init__(self, *精灵)
        add(): 向组中在增加精灵
        sprites(): 返回所有精灵列表
        update(*args): 让组中所有精灵调用update方法
        draw(Suface): 将组中所有精灵的image,绘制到Suface的rect位置
    
    游戏初始化
        创建精灵
        创建精灵组
    
    游戏循环
        精灵组.update()
        精灵组.draw(screen)
        pygame.display.update()

# 派生精灵子类
    1.新建plane_sprites.py文件
    2.定义GameSprite继承自pygame.sprite.Sprite
    注意
        如果一个类的父类不是object
        在重写初始化方法时,一定要先super()一下父类的__init__方法
        保证父类中实现__init__代码能够被正常的执行
        GameSprite
            image
            rect
            speed
            __init__(self, image_name, speed=1);
            update(self);
        属性
            image 精灵图像,使用image_name加载
            rect 精灵大小,默认使用图像大小
            speed 精灵移动速度,默认为1
        方法
            update每次更新屏幕时在游戏循环内调用
                让精灵的self.rect.y += self.speed
        提示
            image的get_rect()方法,可以返回pygame.Rect(0,0,图像宽，图像高)的对象

# 游戏框架的搭建
    一个游戏主程序的职责可以分为两个部分:
        游戏初始化
        游戏循环
    游戏初始化
        设置游戏窗口
        创建游戏时钟
        创建精灵和精灵组
    游戏循环
        设置刷新帧率
        事件监听
        碰撞检测
        更新/绘制精灵组
        更新屏幕显示
    根据明确的职责,设计PlaneGame类
        screen
        clock
        精灵组或精灵...
        __init__(self): 游戏初始化
        __create_sprites(self):

        start_game(self): 游戏循环
        __event_hander(self):  事件监听
        __check_collide(self): 碰撞检测 -- 子弹销毁敌机、敌机撞毁英雄
        __update_sprites(self): 精灵组更新和绘制
        __game_over(): 游戏结束

# 游戏背景
    游戏启动后,背景图像会连续不断移动
    在视觉上产生英雄的飞机不断向上方飞行的错觉--在很多跑酷类游戏中常用的套路
        游戏的背景不断变化
        游戏的主角位置保持不变
    解决办法
        1.创建两张背景图像精灵
            第1张完全和屏幕组合
            第2张在屏幕的正上方
        2.两张图像一起向下运动
            self.rect.y += self.speed
        3.当任意背景精灵的rect.y>=屏幕的高度说明已经移动到下方
        4.当移动到屏幕下方的这张图像设置到屏幕的正上方
            rect.y = -rect.height

# 敌机出场 定时器
    在pygame中可以使用pygame.time.timer()来添加定时器
    所谓定时器,就是每隔一段时间去执行一些动作
        set_timer(eventid, milliseconds) -> None
            set_timer可以创建一个事件
            可以在游戏循环中的事件监听方法中捕获到改事件
            第1个参数事件代号需要基于常量pygame,USEREVENT来指定
                USEREVENT 是一个整数,再增加的事件可以使用USEREVENT+1指定,依次类推...
            第2个参数是事件触发的时间间隔的毫秒值
    定时器事件的监听
        通过pygame.event.get()可以获取当前时刻的事件列表
        遍历列表并且判断event.type是否等于eventid，如果相等,表示定时器事件发生
    
# 碰撞检测
    pygame提供了两个非常方便的方法可以实现碰撞检测
        pygame.sprite.groupcollide()
    两个精灵组中所有精灵的碰撞检测
        groupcollide(group1, group2, dokill1, dokill2, collied=Nore) -> Sprite_dict
            如果dokill设置为True,则发生碰撞的精灵将被自动移除
            collided参数是用于 计算碰撞的回调函数
                如果没有指定,则每个精灵必须是一个rect属性
    pygame.sprite.spritecollide()
        判断某个精灵和指定精灵组中的碰撞
        spritecollide(sprite, group, dokill, collided = None) -> Sprite_list
            如果dokill设置为True，则指定精灵组中发生的精灵将自动被移除
            collided参数是用于计算碰撞的回调函数
                如果没有指定,则每个精灵必须有一个rect属性
            返回精灵组中根精灵发生碰撞的精灵列表