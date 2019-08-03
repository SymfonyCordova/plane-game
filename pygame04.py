import pygame
from plane_sprites import *

# 游戏初始化加载pygame
pygame.init()

# 创建游戏的窗口
screen = pygame.display.set_mode((480,700))

# 绘制背景图像
background = pygame.image.load("./images/background.png")
screen.blit(background, (0, 0))
# pygame.display.update()

# 绘制英雄的飞机
heroMe1 = pygame.image.load("./images/me1.png")
screen.blit(heroMe1, (150, 300))
pygame.display.update()

# 创建时钟对象
clock = pygame.time.Clock()

# 定义rect记录飞机的初始位置
heroMe1Rect = pygame.Rect(150, 300, 102, 126)

# 创建敌机的精灵
enemy = GameSprite("./images/enemy1.png")
enemy1 = GameSprite("./images/enemy1.png", 2)

# 创建敌机的精灵组
enemyGroup = pygame.sprite.Group(enemy, enemy1)

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
    heroMe1Rect.y -= 1

    # 判断飞机的位置
    if heroMe1Rect.bottom <= 0:
        heroMe1Rect.y = 700
    
    # 调用blit方法绘制图像
    screen.blit(background, (0, 0))
    screen.blit(heroMe1, heroMe1Rect)

    # 让精灵组调用两个方法
    # update - 让组中所有精灵更新位置
    enemyGroup.update()

    # draw - 在screen上绘制所有的精灵
    enemyGroup.draw(screen)
    
    # 调用update方法更新显示
    pygame.display.update()

pygame.quit()