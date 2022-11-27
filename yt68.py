
from turtle import *


def Homer():
    tShirt()
    mouth()
    rightEye()
    face()
    eyePositioning()
    leftEye()
    ear()
    hairs()


def rightEye():
    pensize(3)
    pu()
    home()
    pd()
    pensize(3)
    color("black", "white")
    begin_fill()
    circle(80)
    end_fill()
    lt(90)
    pu()
    fd(74)
    pd()
    pensize(4)
    circle(2)


def eyePositioning():
    pu()
    home()
    bk(120)
    pd()


def leftEye():
    pensize(3)
    color("black", "white")
    begin_fill()
    circle(80)
    end_fill()
    lt(90)
    pu()
    fd(74)
    lt(90)
    fd(49)
    pd()
    pensize(4)
    circle(2)
    pensize(3)


def face():
    # creates nose and face
    pensize(3)
    pu()
    home()
    color('black', '#fef00e')
    begin_fill()
    bk(54)
    lt(90)
    fd(30)
    rt(90)
    pd()
    rt(8)
    i = 0
    a = 0

    while i < 50:
        fd(1.4)
        lt(0.2)
        i += 1

    while a < 40:
        fd(0.9)
        rt(0.1)
        a += 1

    b = 0
    while b < 40:
        fd(2)
        rt(4)
        b += 1

    rt(20)
    fd(8)

    c = 0
    while c < 20:
        fd(3.4)
        lt(0.7)
        c += 1

    d = 0
    while d < 10:
        fd(8.4)
        lt(0.7)
        d += 1

    e = 0
    while e < 60:
        fd(5.3)
        lt(3.0)
        e += 1

    rt(110)
    a = 0
    while a < 20:
        fd(3.2)
        lt(0.6)
        a += 1

    rt(40)
    fd(52)
    rt(110)
    fd(100)
    lt(50)

    a = 0
    while a < 50:
        fd(5.3)
        rt(1.3)
        a += 1

    rt(70)
    fd(12)
    lt(40)
    fd(100)

    a = 0
    while a < 30:
        fd(2.3)
        lt(1.0)
        a += 1

    a = 0
    while a < 10:
        fd(14.3)
        rt(2.0)
        a += 1

    a = 0
    while a < 51:
        fd(11.3)
        rt(3.3)
        a += 1

    a = 0
    while a < 22:
        fd(3.3)
        rt(0.5)
        a += 1

    lt(60)

    a = 0
    while a < 5:
        fd(6.5)
        rt(18.3)
        a += 1

    rt(90)
    circle(80, 152)
    end_fill()

    lt(20)
    fd(5)
    lt(20)
    fd(2)
    lt(20)
    fd(2)

    end_fill()

    pu()
    home()
    pd()


def mouth():
    pensize(3)
    pu()
    home()
    goto(62, -28)

    color("black", "#cdb26f")
    begin_fill()
    rt(58)
    pd()
    a = 0
    while a < 5:
        fd(5.3)
        rt(0.3)
        a += 1

    a = 0
    while a < 5:
        fd(5.3)
        rt(0.7)
        a += 1

    rt(18)
    fd(30)
    lt(14)

    a = 0
    while a < 8:
        fd(5.3)
        rt(0.7)
        a += 1

    a = 0
    while a < 4:
        fd(5.3)
        rt(30)
        a += 1

    lt(34)

    while a < 11:
        fd(26.3)
        rt(6.7)
        a += 1

    fd(22.3)
    rt(6.7)
    lt(90)
    fd(6)
    bk(12)
    fd(6)
    lt(96)
    fd(22.3)
    lt(6.7)

    a = 0
    while a < 5:
        fd(26.3)
        lt(6.7)
        a += 1

    rt(110)

    a = 0
    while a < 3:
        fd(16)
        rt(26)
        a += 1

    fd(13)
    lt(38)
    a = 0
    while a < 16:
        fd(23)
        rt(13)
        a += 1

    a = 0
    while a < 6:
        fd(13)
        lt(2.4)
        a += 1

    end_fill()


def tShirt():
    pensize(3)
    pu()
    home()
    goto(-29, -313)
    pd()
    lt(100)

    a = 0
    while a < 20:
        fd(3.2)
        rt(0.6)
        a += 1

    color('black', 'white')
    begin_fill()
    fd(3)
    rt(118)
    fd(41)
    rt(92)
    fd(65)
    end_fill()

    lt(130)
    color('black', 'white')
    begin_fill()
    a = 0
    while a < 9:
        fd(8.2)
        rt(10.6)
        a += 1

    lt(180)
    a = 0
    while a < 5:
        fd(18.6)
        lt(4.4)
        a += 1
    end_fill()

    pu()

    goto(-124, -286)

    color('black', 'white')
    begin_fill()
    lt(110)
    pd()
    a = 0

    while a < 5:
        fd(19.6)
        lt(4.4)
        a += 1

    rt(90)
    a = 0
    while a < 11:
        fd(25.0)
        rt(3.4)
        a += 1

    rt(85)

    a = 0
    while a < 3:
        fd(21.3)
        rt(1.4)
        a += 1

    end_fill()


def ear():
    pensize(3)
    pu()
    home()
    goto(-289, -30)
    color('black', '#fef00e')
    begin_fill()
    lt(230)
    pd()

    a = 0
    while a < 45:
        fd(3.3)
        rt(6.4)
        a += 1

    end_fill()
    pu()
    home()
    goto(-320, -10)
    pd()
    lt(18)

    a = 0
    while a < 5:
        fd(3.8)
        rt(0.8)
        a += 1

    a = 0
    while a < 5:
        bk(3.8)
        rt(0.8)
        a += 1

    lt(90)
    fd(6)
    a = 0
    while a < 5:
        bk(3.8)
        rt(1.6)
        a += 1


def hairs():
    pensize(4)
    pu()
    home()
    goto(-370, 10)
    pd()

    lt(100)
    fd(100)
    rt(158)
    fd(100)
    lt(155)
    fd(100)
    rt(155)
    fd(100)

    pu()
    home()

    goto(-150, 378)
    pd()
    lt(140)
    a = 0
    while a < 10:
        fd(13.8)
        lt(12.6)
        a += 1

    pu()
    home()

    goto(-220, 373)
    pd()

    lt(140)
    a = 0
    while a < 13:
        fd(13.8)
        lt(12.6)
        a += 1


Homer()
done()