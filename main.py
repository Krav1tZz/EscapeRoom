import pygame
from pygame import *
import sys
import math
import time



pygame.init()


WIDTH, HEIGHT = 1280, 720


pygame.display.set_mode((WIDTH, HEIGHT))



WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (128, 128, 128)
fps = 60
background = pygame.transform.scale(pygame.image.load("classroom.png"), (WIDTH, HEIGHT))


screen = pygame.display.set_mode((WIDTH, HEIGHT), HWSURFACE | DOUBLEBUF | RESIZABLE)
current_size = screen.get_size()
last_size = current_size
pygame.display.set_caption("Escape Room Puzzle Game")


classroom_image = pygame.image.load("classroom.png")
hall = pygame.image.load("hall.png")
stairs = pygame.image.load("stairs.png")
hall2 = pygame.image.load("hall2.png")
desk = pygame.image.load('desk.png')
outside = pygame.image.load('wagner.png')
screen.blit(pygame.transform.scale(classroom_image, (WIDTH, HEIGHT)), (0, 0))
classroom_rect = classroom_image.get_rect(center=(WIDTH // 2, HEIGHT // 2))

popups = []
screen_id = 1
trigger_points = []
key_unlocked = False
doorkey_unlocked = False
doorkey_unlocked2 = False
def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)


def show_start_screen():
    global popups
    global screen_id
    global trigger_points
    global key_unlocked
    global doorkey_unlocked
    global doorkey_unlocked2
    
    popups = []
    screen_id = 1
    trigger_points = [[100, 100, 50, 50, podskazka1], [200, 300, 40, 90, podskazka2]]
    key_unlocked = False
    doorkey_unlocked = False
    screen.fill(WHITE)
    draw_text("Escape Room Puzzle Game", pygame.font.Font('FreeSans.ttf', 48), (0, 0, 0), screen, 200, 100)
    draw_text("Press Any key to start", pygame.font.Font('FreeSans.ttf', 24), (0, 0, 0), screen, 220, 300)
    pygame.display.flip()
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYUP:
                waiting = False



def podskazka1():
    global key_unlocked
    global popups
    key_unlocked = True
    popups.append([[300, 200], 'You find a key to open the door', 3])
    print('podskazka 1')

def verh():
    global trigger_points
    global screen_id
    global popups
    popups = []
    screen_id = 4
    trigger_points = [[600, 600, 50, 50, show_start_screen]]
    
def vniz():
    global screen_id
    global popups
    global trigger_points
    popups = []
    screen_id = 5
    trigger_points = [[250, 500, 50, 200, door_vniz], [150, 300, 40, 40, desk1], [200, 200, 40, 40, man], [500, 500, 50, 20, vent]]

def door_vniz():
    global popups
    global screen_id
    global trigger_points
    
    if not doorkey_unlocked2:
        popups.append([[300,200], "Door closed, hmm... Something on the desk on the left", 3])
    else:
        screen_id = 7
    trigger_points = [[200,300, 50 ,50]]


def desk1():
    global popups
    global trigger_points
    global screen_id
    screen_id = 6
    popups.append([[500,200], "back to hall", 100000])
    trigger_points = [[200, 200, 50, 70, note], [500, 500, 50, 50, vniz]]

def note():
    global popups
    popups.append([[300,200], "STEAL KEY FROM MAN IN BLACK", 3])

def man():
    global popups
    popups.append([[300,200], "You found a note: DO NOT FORGET ABOUT SWIPE CARD IN VENTILATION", 5])
def vent():
    global popups
    global doorkey_unlocked2
    global trigger_points
    doorkey_unlocked2 = True
    popups.append([[300,200], "You finally found swipe card. RUN AWAY!", 3])

    




    

def podskazka3():
    global screen_id
    global trigger_points
    global doorkey_unlocked
    if not doorkey_unlocked:
        popups.append([[300,200], "Note on the door - key in the locker", 3])
    else:
        screen_id = 3
        trigger_points = [[300,300, 50,50, verh], [300, 500, 50, 50, vniz]]
        popups.append([[300, 500], "Go up", 10000])
        popups.append([[300,300],"Go down", 10000])
        
    # trigger_points = [[100, 100, 50, 50,], [200, 300, 40, 90, podskazka2]] 
    print('vernutsja obratno')
def doska():
    popups.append([[300,200], "Door on your left - exit", 3])
def podskazka4():
    global screen_id
    global trigger_points
    screen_id = 1
def skafcik():
    global doorkey_unlocked
    doorkey_unlocked = True
    popups.append([[300,200], "Key was found", 2])
    
def podskazka2():
    global screen_id
    global trigger_points
    global key_unlocked
    if key_unlocked:
        screen_id = 2
        trigger_points = [[100, 350, 130, 700, podskazka3], [490, 550, 40, 200, doska], [200, 900, 50, 50, skafcik]] #novije trigger pointi dlja novogo ekrana
    else:
        popups.append([[300, 200], 'You have no key', 3])

def predistorija():
    screen.fill(WHITE)
    draw_text("bla blabla", pygame.font.Font('FreeSans.ttf', 48), (0, 0, 0), screen, 200, 100)
    draw_text("bla bla bla", pygame.font.Font('FreeSans.ttf', 24), (0, 0, 0), screen, 220, 300)
    pygame.display.flip()
    for i in range(8):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        screen.fill(WHITE)
        draw_text("Cool story", pygame.font.Font('FreeSans.ttf', 48), (0, 0, 0), screen, 200, 100)
        draw_text("School was attacked by terrorists, but they left for pizza in Rimi, you have 30 minutes to escape from school!", pygame.font.Font('FreeSans.ttf', 24), (0, 0, 0), screen, 220, 300)
        draw_text(str(i // 4), pygame.font.Font('FreeSans.ttf', 24), (0, 0, 0), screen, 400, 600)
        pygame.display.flip()
        time.sleep(0.25)

def main():
    global trigger_points
    clock = pygame.time.Clock()
    running = True
    start_time = pygame.time.get_ticks()
    escape_time = 30 * 60 * 1000

    

    show_start_screen()
    predistorija()

    while running:
        
        current_time = pygame.time.get_ticks()
        elapsed_time = current_time - start_time
            
        if elapsed_time >= escape_time:
            screen.fill(WHITE)
            draw_text("Times up!", pygame.font.Font('FreeSans.ttf', 48), (255, 0, 0), screen, 250, 200)
            pygame.display.flip()
            pygame.time.wait(3000)  
            pygame.quit()
            sys.exit()

        screen.fill(WHITE)
        if screen_id == 1:
            screen.blit(pygame.transform.scale(classroom_image, screen.get_size()), (0, 0))
        elif screen_id == 2:
            screen.blit(pygame.transform.scale(hall, screen.get_size()), (0, 0))
        elif screen_id == 3:
            screen.blit(pygame.transform.scale(stairs, screen.get_size()), (0, 0))
        elif screen_id == 4:
            screen.fill(WHITE)
            draw_text("Upstairs someone throwed a grenade under your legs and you blowed up =(", pygame.font.Font('Freesans.ttf', 36), (0, 0, 0), screen, 200, 100)
            draw_text("New game", pygame.font.Font('Freesans.ttf', 36), (0, 0, 0), screen, 220, 300)
        elif screen_id == 5:
            screen.blit(pygame.transform.scale(hall2, screen.get_size()), (0, 0))
        elif screen_id == 6:
            screen.blit(pygame.transform.scale(desk, screen.get_size()), (0, 0))
        elif screen_id == 7:
            screen.blit(pygame.transform.scale(outside, screen.get_size()), (0, 0))

        
        #to check trigger points(delete later)
        for i in trigger_points:
            pygame.draw.rect(screen, (150, 0, 0), [round(i[0] / HEIGHT * screen.get_size()[0]), round(i[1] / WIDTH * screen.get_size()[1]), round(i[2] / HEIGHT * screen.get_size()[0]), round(i[3] / WIDTH * screen.get_size()[1])])

        if pygame.mouse.get_pressed()[0]:
            pos = pygame.mouse.get_pos()
            for i in trigger_points:
                i2 = [i[0] / HEIGHT * screen.get_size()[0], i[1] / WIDTH * screen.get_size()[1], i[2] / HEIGHT * screen.get_size()[0], i[3] / WIDTH * screen.get_size()[1]]
                if pos[0] > i2[0] and pos[0] < i2[0] + i2[2] and pos[1] > i2[1] and pos[1] < i2[1] + i2[3]:
                    i[4]()

        draw_text('Time left:', pygame.font.Font('FreeSans.ttf',36), WHITE, screen, 20, 100)
        draw_text("Quit", pygame.font.Font('FreeSans.ttf', 36), WHITE, screen, 20, 60)

        for i in range(len(popups)-1, -1, -1):
            draw_text(popups[i][1], pygame.font.Font('FreeSans.ttf', 36), WHITE, screen, round(popups[i][0][0] / WIDTH * screen.get_size()[1]), round(popups[i][0][1] / HEIGHT * screen.get_size()[1]))
            popups[i][2] -= 0.01
            if popups[i][2] < 0:
                popups.pop(i)

        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if pygame.Rect(20, 20, 200, 40).collidepoint(event.pos):
                    
                    print("Подсказка: ты лох ")
                elif pygame.Rect(20, 60, 200, 40).collidepoint(event.pos):
                    
                    print("Выход из класса")
                    running = False

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()