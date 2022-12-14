import turtle
wn=turtle.Screen()
wn.title("Sharp Art Coding Creations")
wn.bgcolor('deep sky blue')#deep sky blue
wn.setup(1280,768)

c=turtle.Turtle()
c.speed(0)

c.up()
c.goto(-640,-7)
c.down()
c.begin_fill()
c.color("white","green")
c.pensize(10)
c.seth(0)
c.fd(1280)
c.seth(-90)
c.fd(384)
c.seth(180)
c.fd(1280)
c.seth(90)
c.fd(384)
c.end_fill()

c.pensize(10)
c.up()
c.home()
c.seth(0)
c.fd(80)
c.seth(-90)
c.fd(12)

c.color("black")
c.seth(180)
c.fd(160)
c.down()
c.begin_fill()
c.color("white","gray")
c.seth(-135)
c.fd(500)
c.seth(0)
c.fd(865)
c.seth(135)
c.fd(500)
c.end_fill()

c.pensize(10)
c.color("black")
c.up()
c.home()
c.seth(-90)
c.fd(70)
c.down()
c.begin_fill()
c.color("white","green")
c.seth(180)
c.fd(15)
c.bk(30)
c.seth(-45)
c.fd(250)
c.seth(180)
c.fd(385)
c.seth(45)
c.fd(250)
c.end_fill()

c.color("black")
c.up()
c.home()
c.seth(0)
c.fd(640)
c.seth(-90)
c.fd(384)
c.down()
c.begin_fill()
c.color("white","gray")
c.seth(90)
c.fd(100)
c.seth(180)
c.fd(305)
c.seth(-45)
c.color("grey","gray")
c.fd(120)
c.end_fill()




c.up()
c.goto(-625,0)
c.down()
#c.ht()

c.pensize(1)
c.begin_fill()
c.color("#c19973","white")  #a29187
c.seth(90)
c.fd(200)
c.seth(0)
c.fd(1250)
c.seth(-90)
c.fd(200)
c.seth(180)
c.fd(1250)
c.end_fill()

for i in range(25):
    c.seth(90)
    c.pensize(5)
    c.fd(200)
    c.bk(200)
    c.seth(0)
    c.pensize(1)
    c.fd(50)

c.pensize(5)
c.seth(90)
c.fd(200)


c.up()
c.goto(-625,0)
c.down()

for i in range(25):
    c.begin_fill()
    c.color("#c19973","#cd805f")    #ac7e6c
    c.pensize(5)
    c.seth(90)
    c.fd(66.5)
    c.pensize(3)
    c.seth(0)
    c.fd(50)
    c.pensize(5)
    c.seth(-90)
    c.fd(66.5)
    c.pensize(3)
    c.seth(180)
    c.fd(50)
    c.end_fill()
    c.bk(50)
    

c.up()
c.goto(-625,0)
c.seth(90)
c.fd(16)
c.seth(0)
c.fd(10)
c.down()

for i in range(25):
    c.begin_fill()
    c.color("#c19973","#807f83")
    c.pensize(4)
    c.seth(90)
    c.fd(30)
    c.seth(0)
    c.fd(30)
    c.seth(-90)
    c.fd(30)
    c.seth(180)
    c.fd(30)
    c.end_fill()
    c.seth(90)
    c.fd(30)
    c.seth(0)
    c.fd(10)
    c.seth(-90)
    c.color("white")
    c.pensize(2)
    c.up()
    c.fd(2)
    c.down()
    c.fd(28)
    c.seth(0)
    c.color("#c19973")
    c.pensize(4)
    c.fd(10)
    c.seth(90)
    c.color("white")
    c.pensize(2)
    c.up()
    c.fd(2)
    c.down()
    c.fd(28)
    c.seth(0)
    c.color("#c19973")
    c.pensize(4)
    c.fd(10)
    c.seth(-90)
    c.color("#c19973")
    c.pensize(4)
    c.fd(10)
    c.seth(180)
    c.color("white")
    c.pensize(2)
    c.up()
    c.fd(2)
    c.down()
    c.fd(28)
    c.seth(-90)
    c.color("#c19973")
    c.pensize(4)
    c.fd(20)
    c.up()
    c.seth(0)
    c.color("#c19973")
    c.pensize(4)
    c.fd(50)
    c.down()


