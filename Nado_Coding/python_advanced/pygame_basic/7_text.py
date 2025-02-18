import pygame

pygame.init() # 초기화

# 화면 크기 설정
screen_width = 1080 # 가로
screen_height = 800 # 세로
screen = pygame.display.set_mode((screen_width, screen_height))

# title
pygame.display.set_caption("Nado Game")

# FPS
clock = pygame.time.Clock()

# background
background = pygame.image.load("/Users/lofichill/Desktop/python/study/nado coding/applied python/pygame_basic/45908.jpg")

# import character
character = pygame.image.load("/Users/lofichill/Desktop/python/study/nado coding/applied python/gui_basic/check.png")
character_size = character.get_rect().size # image 크기
character_width = character_size[0]
character_height = character_size[1]
character_x_pos = (screen_width / 2) - (character_width / 2) # 화면 가로의 절반 크기
character_y_pos = screen_height - character_height # 화면 세로크기 가장 아래

# moving axis
to_x = 0
to_y = 0

# movement speed
character_speed = 0.6

# enemy character
enemy = pygame.image.load("/Users/lofichill/Desktop/python/study/nado coding/applied python/gui_basic/check.png")
enemy_size = enemy.get_rect().size # image 크기
enemy_width = enemy_size[0]
enemy_height = enemy_size[1]
enemy_x_pos = (screen_width / 2) - (enemy_width / 2) # 화면 가로의 절반 크기
enemy_y_pos = (screen_height / 2) - (enemy_height / 2) # 화면 세로크기 가장 아래

# font definition
game_font = pygame.font.Font(None, 40) # default font, size

# total time
total_time = 10

# 시작시간 정보
start_ticks = pygame.time.get_ticks() # 시작 tick 정보


# event loop
running = True # is the game running?
while running:
    dt = clock.tick(60) # fps 설정
    # print(clock.get_fps()) # fps 확인

    # 캐릭터가 100만큼 이동해야함
    # 10fps: 1초에 10번 동작 -> 10 * 10 = 100
    # 20fps: 1초에 20번 동작 -> 5 * 20 = 100

    for event in pygame.event.get(): # 어떤 이벤트가 발생 하였는가
        if event.type == pygame.QUIT: # 창이 닫히는 이벤트가 발생하였는가
            running = False # 게임이 진행중이 아님

        if event.type == pygame.KEYDOWN: # 키가 눌러졌는지 확인
            if event.key == pygame.K_LEFT:
                to_x -= character_speed
            elif event.key == pygame.K_RIGHT:
                to_x += character_speed
            elif event.key == pygame.K_UP:
                to_y -= character_speed
            elif event.key == pygame.K_DOWN:
                to_y += character_speed
        
        if event.type == pygame.KEYUP: # 방향키를 떼면 멈춤
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                to_y = 0

    character_x_pos += to_x * dt
    character_y_pos += to_y * dt

    # 가로 경계값 처리
    if character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width:
        character_x_pos = screen_width - character_width
    
    # 세로 경계값 처리
    if character_y_pos < 0:
        character_y_pos = 0
    elif character_y_pos > screen_height - character_height:
        character_y_pos = screen_height - character_height
    
    # 충돌 처리를 위한 rect 정보 업데이트
    character_rect = character.get_rect()
    # 화면상 캐릭터 위치로 업데이트
    character_rect.left = character_x_pos
    character_rect.top = character_y_pos

    enemy_rect = enemy.get_rect()
    enemy_rect.left = enemy_x_pos
    enemy_rect.top = enemy_y_pos

    # 충돌 체크
    if character_rect.colliderect(enemy_rect):
        print("충돌 했어요")
        running = False

    # screen.fill((0, 0, 255)) # RGB 값으로 배경 채우기
    screen.blit(background, (0, 0))
    screen.blit(character, (character_x_pos, character_y_pos)) # 캐릭터 그리기
    screen.blit(enemy, (enemy_x_pos, enemy_y_pos)) # 적 그리기

    # timer
    # elapsed time calculated
    elapsed_time = (pygame.time.get_ticks() - start_ticks) / 1000  # ms to seconds

    timer = game_font.render(str(int(total_time - elapsed_time)), True, (255, 255, 255))
    # int = 소수점 배제 (출력할 글자, True, 글자 색상)
    screen.blit(timer, (10, 10))

    # 시간 0 이하면 종료
    if total_time - elapsed_time <= 0:
        print("time out")
        running = False

    pygame.display.update() # 게임화면 다시 그리기
    
# 잠시 대기
pygame.time.delay(2000) # 2초 대기

# pygame 종료
pygame.quit()