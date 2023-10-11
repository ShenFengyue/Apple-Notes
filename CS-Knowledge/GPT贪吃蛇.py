import pygame
import random 

# 游戏窗口尺寸
window_width = 800
window_height = 600

# 蛇身格子尺寸和初始位置
snake_size = 20
snake_x = window_width // 2
snake_y = window_height // 2

# 食物格子尺寸和初始位置
food_size = 20
food_x = random.randint(0, (window_width - food_size) // food_size) * food_size
food_y = random.randint(0, (window_height - food_size) // food_size) * food_size

# 初始化pygame
pygame.init()

# 创建游戏窗口
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption('贪吃蛇游戏')

# 定义颜色
black = (0, 0, 0)
white = (255, 255, 255)
green = (0, 255, 0)

# 蛇的初始移动方向
snake_direction = "right"

# 蛇的初始长度
snake_length = 1
snake_body = [(snake_x, snake_y)]

# 游戏主循环
running = True
clock = pygame.time.Clock()

while running:
    # 处理退出事件
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # 处理按键事件
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT and snake_direction != "right":
                snake_direction = "left"
            elif event.key == pygame.K_RIGHT and snake_direction != "left":
                snake_direction = "right"
            elif event.key == pygame.K_UP and snake_direction != "down":
                snake_direction = "up"
            elif event.key == pygame.K_DOWN and snake_direction != "up":
                snake_direction = "down"

    # 移动蛇头
    if snake_direction == "right":
        snake_x += snake_size
    elif snake_direction == "left":
        snake_x -= snake_size
    elif snake_direction == "up":
        snake_y -= snake_size
    elif snake_direction == "down":
        snake_y += snake_size

    # 判断蛇是否吃到食物
    if snake_x == food_x and snake_y == food_y:
        # 生成新的食物
        food_x = random.randint(0, (window_width - food_size) // food_size) * food_size
        food_y = random.randint(0, (window_height - food_size) // food_size) * food_size
        # 增加蛇的长度
        snake_length += 1

    # 更新蛇的身体
    snake_body.append((snake_x, snake_y))
    if len(snake_body) > snake_length:
        del snake_body[0]

    # 检查蛇是否碰到自己
    if (snake_x, snake_y) in snake_body[:-1]:
        running = False

    # 检查蛇是否碰到边界
    if snake_x < 0 or snake_x >= window_width or snake_y < 0 or snake_y >= window_height:
        running = False

    # 渲染游戏界面
    window.fill(black)

    # 渲染食物
    pygame.draw.rect(window, green, (food_x, food_y, food_size, food_size))

    # 渲染蛇身体
    for body_part in snake_body:
        pygame.draw.rect(window, white, (body_part[0], body_part[1], snake_size, snake_size))

    # 刷新显示
    pygame.display.update()

    # 控制游戏速度
    clock.tick(10)

# 退出游戏
pygame.quit()