c.up()
c.goto(-625,0)
c.seth(90)
c.fd(90)
c.seth(0)
c.fd(10)
c.down()


for i in range(25):
    c.begin_fill()
    c.color("#c19973","#cd805f")
    c.pensize(4)
    c.seth(90)
    c.fd(90)
    c.seth(0)
    c.fd(30)
    c.seth(-90)
    c.fd(90)
    c.seth(180)
    c.fd(30)
    c.end_fill()
    c.seth(90)
    c.fd(60)

    c.begin_fill()
    c.color("#c19973","#807f83")
    c.pensize(4)
    c.seth(90)
    c.fd(30)
    c.seth(0)
    c.fd(30)
    c.seth(-90)
    c.fd(30)
    c.seth(180)
    c.fd(30)
    c.end_fill()
    c.seth(90)
    c.fd(30)
    c.seth(0)
    c.fd(10)
    c.seth(-90)
    c.color("white")
    c.pensize(2)
    c.up()
    c.fd(2)
    c.down()
    c.fd(28)
    c.seth(0)
    c.color("#c19973")
    c.pensize(4)
    c.fd(10)
    c.seth(90)
    c.color("white")
    c.pensize(2)
    c.up()
    c.fd(2)
    c.down()
    c.fd(28)
    c.seth(0)
    c.color("#c19973")
    c.pensize(4)
    c.fd(10)
    c.seth(-90)
    c.color("#c19973")
    c.pensize(4)
    c.fd(10)
    c.seth(180)
    c.color("white")
    c.pensize(2)
    c.up()
    c.fd(2)
    c.down()
    c.fd(28)
    c.seth(-90)
    c.color("#c19973")
    c.pensize(4)
    c.fd(20)
    c.up()
    c.seth(-90)
    c.color("#c19973")
    c.pensize(4)
    c.fd(60)
    c.down()
    c.begin_fill()
    c.color("#c19973","#807f83")
    c.pensize(4)
    c.seth(90)
    c.fd(30)
    c.seth(0)
    c.fd(30)
    c.seth(-90)
    c.fd(30)
    c.seth(180)
    c.fd(30)
    c.end_fill()
    c.seth(90)
    c.fd(30)
    c.seth(0)
    c.fd(10)
    c.seth(-90)
    c.color("white")
    c.pensize(2)
    c.up()
    c.fd(2)
    c.down()
    c.fd(28)
    c.seth(0)
    c.color("#c19973")
    c.pensize(4)
    c.fd(10)
    c.seth(90)
    c.color("white")
    c.pensize(2)
    c.up()
    c.fd(2)
    c.down()
    c.fd(28)
    c.seth(0)
    c.color("#c19973")
    c.pensize(4)
    c.fd(10)
    c.seth(-90)
    c.color("#c19973")
    c.pensize(4)
    c.fd(10)
    c.seth(180)
    c.color("white")
    c.pensize(2)
    c.up()
    c.fd(2)
    c.down()
    c.fd(28)
    c.seth(-90)
    c.color("#c19973")
    c.pensize(4)
    c.fd(20)
    c.up()
    c.seth(0)
    c.color("#c19973")
    c.pensize(4)
    c.fd(50)
    c.down()



c.up()
c.home()
c.seth(180)
c.fd(75)
c.down()
c.begin_fill()
c.color("#c19973","#cd805f")#c19973
c.pensize(5)
c.seth(90)
c.fd(200)
c.seth(0)
c.fd(150)
c.seth(-90)
c.fd(200)
c.seth(180)
c.fd(150)
c.end_fill()


c.ht()
c.pensize(2)
c.seth(90)
c.fd(110)
c.seth(0)
c.begin_fill()
c.color("#c19973","white")#c19973
c.pensize(3)
c.fd(15)
c.seth(90)
c.fd(60)
c.seth(35)
c.circle(-100,36)
c.circle(-100,36)
c.seth(-90)
c.fd(58)
c.seth(0)
c.fd(16)
c.seth(90)
c.fd(89)
c.seth(180)
c.fd(148)
c.seth(-90)
c.fd(89)
c.end_fill()

