import play
import pygame
from random import randint
play.set_backdrop((51,186,34))

N=0
schet = play.new_text(words="Очки {}".format(str(N)),y=200,x=-100)
STATUS=1
def start():
    bird.start_physics(can_move=True,y_speed=5, bounciness=0.1, obeys_gravity=False)
gameovertext = play.new_text(
    words="gameover",
    x = 0,
    y = 0,
    font_size=90,
    color="red")

gameoverbutton = play.new_circle(color="red",x=0,y=-50,radius=30)
restartbutton = play.new_circle(color="green",x=0,y=-140,radius=30)
restartbutton.hide()
gameoverbutton.hide()
gameovertext.hide()
@restartbutton.when_clicked
def do2():
    global STATUS
    STATUS=1
    # bird.stop_physics()
    bird.show()
    # gameovertext.hide()
    # gameoverbutton.hide()
    # restartbutton.hide()
    # bird.y = 0
    # start()
@gameoverbutton.when_clicked
def do():
    exit()


def gameover():
    global trubas
    '''Красная кнопка это кнопка выхода'''
    for truba in trubas:
        truba[0].remove()
        truba[1].remove()
    trubas = []
    bird.stop_physics()
    bird.hide()
    schet.hide()
    gameovertext.show()
    gameoverbutton.show()
    restartbutton.show()


def draw_truba(y_truba,rast):
    x_truba = 500
    delta = 500
    truba = play.new_image(
    x = x_truba,
    y = y_truba + rast,
    image="/img/truba2.png",
    size=3000,
    transparency = 50)
    truba2 = play.new_image(
    x = x_truba,
    y = y_truba-delta,
    image="/img/truba1.png",
    size=3000,
    transparency = 50)
    return truba, truba2

bird = play.new_image(
    image = "/img/birdanimation0.png",
    x = -300,
    y = 0,
    size=150)
bird.start_physics(can_move=True,y_speed=10, bounciness=0.1, obeys_gravity=False)
    
trubas = []

@play.repeat_forever
async def draw():
    global N
    if STATUS==1:
        N+=1
        schet.words="Очки {}".format(str(N)) 
        y_truba = randint(50,400)
        rast =  randint(50,100)
        trubas.append(draw_truba(y_truba,rast))
        await play.timer(seconds=2)


@play.repeat_forever
def run():
    if STATUS==1:
        for truba in trubas:
            truba[0].x-=4
            truba[1].x-=4
            if truba[0].x<=-500:
                truba[1].remove()
                truba[0].remove()
                trubas.remove(truba)

costims = ["/img/birdanimation0.png","/img/birdanimation1.png","/img/birdanimation2.png"]
@play.repeat_forever
async def editcostim():
    if STATUS==1:
        for costim in costims:
            bird.image=costim
            await play.timer(0.5)

@play.repeat_forever
def jumb():
    if STATUS==1:
        if play.key_is_pressed("space"):
            bird.physics.y_speed = 50
        else: 
            bird.physics.y_speed = -20
    
@play.repeat_forever
def toching():
    global STATUS
    if STATUS==1:
        for truba in trubas:
            if bird.is_touching(truba[0]) or bird.is_touching(truba[1]):
                STATUS=0
                gameover()
    
play.start_program()
    
