import pygame

pygame.init()

# 创建游戏的窗口
screen = pygame.display.set_mode((480,700))

# 绘制背景图像
background = pygame.image.load("./images/background.png")
screen.blit(background, (0, 0))
# pygame.display.update()

# 绘制英雄的飞机
hero_me1 = pygame.image.load("./images/me1.png")
screen.blit(hero_me1, (150, 300))
pygame.display.update()

# 创建时钟对象
clock = pygame.time.Clock()

# 定义rect记录飞机的初始位置
hero_me1_rect = pygame.Rect(150, 300, 102, 126)

# 循环保证
while True:
    clock.tick(60)

    # 捕获事件
    for event in pygame.event.get():  
        # 判断用户是否点击了关闭按钮
        if event.type == pygame.QUIT:
            print("退出游戏")
            # 卸载游戏模块
            pygame.quit()
            # 直接退出系统
            exit()

    # 修改飞机的位置
    hero_me1_rect.y -= 1

    # 判断飞机的位置
    if hero_me1_rect.bottom <= 0:
        hero_me1_rect.y = 700
    
    # 调用blit方法绘制图像
    screen.blit(background, (0, 0))
    screen.blit(hero_me1, hero_me1_rect)
    
    # 调用update方法更新显示
    pygame.display.update()

pygame.quit()