c.up()
c.home()
c.seth(180)
c.fd(75)
c.pensize(5)
c.seth(90)
c.fd(200)
c.seth(0)
c.fd(25)
c.pensize(1)
c.seth(-90)
c.fd(55)
c.down()

for i in range(3):
    c.begin_fill()
    c.color("white","#807f83")
    c.pensize(2)
    c.seth(90)
    c.fd(24)
    c.seth(0)
    c.fd(24)
    c.seth(-90)
    c.fd(24)
    c.seth(180)
    c.fd(24)
    c.end_fill()
    c.seth(90)
    c.fd(24)
    c.seth(0)
    c.fd(8)
    c.seth(-90)
    c.fd(24)
    c.seth(0)
    c.fd(8)
    c.seth(90)
    c.fd(24)
    c.seth(0)
    c.fd(8)
    c.seth(-90)
    c.fd(8)
    c.seth(180)
    c.fd(24)
    c.seth(-90)
    c.fd(16)
    c.up()
    c.seth(0)
    c.fd(38)
    c.down()




c.color("#c19973")#c19973
c.up()
c.home()
c.seth(180)
c.fd(75)
c.down()
c.pensize(5)
c.begin_fill()
c.color("#c19973","white")#c19973
c.seth(90)
c.fd(110)
c.seth(180)
c.fd(5)
c.bk(5)
c.seth(0)
c.fd(155)
c.bk(5)
c.seth(-90)
c.fd(110)
c.pensize(5)
c.seth(180)
c.fd(20)
c.seth(90)
c.fd(70)
c.seth(135)
c.circle(77,45)
c.circle(77,45)
c.seth(-90)
c.fd(70)
c.seth(180)
c.fd(20)
c.end_fill()



c.pensize(5)
c.up()
c.home()
c.seth(180)
c.fd(49)
c.down()
c.seth(90)
c.fd(10)
c.begin_fill()
c.color("#391a1f","#391a1f")
c.fd(50)
c.seth(0)
c.fd(98)
c.seth(-90)
c.fd(50)
c.seth(180)
c.fd(98)
c.end_fill()


c.begin_fill()
c.color("black","#3d3a36")
c.pensize(3)
c.seth(180)
c.fd(1)
c.seth(-90)
c.fd(10)
c.seth(0)
c.fd(100)
c.seth(90)
c.fd(10)
c.seth(180)
c.fd(100)
c.end_fill()
c.seth(-90)
c.fd(5)
c.seth(0)
c.fd(100)

c.up()
c.seth(90)
c.fd(58)
c.down()
c.begin_fill()
c.color("white","white")
c.fd(5)
c.seth(135)
c.circle(70.5,45)
c.circle(70.5,45)
c.seth(-90)
c.fd(5)
c.seth(0)
c.fd(100)
c.end_fill()

c.up()
c.home()
c.seth(90)
c.fd(13)
c.down()
c.begin_fill()
c.color("orange","gold")
c.seth(180)
c.fd(15)
c.seth(90)
c.fd(35)
c.seth(0)
c.fd(15)
c.seth(-90)
c.fd(35)
c.seth(0)
c.fd(15)
c.seth(90)
c.fd(35)
c.seth(180)
c.fd(15)
c.end_fill()

