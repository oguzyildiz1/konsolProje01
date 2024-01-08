import turtle

turtle.speed() 
print(turtle.position())

turtle.color('red') # kafa çizimi
turtle.fillcolor('yellow')
turtle.begin_fill()
for i in range(8): # yedigen #kafa uzunluğu 100
    turtle.forward(50)
    turtle.left(45)
turtle.end_fill()

turtle.penup()
turtle.goto(0,20)
turtle.pendown()
turtle.fillcolor('lightblue') #ağız çizimi
turtle.begin_fill()
for i in range(2): 
    turtle.forward(50)
    turtle.left(90)
    turtle.forward(10)
    turtle.left(90)
turtle.end_fill()

# gövde çizimi
turtle.penup()
turtle.goto(50,0)
turtle.pendown()
turtle.fillcolor('red')
turtle.begin_fill()
turtle.left(90)
turtle.backward(40) #boyun ölçütü
turtle.right(100)
turtle.forward(120) #omuz
turtle.right(80)
turtle.forward(200) #kol uzunluğu
turtle.right(90)
turtle.forward(40) #bilek 
turtle.right(85) # açı bilek
turtle.forward(150) #iç kol uzunluğu
#turtle.left(350)
turtle.left(170) 
turtle.forward(150) #bel ölçüsü
turtle.right(85)
print("son bitiş position: ",turtle.position())
turtle.penup()

## test starts 
turtle.goto(50,0)
turtle.pendown()
turtle.forward(50)
## test ends
#turtle.goto(0,0)
#turtle.pendown()
turtle.left(90)
turtle.forward(40) #boyun uzunluğu
turtle.right(80) #10 derece eğim verildi
turtle.forward(120) #boyun uzunluğu
turtle.right(280)
turtle.forward(200) #kol uzun
turtle.left(90)
turtle.forward(40) #bilek uzunluğu
turtle.left(85) 
turtle.forward(150) #iç kol
turtle.right(170)
turtle.forward(150)
turtle.left(85)
turtle.forward(154.06)
turtle.end_fill()

#göz çizimi 1
turtle.color('gray')
turtle.fillcolor('white')
turtle.begin_fill()
turtle.penup()
turtle.goto(0,75) #1. gözün yeri
turtle.pendown()
r = 10
turtle.circle(r)
turtle.end_fill()

#göz çizimi 2
turtle.begin_fill()
turtle.penup()
turtle.goto(50,75) #2. gözün yeri
turtle.pendown()
r = 10
turtle.circle(r)
turtle.end_fill()

#göz içleri 1
turtle.color('gray')
turtle.fillcolor('blue') # mavi göz
turtle.begin_fill()
turtle.penup()
turtle.goto(0,80) #1. gözün içi r=5'e göre position
turtle.pendown()
r = 5
turtle.circle(r)
turtle.end_fill()

turtle.begin_fill()
turtle.penup()
turtle.goto(50,80) #1. gözün içi r=5'e göre position
turtle.pendown()
r = 5
turtle.circle(r)
turtle.end_fill()

turtle.mainloop()

#yapılacak: gözler ve renkler


''' Önemli bilgiler'''
#hipotenüs 50 ise diğer kenar 36


# turtle.right(90)
# turtle.forward(100) #omuz
# turtle.right(45)
# turtle.forward(50)#omuz
# turtle.right(45)
# turtle.forward(200)
print(turtle.position())

input()