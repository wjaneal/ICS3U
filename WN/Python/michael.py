from vpython import *
scene.width = 1280
scene.height = 720
scene.autoscale = 0
scene.range = (200,100,200)
scene.center = (0,50,0)
ball = sphere(pos=(0,100,0),radius=2)
ground = box(pos=(0,-1,0),size=(100,2,10))
building = box(size=(5,100,5),pos=(0,50,0),color=color.blue)
gravity = 9.8   
velocityX = 5   
seconds = 0
dt = .025
finished = False
while not finished:
    rate(100)
    seconds += dt
    ballY = 100 + 5*seconds-.5 * gravity * seconds**2
    ballX = velocityX * seconds
    ball.pos = vector(ballX,ballY,0)
    if ballY - 2 <= 0:
        finished = True
        #print ("seconds to drop: " + str(seconds))
        #print ("distance in the x direction: " + str(ballX))
seconds = 0
finished = false
while not finished:
    rate(100)
    seconds += dt
    ballY = 0 + 50*seconds-.5 * gravity * seconds**2
    ballX += velocityX
    ball.pos = vector(ballX,ballY,0)
    if ballY - 2 >= 200:
        finished = True

