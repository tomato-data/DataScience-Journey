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
pygame.display.set_caption("Python Game")

# FPS
clock = pygame.time.Clock()

game_font = pygame.font.Font(None, 40)
game_result = ''

# 사용자 게임 초기화 (배경화면, 게임 이미지, 좌표, 폰트, 속도 등)
background = pygame.image.load("/Users/lofichill/Desktop/python/study/nado coding/applied python/pygame_basic/background.png")

character = pygame.image.load("/Users/lofichill/Desktop/python/study/nado coding/applied python/pygame_basic/jerry_70.png")
character_size = character.get_rect().size
character_width = character_size[0]
character_height = character_size[1]
character_x_pos = (screen_width / 2) - (character_width / 2)
character_y_pos = screen_height - character_height

to_x = 0
character_speed = 5

# enemy
enemy = pygame.image.load("/Users/lofichill/Desktop/python/study/nado coding/applied python/pygame_basic/tom_70.png")
enemy_size = enemy.get_rect().size
enemy_width = enemy_size[0]
enemy_height = enemy_size[1]
enemy_x_pos = randint(0, screen_width - enemy_width)
enemy_y_pos = 0
enemy_speed = 3

score = 0

# event loop
running = True
while running:
    dt = clock.tick(60) # fps 설정
    # 이벤트 처리
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

    # character postion definition
    character_x_pos += to_x
    if character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width:
        character_x_pos = screen_width - character_width

    # 계속해서 떨어지는 적
    enemy_y_pos += enemy_speed
    if enemy_y_pos > screen_height:
        score += 10
        enemy_y_pos = 0
        enemy_x_pos = randint(0, screen_width - enemy_width)

    # collision
    character_rect = character.get_rect()
    character_rect.left = character_x_pos
    character_rect.top = character_y_pos

    enemy_rect = enemy.get_rect()
    enemy_rect.left = enemy_x_pos
    enemy_rect.top = enemy_y_pos

    if character_rect.colliderect(enemy_rect):
        print("colided")
        game_result = 'Game Over'
        running = False

    screen.blit(background, (0, 0))
    screen.blit(character, (character_x_pos, character_y_pos))
    screen.blit(enemy, (enemy_x_pos, enemy_y_pos))
    score_txt = game_font.render("score: {}".format(score), True, (0, 0, 0))
    screen.blit(score_txt, (10, 10))
    
    pygame.display.update()
    

msg = game_font.render(game_result, True, (255, 0, 0))
msg_rect = msg.get_rect(center = (int(screen_width / 2), int(screen_width / 2)))
screen.blit(msg, msg_rect)

pygame.display.update()
pygame.time.delay(2000)

pygame.quit()