c.up()
c.home()
c.seth(180)
c.fd(75)
c.seth(90)
c.fd(110)
c.seth(180)
c.fd(2)
c.down()
for i in range(3):
    c.begin_fill()
    c.color("#c19973","brown")
    c.pensize(2)
    c.seth(90)
    c.fd(15)
    c.seth(0)
    c.fd(5)
    c.seth(-90)
    c.fd(15)
    c.seth(180)
    c.fd(5)
    c.end_fill()
    c.seth(90)
    c.fd(15)
    c.seth(0)
    c.fd(2.5)
    c.begin_fill()
    c.color("white","white")
    c.circle(2.5)
    c.end_fill()
    c.color("#c19973")
    c.seth(0)
    c.fd(2.5)
    c.seth(-90)
    c.fd(15)
    c.seth(180)
    c.fd(5)
    c.seth(0)
    c.fd(5)
    c.pensize(3)
    c.seth(90)
    c.fd(10)
    c.seth(50)
    c.fd(5)
    c.seth(-50)
    c.fd(5)
    c.seth(-90)
    c.fd(10)

    c.seth(90)
    c.fd(10)
    c.seth(50)
    c.fd(5)
    c.seth(-50)
    c.fd(5)
    c.seth(-90)
    c.fd(10)

    c.seth(90)
    c.fd(10)
    c.seth(50)
    c.fd(5)
    c.seth(-50)
    c.fd(5)
    c.seth(-90)
    c.fd(10)

    c.seth(90)
    c.fd(10)
    c.seth(50)
    c.fd(5)
    c.seth(-50)
    c.fd(5)
    c.seth(-90)
    c.fd(10)

    c.seth(90)
    c.fd(10)
    c.seth(50)
    c.fd(5)
    c.seth(-50)
    c.fd(5)
    c.seth(-90)
    c.fd(10)

    c.seth(90)
    c.fd(10)
    c.seth(50)
    c.fd(5)
    c.seth(-50)
    c.fd(5)
    c.seth(-90)
    c.fd(10)

    c.seth(90)
    c.fd(10)
    c.seth(50)
    c.fd(5)
    c.seth(-50)
    c.fd(5)
    c.seth(-90)
    c.fd(10)

c.begin_fill()
c.color("#c19973","brown")
c.pensize(2)
c.seth(90)
c.fd(15)
c.seth(0)
c.fd(5)
c.seth(-90)
c.fd(15)
c.seth(180)
c.fd(5)
c.end_fill()
c.seth(90)
c.fd(15)
c.seth(0)
c.fd(2.5)
c.begin_fill()
c.color("white","white")
c.circle(2.5)
c.end_fill()
################


c.color("#c19973")
c.up()
c.home()
c.seth(180)
c.fd(75)
c.seth(90)
c.fd(200)
c.down()
c.pensize(10)
c.seth(90)
c.fd(20)
c.seth(10)
c.fd(50)
c.seth(-90)
c.fd(25)
c.bk(25)
c.seth(0)
c.fd(52)
c.seth(-90)
c.fd(25)
c.bk(25)
c.seth(-10)
c.fd(50)
c.seth(-90)
c.fd(20)

c.pensize(5)
c.seth(180)
c.fd(150)
c.seth(90)
c.fd(20)
c.pensize(5)
c.color("white")
c.begin_fill()
c.color("#c19973","white")
c.seth(10)
c.fd(50)
c.bk(55)
c.fd(55)
c.seth(0)
c.fd(52)
c.seth(-10)
c.fd(55)
c.bk(5)
c.pensize(5)
c.seth(110)
c.circle(30,50)
c.seth(90)
c.fd(5)
c.seth(30)
c.fd(10)
c.seth(170)
c.fd(45)
c.seth(180)
c.fd(47)
c.seth(-170)
c.fd(45)
c.seth(-30)
c.fd(10)
c.seth(-90)
c.fd(5)
c.seth(-150)
c.circle(30,45)
c.end_fill()


c.color("black")
c.up()
c.home()
c.seth(90)
c.fd(255)

c.down()
c.begin_fill()
c.color("#cd805f","#cd805f")
c.seth(180)
c.fd(28.5)
c.seth(-170)
c.fd(40)
c.seth(90)
c.circle(-67,180)
c.seth(170)
c.fd(40)
c.seth(180)
c.fd(28.5)
c.end_fill()
c.up()
c.color("black")
c.seth(180)
c.fd(28.5)
c.seth(-170)
c.fd(40)
c.seth(90)
c.circle(-67,60)
c.down()
c.begin_fill()
c.color("brown","brown")
c.fd(40)
c.seth(-30)
c.fd(40)
c.seth(-160)
c.circle(-100,40)
c.end_fill()

