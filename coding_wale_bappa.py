# -*- coding: utf-8 -*-
"""
Created on Sat Sep 18 19:29:32 2021

@author: HOME
"""


import turtle
import math
import random

bob=turtle.Turtle()
bob.speed(1000)
bob.width(2)
bob.getscreen().bgcolor("#C0C0C0")

bob.penup()
bob.left(90)
bob.forward(200)
bob.right(90)
bob.pendown()


bob.begin_fill()
bob.forward(20)
bob.left(110)
for i in range(50):
    bob.forward(.5)
    bob.left(.7)
bob.left(120)
for i in range(41):
    bob.forward(.5)
    bob.right(.7)
bob.end_fill()

bob.penup()
bob.forward(7)
bob.pendown()


bob.begin_fill()
bob.forward(15)
bob.left(126)
bob.forward(60)
bob.left(156)
bob.forward(30)
bob.left(26)
bob.forward(25)
bob.end_fill()

bob.penup()
bob.back(90)
bob.left(270)
bob.backward(35)
bob.left(90)
bob.forward(20)
bob.pendown()

bob.width(4)#10
bob.right(30)
for i in range(30):
    bob.forward(3)
    bob.left(2)
bob.left(30)
for i in range(20):
    bob.left(1.5)
    bob.forward(1)
bob.left(86)
for i in range(20):
    bob.forward(3.8)
bob.left(60)
for i in range(33):
    bob.forward(.8)
    bob.left(4)
bob.left(-10)
bob.forward(28)


bob.penup()
bob.left(45)
bob.forward(100)
bob.right(160)
bob.forward(50)
bob.left(105)
bob.pendown()

bob.right(30)
for i in range(16):
    bob.forward(5)
    bob.left(5)
bob.left(40)
for i in range(20):
    bob.forward(5)
    bob.left(2)
bob.left(20)
for i in range(17):
    bob.forward(2)
    bob.left(3)


bob.penup()
bob.left(26.6)#28
bob.forward(165)
bob.pendown()



bob.right(20)#24
for i in range(16):
    bob.forward(5)
    bob.right(3)
bob.right(44)
for i in range(20):
    bob.forward(5)
    bob.right(2.9)
bob.right(17)
for i in range(17):
    bob.forward(2)
    bob.right(2.4)


bob.penup()
bob.right(33)
bob.forward(90)
bob.left(20)
bob.forward(20)
bob.right(40)

bob.left(30)#60
bob.forward(20)#20
bob.right(30)
bob.forward(30)#30
bob.right(90)
#bob.forward(20)
bob.left(90)
bob.pendown()


