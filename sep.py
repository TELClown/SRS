import speech
import time
import matplotlib.pyplot as plt
import turtle
def draw():
    # 画图
    turtle.pensize(5)
    turtle.pencolor("red")
    turtle.fillcolor("red")
    turtle.goto(-50,50)
    turtle.left(70)
    turtle.begin_fill()
    turtle.begin_fill()
    for i in range(4):
        turtle.forward(200)
        turtle.right(140)
        turtle.forward(200)
        turtle.left(50)
    turtle.end_fill()
    turtle.penup()
    
    print("电风扇打开成功！")
    speech.say("电风扇打开成功！")

def switch(action):
    #仿真ui打开python画图界面画一个风扇
    try:
        if "on" in action.lower(): # action 为 on时表示语音输入为打开电风扇，则开始画图
            draw()
        else: # 否则为关闭电风扇
            print("电风扇关闭成功！")
            speech.say("电风扇关闭成功！")
            turtle.bye()
            
        #无错时返回 1
        response_code = 1

    except Exception as exec:
        #报错，返回-1表示出错
        print(str(exec))
        response_code = -1
    
    return response_code

while True:
    response = speech.input()  #接收语音
    print("your order is" + response)
    if "电风扇" in response and "开" in response :
        re = switch("on")
        if re<0:
            print("电风扇打开失败")
            speech.say("电风扇打开失败")
            exit()
            
    if "电风扇" in response and "关" in response :
        switch("off")
        if re<0:
            print("电风扇关闭失败")
            speech.say("电风扇关闭失败")
            exit()