c.seth(30)
c.fd(37)
c.pensize(3)
c.begin_fill()
c.color("black","dark blue")
c.seth(0)
c.circle(10,180)
c.seth(60)
c.fd(10)
c.seth(100)
c.fd(20)
c.seth(-100)
c.fd(20)
c.seth(-60)
c.fd(10)
c.seth(180)
c.circle(10,180)
c.end_fill()

#######
c.color("#c19973")
c.up()
c.home()
c.seth(180)
c.fd(600)
c.seth(90)
c.fd(200)

c.down()
c.pensize(10)
c.seth(90)
c.fd(15)
c.seth(10)
c.fd(33)
c.seth(-90)
c.fd(20)
c.bk(20)
c.seth(0)
c.fd(35)
c.seth(-90)
c.fd(20)
c.bk(20)
c.seth(-10)
c.fd(33)
c.seth(-90)
c.fd(15)

c.pensize(5)
c.seth(180)
c.fd(100)
c.seth(90)
c.fd(15)

c.pensize(5)
c.color("white")
c.begin_fill()
c.color("#c19973","white")
c.seth(10)
c.fd(33)
c.bk(38)
c.fd(38)
c.seth(0)
c.fd(35)
c.seth(-10)
c.fd(38)
c.bk(2)
c.pensize(5)
c.seth(110)
c.circle(20,50)
c.seth(90)
c.fd(3)
c.seth(30)
c.fd(7)
c.seth(170)
c.fd(32)
c.seth(180)
c.fd(34)
c.seth(-170)
c.fd(32)
c.seth(-30)
c.fd(7)
c.seth(-90)
c.fd(3)
c.seth(-150)
c.circle(20,45)
c.end_fill()

c.color("black")
c.up()
c.home()
c.seth(180)
c.fd(550)
c.seth(90)
c.fd(240)


c.down()
c.begin_fill()
c.color("#cd805f","#cd805f")
c.seth(180)
c.fd(17)
c.seth(-170)
c.fd(30)
c.seth(90)
c.circle(-46,180)
c.seth(170)
c.fd(30)
c.seth(180)
c.fd(17)
c.end_fill()

c.up()
c.color("black")
c.seth(180)
c.fd(17)
c.seth(-170)
c.fd(30)
c.seth(90)
c.circle(-46,60)
c.down()
c.begin_fill()
c.color("brown","brown")
c.fd(30)
c.seth(-30)
c.fd(30)
c.seth(-160)
c.circle(-78,40)
c.end_fill()

c.seth(30)
c.fd(30)
c.pensize(2)
c.begin_fill()
c.color("black","dark blue")
c.seth(0)
c.circle(7,180)
c.seth(60)
c.fd(7)
c.seth(100)
c.fd(15)
c.seth(-100)
c.fd(15)
c.seth(-60)
c.fd(7)
c.seth(180)
c.circle(7,180)
c.end_fill()
####

c.color("#c19973")
c.up()
c.home()
c.seth(0)
c.fd(600)
c.seth(90)
c.fd(200)

c.down()
c.pensize(10)
c.seth(90)
c.fd(15)
c.seth(170)
c.fd(33)
c.seth(-90)
c.fd(20)
c.bk(20)
c.seth(180)
c.fd(35)
c.seth(-90)
c.fd(20)
c.bk(20)
c.seth(-170)
c.fd(33)
c.seth(-90)
c.fd(15)

c.pensize(5)
c.seth(0)
c.fd(100)
c.seth(90)
c.fd(15)

c.pensize(5)
c.color("white")
c.begin_fill()
c.color("#c19973","white")
c.seth(170)
c.fd(33)
c.bk(38)
c.fd(38)
c.seth(180)
c.fd(35)
c.seth(-170)
c.fd(38)
c.bk(2)
c.pensize(5)
c.seth(70)
c.circle(-20,50)
c.seth(90)
c.fd(3)
c.seth(150)
c.fd(7)
c.seth(10)
c.fd(32)
c.seth(0)
c.fd(34)
c.seth(-10)
c.fd(32)
c.seth(-150)
c.fd(7)
c.seth(-90)
c.fd(3)
c.seth(-30)
c.circle(-20,45)
c.end_fill()