bob.width(4)#6
for i in range(50):#50
	bob.left(math.sin(i//10)*.2)#.5
	bob.back(.5)#.5
for i in range(26):#50
	bob.left(6)
	bob.back(1.5) #.5  
for i in range(27):#50
	bob.left(6)
	bob.forward(1.9) #.5 
for i in range(48):#50
	bob.left(math.sin(i//10)*.9)#.5
	bob.forward(.3)#.5 


bob.penup()
bob.goto(19,115)
bob.pendown()


bob.forward(10)


bob.penup()
bob.goto(19,100)#90
bob.pendown()


bob.width(20)######################################################
#bob.back(110)
'''for i in range(100):
	bob.left(2)
	bob.back(2.5)'''
bob.back(60)
for i in range(23):#25
	bob.right(-1)
	bob.back(7)

    
bob.penup()
bob.goto(69,20)
bob.pendown()


bob.begin_fill()
bob.width(4)
bob.begin_fill()
bob.circle(10)
bob.end_fill()
bob.end_fill()

bob.penup()
bob.goto(-9,20)
bob.pendown()


bob.begin_fill()
bob.circle(10)
bob.left(138)
for i in range(20):
    bob.right(3)
    bob.forward(2.4)
bob.right(158)
for i in range(10):
    bob.left(5)
    bob.forward(4)
#bob.right(90)#########################################
#bob.forward(10)####################################
bob.end_fill()

bob.penup()
bob.goto(22,-132)
bob.pendown()


bob.right(105)#100
bob.circle(100,70)
'''for i in range(50):
    bob.forward(2)
    bob.left(.3)'''


bob.penup()
bob.goto(-28,-19)
bob.pendown()

bob.left(90)
bob.right(45)
bob.left(-10)
bob.back(90)
for i in range(290):#250
    bob.left(.6)#.6
    bob.back(1)#1
for i in range(250):#200
    bob.right(.9)#.5#.9
    bob.back(1)#1
bob.back(40)
for i in range(180):#50
    bob.right(.5)#.5
    bob.back(.5)#.5


bob.penup()
bob.goto(128,-223)
bob.pendown()


for i in range(50):#50
    bob.left(.8)#.8
    bob.forward(1.2)#.9


bob.penup()
bob.goto(115,-223)#115,-223
bob.right(118)#118
bob.pendown()

  
bob.forward(40)
bob.left(135)
bob.forward(10)
bob.right(135)
bob.forward(20)
for i in range(137):#150
    bob.left(1.3)
    bob.forward(.6)
#bob.right(60)
bob.forward(35)


bob.penup()
bob.goto(-15,-250)#-219
bob.right(39)
bob.pendown()


bob.right(20)
bob.forward(35)
for i in range(100):
    bob.left(1.8)
    bob.forward(.6)
bob.left(30)
bob.forward(40)
for i in range(150):
    bob.left(-1.2)
    bob.forward(1.8)


bob.penup()
bob.goto(-60,-50)#-219
bob.left(81)
bob.pendown()


bob.forward(20)
bob.right(20)
bob.forward(18)
bob.left(145)
bob.forward(18)
bob.right(110)
bob.forward(20)
for i in range(100):
    bob.left(2)
    bob.forward(1)
bob.forward(30)
for i in range(50):
    bob.left(2.5)#2
    bob.forward(1.2)#1


bob.penup()
bob.goto(-10,10)#-219
#bob.left(81)
bob.pendown()


bob.begin_fill()
bob.circle(8.789)#8.8
bob.end_fill()

bob.penup()
bob.goto(-35,99.99)#
bob.left(126)
bob.right(119)
bob.left(40)#40
bob.left(30)#30
bob.pendown()


#bob.begin_fill()
#for i in range(50):
bob.back(22)#19
bob.left(90)
bob.forward(10)
bob.right(90)
bob.right(45)
bob.forward(10)
#bob.end_fill()


bob.penup()
bob.goto(55,88)#
#bob.left(126)
bob.right(20)
#bob.left(40)#40
#bob.left(30)#30
bob.pendown()


#bob.begin_fill()
bob.left(45)
bob.back(10)
bob.right(35)#40
bob.forward(7.7)
bob.right(45)########3
bob.forward(19)
bob.left(-10)
bob.back(24)
#bob.end_fill()


bob.penup()
bob.goto(99,-34)#
#bob.left(126)
#bob.right(20)
#bob.left(40)#40
#bob.left(30)#30
bob.pendown()


bob.right(90)
for i in range(55):
    bob.left(1.6)
    bob.forward(1)
bob.right(30)
bob.forward(20)
bob.right(10)
bob.forward(20)


bob.penup()
bob.back(60)
bob.pendown()

bob.begin_fill()
for i in range(50):
    bob.left(2.5)
    bob.forward(1)
bob.forward(20)
bob.left(90)
bob.forward(20)
for i in range(51):
    bob.left(2.5)
    bob.forward(1)
bob.end_fill()

# information printing
bob.penup()
bob.setpos(-250,250)
bob.pendown()
bob.pencolor('black')
bob.write('Happy Ganesh Chaturthi', font=("Arial",30, "bold"))
bob.penup()

bob.goto(-300,-200)
bob.pendown()
bob.write("Created by - Dilip Prasad")
bob.penup()
bob.ht()

turtle.done()
