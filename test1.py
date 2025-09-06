import turtle
import time
import random

# 设置游戏窗口
wn = turtle.Screen()
wn.title("贪吃蛇游戏")
wn.bgcolor("black")
wn.setup(width=600, height=600)
wn.tracer(0)  # 关闭窗口自动刷新

# 创建蛇头
snake_head = turtle.Turtle()
snake_head.speed(0)
snake_head.shape("square")
snake_head.color("white")
snake_head.penup()
snake_head.goto(0, 0)
snake_head.direction = "stop"

# 创建食物
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
food.goto(0, 100)

# 创建蛇的身体部分列表
segments = []

# 创建计分板
score = 0
high_score = 0
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("得分: 0  最高分: 0", align="center", font=("Arial", 24, "normal"))

# 定义移动函数
def go_up():
    if snake_head.direction != "down":
        snake_head.direction = "up"

def go_down():
    if snake_head.direction != "up":
        snake_head.direction = "down"

def go_left():
    if snake_head.direction != "right":
        snake_head.direction = "left"

def go_right():
    if snake_head.direction != "left":
        snake_head.direction = "right"

def move():
    if snake_head.direction == "up":
        y = snake_head.ycor()
        snake_head.sety(y + 20)
    
    if snake_head.direction == "down":
        y = snake_head.ycor()
        snake_head.sety(y - 20)
    
    if snake_head.direction == "left":
        x = snake_head.xcor()
        snake_head.setx(x - 20)
    
    if snake_head.direction == "right":
        x = snake_head.xcor()
        snake_head.setx(x + 20)

# 键盘绑定
wn.listen()
wn.onkeypress(go_up, "w")
wn.onkeypress(go_down, "s")
wn.onkeypress(go_left, "a")
wn.onkeypress(go_right, "d")
wn.onkeypress(go_up, "Up")
wn.onkeypress(go_down, "Down")
wn.onkeypress(go_left, "Left")
wn.onkeypress(go_right, "Right")

# 主游戏循环
while True:
    wn.update()
    
    # 检测与边界的碰撞
    if snake_head.xcor() > 290 or snake_head.xcor() < -290 or snake_head.ycor() > 290 or snake_head.ycor() < -290:
        time.sleep(1)
        snake_head.goto(0, 0)
        snake_head.direction = "stop"
        
        # 隐藏身体部分
        for segment in segments:
            segment.goto(1000, 1000)  # 移出屏幕
        
        # 清空身体部分列表
        segments.clear()
        
        # 重置分数
        score = 0
        
        # 更新分数显示
        pen.clear()
        pen.write("得分: {}  最高分: {}".format(score, high_score), align="center", font=("Arial", 24, "normal"))
    
    # 检测与食物的碰撞
    if snake_head.distance(food) < 20:
        # 将食物移动到随机位置
        x = random.randint(-270, 270)
        y = random.randint(-270, 270)
        food.goto(x, y)
        
        # 添加新的身体部分
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("grey")
        new_segment.penup()
        segments.append(new_segment)
        
        # 增加分数
        score += 10
        
        if score > high_score:
            high_score = score
        
        # 更新分数显示
        pen.clear()
        pen.write("得分: {}  最高分: {}".format(score, high_score), align="center", font=("Arial", 24, "normal"))
    
    # 移动身体部分
    for index in range(len(segments) - 1, 0, -1):
        x = segments[index - 1].xcor()
        y = segments[index - 1].ycor()
        segments[index].goto(x, y)
    
    # 移动第一个身体部分到蛇头的位置
    if len(segments) > 0:
        x = snake_head.xcor()
        y = snake_head.ycor()
        segments[0].goto(x, y)
    
    move()
    
    # 检测与自身的碰撞
    for segment in segments:
        if segment.distance(snake_head) < 20:
            time.sleep(1)
            snake_head.goto(0, 0)
            snake_head.direction = "stop"
            
            # 隐藏身体部分
            for segment in segments:
                segment.goto(1000, 1000)  # 移出屏幕
            
            # 清空身体部分列表
            segments.clear()
            
            # 重置分数
            score = 0
            
            # 更新分数显示
            pen.clear()
            pen.write("得分: {}  最高分: {}".format(score, high_score), align="center", font=("Arial", 24, "normal"))
    
    time.sleep(0.1)