c.color("black")
c.up()
c.home()
c.seth(0)
c.fd(550)
c.seth(90)
c.fd(240)


c.down()
c.begin_fill()
c.color("#cd805f","#cd805f")
c.seth(0)
c.fd(17)
c.seth(-10)
c.fd(30)
c.seth(90)
c.circle(46,180)
c.seth(10)
c.fd(30)
c.seth(0)
c.fd(17)
c.end_fill()

c.up()
c.color("black")
c.seth(0)
c.fd(17)
c.seth(-10)
c.fd(30)
c.seth(90)
c.circle(46,60)
c.down()
c.begin_fill()
c.color("brown","brown")
c.fd(30)
c.seth(-150)
c.fd(30)
c.seth(-20)
c.circle(78,40)
c.end_fill()

c.seth(150)
c.fd(30)
c.pensize(2)
c.begin_fill()
c.color("black","dark blue")
c.seth(180)
c.circle(-7,180)
c.seth(120)
c.fd(7)
c.seth(80)
c.fd(15)
c.seth(-80)
c.fd(15)
c.seth(-120)
c.fd(7)
c.seth(0)
c.circle(-7,180)
c.end_fill()


c.color('white')
c.up()
c.goto(-625,0)
c.pensize(5)
c.seth(90)
c.fd(199)
c.down()
c.seth(0)
c.fd(1250)
c.bk(1250)
c.up()
c.seth(180)
c.fd(2)
c.down()
for i in range(25):
    c.begin_fill()
    c.color("#c19973","brown")
    c.pensize(2)
    c.seth(90)
    c.fd(15)
    c.seth(0)
    c.fd(5)
    c.seth(-90)
    c.fd(15)
    c.seth(180)
    c.fd(5)
    c.end_fill()
    c.seth(90)
    c.fd(15)
    c.seth(0)
    c.fd(2.5)
    c.begin_fill()
    c.color("white","white")
    c.circle(2.5)
    c.end_fill()
    c.color("#c19973")
    c.seth(0)
    c.fd(2.5)
    c.seth(-90)
    c.fd(15)
    c.seth(180)
    c.fd(5)
    c.seth(0)
    c.fd(5)
    c.pensize(3)
    c.seth(90)
    c.fd(10)
    c.seth(50)
    c.fd(5)
    c.seth(-50)
    c.fd(5)
    c.seth(-90)
    c.fd(10)

    c.seth(90)
    c.fd(10)
    c.seth(50)
    c.fd(5)
    c.seth(-50)
    c.fd(5)
    c.seth(-90)
    c.fd(10)

    c.seth(90)
    c.fd(10)
    c.seth(50)
    c.fd(5)
    c.seth(-50)
    c.fd(5)
    c.seth(-90)
    c.fd(10)

    c.seth(90)
    c.fd(10)
    c.seth(50)
    c.fd(5)
    c.seth(-50)
    c.fd(5)
    c.seth(-90)
    c.fd(10)

    c.seth(90)
    c.fd(10)
    c.seth(50)
    c.fd(5)
    c.seth(-50)
    c.fd(5)
    c.seth(-90)
    c.fd(10)

    c.seth(90)
    c.fd(10)
    c.seth(50)
    c.fd(5)
    c.seth(-50)
    c.fd(5)
    c.seth(-90)
    c.fd(10)

    c.seth(90)
    c.fd(10)
    c.seth(50)
    c.fd(5)
    c.seth(-50)
    c.fd(5)
    c.seth(-90)
    c.fd(10)

c.begin_fill()
c.color("#c19973","brown")
c.pensize(2)
c.seth(90)
c.fd(15)
c.seth(0)
c.fd(5)
c.seth(-90)
c.fd(15)
c.seth(180)
c.fd(5)
c.end_fill()
c.seth(90)
c.fd(15)
c.seth(0)
c.fd(2.5)
c.begin_fill()
c.color("white","white")
c.circle(2.5)
c.ht()
c.end_fill()
turtle.done()