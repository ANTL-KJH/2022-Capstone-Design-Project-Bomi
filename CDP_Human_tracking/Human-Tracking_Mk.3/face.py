import turtle
from turtle import *
from datetime import datetime
import numpy as np

frame = np.array([[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], \
                  [0,0,1,1,1,1,1,0,0,0,0,0,0,1,1,1,1,1,0,0], \
                  [0,0,1,1,1,1,1,0,0,0,0,0,0,1,1,1,1,1,0,0], \
                  [0,0,1,1,0,1,1,0,0,0,0,0,0,1,1,0,1,1,0,0], \
                  [0,0,1,1,0,1,1,0,0,0,0,0,0,1,1,0,1,1,0,0], \
                  [0,0,1,1,0,1,1,0,0,0,0,0,0,1,1,0,1,1,0,0], \
                  [0,0,1,1,1,1,1,0,0,0,0,0,0,1,1,1,1,1,0,0], \
                  [0,0,1,1,1,1,1,0,0,0,0,0,0,1,1,1,1,1,0,0], \
                  [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], \
                  [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], \
                  [0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0], \
                  [0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0], \
                  [0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0], \
                  [0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0], \
                  [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]])

frame2 = np.array([[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], \
                  [0,0,1,1,1,0,0,0,0,0,0,0,0,0,0,1,1,1,0,0], \
                  [0,0,0,1,1,1,0,0,0,0,0,0,0,0,1,1,1,0,0,0], \
                  [0,0,0,0,1,1,1,0,0,0,0,0,0,1,1,1,0,0,0,0], \
                  [0,0,0,0,0,1,1,1,0,0,0,0,1,1,1,0,0,0,0,0], \
                  [0,0,0,0,1,1,1,0,0,0,0,0,0,1,1,1,0,0,0,0], \
                  [0,0,0,1,1,1,0,0,0,0,0,0,0,0,1,1,1,0,0,0], \
                  [0,0,1,1,1,0,0,0,0,0,0,0,0,0,0,1,1,1,0,0], \
                  [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], \
                  [0,0,0,0,0,0,1,1,1,1,1,1,1,1,0,0,0,0,0,0], \
                  [0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0], \
                  [0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0], \
                  [0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0], \
                  [0,0,0,0,0,0,1,1,1,1,1,1,1,1,0,0,0,0,0,0], \
                  [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]])



def jump(distance): # 펜이동 
    penup()
    forward(distance)
    pendown()

def rectangle(width, height, fill_color):
    begin_fill()
    fillcolor(fill_color)
    setheading(45)
    turtle.circle(15, steps = 4)
    rt(45);
    
    #fd(width); lt(90); fd(height); lt(90)
    #fd(width); lt(90); fd(height); lt(90)

def draw(width, height):
    rt(90)
    radius = 160
    #reset() #초기화
    pensize(4) #펜 굵기
    for i in range(15):
        for j in range(20):
            if frame[i][j] == 0:
                fill_color='skyblue'
                color(fill_color)
                #dot(10, 'black')
            else:
                fill_color='black'
                color(fill_color)
                #dot(10, 'green')
            rectangle(width, height, fill_color)
            
            jump(30)
        rt(90); jump(30); rt(90); jump(600); rt(90); rt(90)



def makeOnePickcell(name, width, height):
    reset()
    pensize(2)
    penup()
    goto(-280, 250)
    pendown()
    draw(width, height)
    ht()
    
    #rectangle(width, height)

def makingFrame():
    global pickcell
    makeOnePickcell("Black_Block", 20, 15)

def BomiFace():
    tracer(False) #터틀이 그리는건 보여주지 않음
    makingFrame()
    turtle.setup(800, 600) #800x600 크기의 픽셀 준비
    turtle.title("Bomi") # 프로그램 제목
    

"""
1.각각 프레임을 아이디형태로 가짐 (가로, 세로, 색깔)ex (1,1,0)
2.각각의 프레임을 터틀그래픽으로 한번에 모두 그림
3.그리는 도중에 색깔 인덱스가 1이면 색이 녹색이다. 0이면 모두 검은색이다.
4.
"""
if __name__ == "__main__":
    main()