import pygame

pygame.init() # 초기화

# 화면 크기 설정
screen_width = 480 # 가로
screen_height = 640 # 세로
screen = pygame.display.set_mode((screen_width, screen_height))

# title
pygame.display.set_caption("Nado Game")

# background
background = pygame.image.load("/Users/lofichill/Desktop/python/study/nado coding/applied python/pygame_basic/45908.jpg")

# import character
character = pygame.image.load("/Users/lofichill/Desktop/python/study/nado coding/applied python/pygame_basic/character.jpg")
character_size = character.get_rect().size # image 크기
character_width = character_size[0]
character_height = character_size[1]
character_x_pos = (screen_width / 2) - (character_width / 2) # 화면 가로의 절반 크기
character_y_pos = screen_height - character_height # 화면 세로크기 가장 아래

# event loop
running = True # is the game running?
while running:
    for event in pygame.event.get(): # 어떤 이벤트가 발생 하였는가
        if event.type == pygame.QUIT: # 창이 닫히는 이벤트가 발생하였는가
            running = False # 게임이 진행중이 아님

    # screen.fill((0, 0, 255)) # RGB 값으로 배경 채우기
    screen.blit(background, (0, 0))
    screen.blit(character, (character_x_pos, character_y_pos)) # 캐릭터 그리기

    pygame.display.update() # 게임화면 다시 그리기
    

# pygame 종료
pygame.quit()