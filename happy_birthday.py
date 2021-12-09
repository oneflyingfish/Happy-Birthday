# -*- coding: UTF-8 -*-
import turtle

#ctrl+shift+alt+l

def main():
    turtle.screensize(1800, 600)
    turtle.clear()
    # turtle.hideturtle()
    turtle.speed(4);
    turtle.pensize(6)

    # 绘制第一层奶油
    turtle.begin_fill()
    turtle.color('pink', 'pink')
    turtle.penup()
    turtle.goto(100, 100);
    turtle.pendown()
    turtle.setheading(150)
    turtle.circle(200, 60)
    turtle.penup()
    turtle.goto(-100, 100)
    turtle.pendown()
    # 描绘曲边
    turtle.setheading(-48)
    turtle.circle(50, 48)
    turtle.setheading(-36)
    turtle.circle(50, 48)
    turtle.setheading(-24)
    turtle.circle(50, 48)
    turtle.setheading(-12)
    turtle.circle(50, 48)
    turtle.setheading(0)
    turtle.circle(50, 48)

    turtle.goto(100, 100)
    turtle.end_fill()
    # 第一层奶油绘制及着色完毕

    # 绘制第一层蛋糕
    turtle.begin_fill()
    turtle.color('brown', 'brown')
    turtle.goto(100, 20)
    turtle.setheading(-150)
    turtle.circle(-200, 60)
    turtle.goto(-100, 100)
    turtle.color('white', 'brown')
    # 再次描绘曲边
    turtle.setheading(-48)
    turtle.circle(50, 48)
    turtle.setheading(-36)
    turtle.circle(50, 48)
    turtle.setheading(-24)
    turtle.circle(50, 48)
    turtle.setheading(-12)
    turtle.circle(50, 48)
    turtle.setheading(0)
    turtle.circle(50, 48)

    turtle.goto(100, 100)
    turtle.end_fill()

    # 绘制第二层蛋糕奶油
    turtle.penup()
    turtle.goto(-100, 20)
    turtle.pendown();  # turtle位置初始化完毕

    turtle.begin_fill()
    turtle.color('pink', 'pink')
    turtle.setheading(180)
    turtle.circle(60, 60)
    # 描绘曲边
    turtle.setheading(-48)
    turtle.circle(76, 48)
    turtle.setheading(-36)
    turtle.circle(76, 48)
    turtle.setheading(-24)
    turtle.circle(76, 48)
    turtle.setheading(-12)
    turtle.circle(76, 48)
    turtle.setheading(0)
    turtle.circle(76, 48)
    turtle.setheading(120)

    turtle.circle(60, 57)
    turtle.goto(100, 20)

    turtle.color('white', 'pink')
    turtle.setheading(-150)
    turtle.circle(-200, 60)
    turtle.end_fill()
    # turtle.end

    # 绘制第二层蛋糕
    turtle.begin_fill()
    turtle.penup()
    turtle.goto(-140, -31)
    turtle.pendown();
    # 再次描绘曲边
    turtle.color('white', 'green')
    turtle.goto(-152, -21)
    turtle.setheading(-48)
    turtle.circle(76, 48)
    turtle.setheading(-36)
    turtle.circle(76, 48)
    turtle.setheading(-24)
    turtle.circle(76, 48)
    turtle.setheading(-12)
    turtle.circle(76, 48)
    turtle.setheading(0)
    turtle.circle(76, 48)
    turtle.setheading(120)

    turtle.goto(140, -31)
    turtle.setheading(-90)
    turtle.color('green', 'green')
    turtle.goto(140, -110)
    turtle.setheading(-150)
    turtle.circle(-280, 60)
    turtle.goto(-140, -31)
    turtle.end_fill()
    # 至此，第一二层蛋糕绘制完毕

    #绘制第三层蛋糕
    turtle.begin_fill()
    turtle.penup()
    turtle.color('pink', 'pink')
    turtle.goto(-140,-110)
    turtle.pendown()

    turtle.setheading(180)
    turtle.circle(48,60)
    #绘制奶油
    turtle.setheading(-48)
    turtle.circle(91, 48)
    turtle.setheading(-36)
    turtle.circle(91, 48)
    turtle.setheading(-24)
    turtle.circle(91, 48)
    turtle.setheading(-12)
    turtle.circle(91, 48)
    turtle.setheading(0)
    turtle.circle(91, 48)
    turtle.setheading(90)

    turtle.setheading(120)
    turtle.circle(48, 56)
    turtle.color('white', 'pink')
    turtle.setheading(-150)
    turtle.circle(-280, 60)
    turtle.goto(-140,-110)
    turtle.end_fill()

    #绘制底层蛋糕
    turtle.begin_fill()
    turtle.penup()
    turtle.goto(-181,-136)
    turtle.pendown()
    turtle.color('white', 'orange')
    turtle.setheading(-48)
    turtle.circle(91, 48)
    turtle.setheading(-36)
    turtle.circle(91, 48)
    turtle.setheading(-24)
    turtle.circle(91, 48)
    turtle.setheading(-12)
    turtle.circle(91, 48)
    turtle.setheading(0)
    turtle.circle(91, 48)
    turtle.color('orange', 'orange')
    turtle.goto(180,-236)

    turtle.setheading(-150)
    turtle.circle(-362,60)
    turtle.goto(-181, -236)
    turtle.goto(-181, -136)
    turtle.end_fill()

    turtle.speed(1);
    #插蜡烛
    #上蜡烛一
    turtle.penup()
    turtle.goto(-85,100)
    turtle.pendown()
    turtle.pensize(8)
    turtle.color('yellow')
    turtle.goto(-85,160)

    turtle.pensize(1)
    turtle.color('brown')
    turtle.goto(-90, 170)
    turtle.pensize(10)
    turtle.color('orange')
    turtle.goto(-90, 172)

    # 上蜡烛二
    turtle.penup()
    turtle.goto(0, 85)
    turtle.pendown()
    turtle.pensize(8)
    turtle.color('yellow')
    turtle.goto(0, 145)

    turtle.penup()
    turtle.goto(0, 145)
    turtle.pendown()
    turtle.pensize(1)
    turtle.color('brown')
    turtle.goto(0, 155)
    turtle.pensize(10)
    turtle.color('orange')
    turtle.goto(0, 157)

    #上蜡烛3

    turtle.penup()
    turtle.goto(85, 100)
    turtle.pendown()
    turtle.pensize(8)
    turtle.color('yellow')
    turtle.goto(85, 160)

    turtle.penup()
    turtle.goto(85, 160)
    turtle.pendown()
    turtle.pensize(1)
    turtle.color('brown')
    turtle.goto(87, 170)
    turtle.pensize(10)
    turtle.color('orange')
    turtle.goto(87, 172)
    # 上蜡烛4

    turtle.penup()
    turtle.goto(-40, 115)
    turtle.pendown()
    turtle.pensize(8)
    turtle.color('yellow')
    turtle.goto(-40, 160)

    turtle.penup()
    turtle.goto(-40, 160)
    turtle.pendown()
    turtle.pensize(1)
    turtle.color('brown')
    turtle.goto(-38, 170)
    turtle.pensize(10)
    turtle.color('orange')
    turtle.goto(-38, 172)

    # 上蜡烛5
    turtle.penup()
    turtle.goto(40, 115)
    turtle.pendown()
    turtle.pensize(8)
    turtle.color('yellow')
    turtle.goto(40, 160)

    turtle.penup()
    turtle.goto(40, 160)
    turtle.pendown()
    turtle.pensize(1)
    turtle.color('brown')
    turtle.goto(39, 170)
    turtle.pensize(10)
    turtle.color('orange')
    turtle.goto(39, 172)

    # 下蜡烛1

    turtle.penup()
    turtle.goto(-170, -120)
    turtle.pendown()
    turtle.pensize(8)
    turtle.color('yellow')
    turtle.goto(-175, -60)

    turtle.penup()
    turtle.goto(-175, -60)
    turtle.pendown()
    turtle.pensize(1)
    turtle.color('brown')
    turtle.goto(-175, -50)
    turtle.pensize(10)
    turtle.color('orange')
    turtle.goto(-175, -48)

    # 下蜡烛2
    turtle.penup()
    turtle.goto(160, -120)
    turtle.pendown()
    turtle.pensize(8)
    turtle.color('yellow')
    turtle.goto(162, -60)

    turtle.penup()
    turtle.goto(162, -60)
    turtle.pendown()
    turtle.pensize(1)
    turtle.color('brown')
    turtle.goto(160, -50)
    turtle.pensize(10)
    turtle.color('orange')
    turtle.goto(160, -48)

    # 下蜡烛3
    turtle.penup()
    turtle.goto(-60, -170)
    turtle.pendown()
    turtle.pensize(8)
    turtle.color('yellow')
    turtle.goto(-60, -110)

    turtle.penup()
    turtle.goto(-60, -110)
    turtle.pendown()
    turtle.pensize(1)
    turtle.color('brown')
    turtle.goto(-60, -100)
    turtle.pensize(10)
    turtle.color('orange')
    turtle.goto(-60, -98)

    # 下蜡烛4
    turtle.penup()
    turtle.goto(60, -170)
    turtle.pendown()
    turtle.pensize(8)
    turtle.color('yellow')
    turtle.goto(60, -110)

    turtle.penup()
    turtle.goto(60, -110)
    turtle.pendown()
    turtle.pensize(1)
    turtle.color('brown')
    turtle.goto(62, -100)
    turtle.pensize(10)
    turtle.color('orange')
    turtle.goto(62, -98)

    turtle.pensize(2)
    turtle.color('deepskyblue')

    turtle.penup()
    turtle.goto(-112, -30)
    turtle.pendown()
    turtle.write("x", font=('华文行楷', 25, 'normal'))

    turtle.penup()
    turtle.goto(-79, -45)
    turtle.pendown()
    turtle.write("x", font=('华文行楷', 25, 'normal'))

    turtle.penup()
    turtle.goto(-46, -50)
    turtle.pendown()
    turtle.write("x", font=('华文行楷', 25, 'normal'))
    
    turtle.penup()
    turtle.goto(-13, -60)
    turtle.pendown()
    turtle.write("生", font=('华文行楷', 25, 'normal'))

    turtle.penup()
    turtle.goto(20, -50)
    turtle.pendown()
    turtle.write("日", font=('华文行楷', 25, 'normal'))

    turtle.penup()
    turtle.goto(53, -40)
    turtle.pendown()
    turtle.write("快", font=('华文行楷', 25, 'normal'))

    turtle.penup()
    turtle.goto(86, -20)
    turtle.pendown()
    turtle.write("乐", font=('华文行楷', 25, 'normal'))

    turtle.penup()
    turtle.goto(230,-300)
    turtle.pendown()
    turtle.write("----from xx", font=('宋体', 15, 'normal'))

    turtle.hideturtle()
    turtle.mainloop()

if __name__ == '__main__':
    main()
