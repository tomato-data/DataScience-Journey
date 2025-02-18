import pygame

pygame.init() # 초기화

# 화면 크기 설정
screen_width = 1080 # 가로
screen_height = 640 # 세로
screen = pygame.display.set_mode((screen_width, screen_height))
game_over_font = pygame.font.Font('raanana.ttf', 40)

# title
pygame.display.set_caption("Game Name")

# FPS
clock = pygame.time.Clock()
##########################################################

# event loop
running = True
while running:
    dt = clock.tick(30) # fps 설정
    
    for event in pygame.event.get(): # 어떤 이벤트가 발생 하였는가
        if event.type == pygame.QUIT: # 창이 닫히는 이벤트가 발생하였는가
            running = False # 게임이 진행중이 아님
    # 2. 이벤트 처리 (키보드, 마우스 등)

    game_over_txt = game_over_font.render("Game Over", True, (0, 255, 0))
    screen.blit(game_over_txt, (10, 10))
    pygame.display.update()
    
pygame.quit()