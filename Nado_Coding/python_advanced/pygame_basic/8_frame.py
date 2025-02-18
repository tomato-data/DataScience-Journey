import pygame
from random import *
##########################################################
# 기본 초기화 (반드시 해야하는 것들)
pygame.init() # 초기화

# 화면 크기 설정
screen_width = 1080 # 가로
screen_height = 640 # 세로
screen = pygame.display.set_mode((screen_width, screen_height))

# title
pygame.display.set_caption("Game Name")

# FPS
clock = pygame.time.Clock()
##########################################################

# 사용자 게임 초기화 (배경화면, 게임 이미지, 좌표, 폰트, 속도 등) 
background = pygame.image.load("")

# event loop
running = True
while running:
    dt = clock.tick(30) # fps 설정
    
    for event in pygame.event.get(): # 어떤 이벤트가 발생 하였는가
        if event.type == pygame.QUIT: # 창이 닫히는 이벤트가 발생하였는가
            running = False # 게임이 진행중이 아님
    # 2. 이벤트 처리 (키보드, 마우스 등)

    pygame.display.update()
    
pygame.quit()