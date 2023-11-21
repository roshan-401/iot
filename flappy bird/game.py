import pygame,sys
import serial
import time

arduino = serial.Serial(port='COM7', baudrate=115200, timeout=.1)

def draw_floor():
    screen.blit(floor_surface,(floor_x_pos,height-50))
    screen.blit(floor_surface,(floor_x_pos+width,height-50))
    
pygame.init()

#screen
width,height = 576/2,1024/2
screen = pygame.display.set_mode((width,height))
clock = pygame.time.Clock()


#game variables 
gravity = 0.25
bird_movement = 0

#floor
bg_surface = pygame.image.load('assets/background-day.png').convert()
# bg_surface = pygame.transform.scale2x(bg_surface)
floor_surface = pygame.image.load('assets/base.png').convert()
floor_x_pos = 0

#bird
bird_surface = pygame.image.load('assets/bluebird-midflap.png').convert()
# bird_surface = pygame.transform.scale2x(bird_surface)
bird_rect = bird_surface.get_rect(center=(50,height/2))

while True:
    #audrino code
    value = arduino.readline().decode().strip()
    # if value:
    #     print(value)
    # else:
    #     print("non")
    # time.sleep(0.1)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.blit(bg_surface,(0,0))

    bird_movement += gravity
    if value:
        value = min(max(0,int(value)*2),height)
        # print(bird_rect)
        bird_rect.centery = value
    screen.blit(bird_surface,bird_rect)
    floor_x_pos -= 1
    draw_floor()
    if floor_x_pos <= -1 * width:
        floor_x_pos = 0

    pygame.display.update()
    clock.tick(60)