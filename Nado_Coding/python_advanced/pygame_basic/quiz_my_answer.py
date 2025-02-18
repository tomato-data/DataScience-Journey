import pygame
from random import *
##########################################################
# 기본 초기화 (반드시 해야하는 것들)
pygame.init() # 초기화

# 화면 크기 설정
screen_width = 630 # 가로
screen_height = 500 # 세로
screen = pygame.display.set_mode((screen_width, screen_height))

# title
pygame.display.set_caption("Game Name")

# FPS
clock = pygame.time.Clock()
############################################################

# 사용자 게임 초기화 (배경화면, 게임 이미지, 좌표, 폰트, 속도 등)
background = pygame.image.load("/Users/lofichill/Desktop/python/study/nado coding/applied python/pygame_basic/background.png")

character = pygame.image.load("/Users/lofichill/Desktop/python/study/nado coding/applied python/pygame_basic/jerry_70.png")
character_size = character.get_rect().size
character_width = character_size[0]
character_height = character_size[1]
character_x_pos = (screen_width / 2) - (character_width / 2)
character_y_pos = screen_height - character_height 

to_x = 0
character_speed = 0.5

enemy = pygame.image.load("/Users/lofichill/Desktop/python/study/nado coding/applied python/pygame_basic/tom_70.png")
enemy_size = enemy.get_rect().size
enemy_width = enemy_size[0]
enemy_height = enemy_size[1]

enemy_x_pos = randint(0, screen_width - enemy_width)
enemy_y_pos = 0
enemy_speed = 3



# event loop
running = True
while running:
    dt = clock.tick(60) # fps 설정

    # 2. 이벤트 처리 (키보드, 마우스 등)
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN: # 키가 눌러졌는지 확인
            if event.key == pygame.K_LEFT:
                to_x -= character_speed
            elif event.key == pygame.K_RIGHT:
                to_x += character_speed
        
        if event.type == pygame.KEYUP: # 방향키를 떼면 멈춤
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0

    character_x_pos += to_x * dt

    if character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width:
        character_x_pos = screen_width - character_width

    # if event.type == pygame.KEYUP or event.type == pygame.KEYDOWN:
    enemy_y_pos += enemy_speed

    if enemy_y_pos == screen_height - enemy_height:
        enemy_x_pos = randint(0, screen_width - enemy_width)
        enemy_y_pos = 0

    character_rect = character.get_rect()
    character_rect.left = character_x_pos
    character_rect.top = character_y_pos

    enemy_rect = enemy.get_rect()
    enemy_rect.left = enemy_x_pos
    enemy_rect.top = enemy_y_pos

    if character_rect.colliderect(enemy_rect):
        print("충돌 했어요")
        running = False

    screen.blit(background, (0, 0))
    screen.blit(character, (character_x_pos, character_y_pos))
    screen.blit(enemy, (enemy_x_pos, enemy_y_pos))

    pygame.display.update()
    
pygame.quit()