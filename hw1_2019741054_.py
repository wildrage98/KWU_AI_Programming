import turtle as t

t.speed(0)
t.setup(width=400, height=380)
 #크기설정
t.screensize( 10,10 ,'#0E639E') 
# 바탕색 푸른색으로 설정



def move(x,y): 
    t.pu()
    t.home()
    t.goto(x,y)
    t.pd()
    return
#이동
def sun(r, color): 
    t.color(color)
    t.fillcolor(color)
    t.begin_fill()
    t.circle(r)
    t.end_fill()
# 노을의 반지름과 색
def mount(x,y,size,color): 
    move(x,y)
    t.color(color)
    t.fillcolor(color)
    t.begin_fill()
    for i in range(3):
        t.forward(size)
        t.left(120)
    t.end_fill()
    return
#산의 시작점과 크기, 색

move(30,20-120)
sun(180,'violetred')
move(30,40-120)
sun(160, 'pink')
move(30,60-120)
sun(140, 'red')
move(30,80-120)
sun(120, 'orange')
move(30,100-120)
sun(100, 'yellow')
#노을 


move(-200,0)
t.fillcolor('green')
t.begin_fill()
t.forward(400)
t.left(90)
t.forward(-190)
t.left(90)
t.forward(400)
t.end_fill()
#땅


mount(-240,-70,250,'lightgray')
mount(-90,-70,250,'lightgray')
mount(0,-90,250,'lightgray')

mount(-290,-90,190,'gray90')
mount(80,-90,190,'gray90')
mount(-150,-90,190,'gray90')
mount(-10,-85,160,'gray90')


mount(-240,-130,190,'gray70')
mount(-100,-110,120,'gray70')
#산


move(105,-190)
t.color('ivory')
t.fillcolor('ivory')
t.begin_fill()
t.left(70)
t.forward(50)
t.left(30)
t.forward(20)
t.left(50)
t.forward(30)
t.left(45)
t.forward(40)

t.right(90)
t.forward(10)
t.right(80)
t.forward(40)
t.right(40)
t.forward(30)
t.right(40)
t.forward(40)
t.right(30)
t.forward(60)
t.end_fill()
#길


mount(-50,-120,130,'gray70')
#길을 덮는 산

t.done()
#끝