import pygame
from random import *

pygame.init() # 初期設定

# 画面サイズ設定
screen_width = 630 # よこの長さ
screen_height = 500 # たての長さ
screen = pygame.display.set_mode((screen_width, screen_height))

background = pygame.image.load("/Users/lofichill/Desktop/python/study/nado coding/applied python/pygame_basic/background.png") # ファイルの経路を入れる

character = pygame.image.load("/Users/lofichill/Desktop/python/study/nado coding/applied python/pygame_basic/jerry_70.png") # ファイルの経路を入れる
character_size = character.get_rect().size # イメージのサイズ
character_width = character_size[0] # よこの長さをセーブ
character_height = character_size[1] # たての長さセーブ
character_x_pos = (screen_width / 2) - (character_width / 2) # 画面の横の長さの半ばのところに入れるための計算
character_y_pos = screen_height - character_height # 画面の下の部分に来るようにするための計算
character_speed = 5
to_x = 0

enemy = pygame.image.load("/Users/lofichill/Desktop/python/study/nado coding/applied python/pygame_basic/tom_70.png")
enemy_size = enemy.get_rect().size # イメージのサイズ
enemy_width = enemy_size[0]
enemy_height = enemy_size[1]
enemy_x_pos = randint(0, screen_width - enemy_width)
enemy_y_pos = 0
enemy_speed = 3

score = 0

game_font = pygame.font.Font(None, 40)
game_result = ''

# タイトル
pygame.display.set_caption("") # 好きななまえをつける

# fps設定
clock = pygame.time.Clock()

# イベントループ
running = True
while running: # ゲームが動いているかを確認
    dt = clock.tick(60) # fps設定
    for event in pygame.event.get(): # どのようなイベントが起こったかを確認
        if event.type == pygame.QUIT: # ウィンドウの「X」ボタンを押しましたか？
            running = False # ゲームを終了しました

    if event.type == pygame.KEYDOWN: # キーを押していますか？
        if event.key == pygame.K_LEFT:
            to_x -= character_speed
        elif event.key == pygame.K_RIGHT:
            to_x += character_speed

    if event.type == pygame.KEYUP: # キーを押していない時には止まるように設定
        if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
            to_x = 0

    # キャラクターの位置を変化する計算
    character_x_pos += to_x

    if character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width:
        character_x_pos = screen_width - character_width

    enemy_y_pos += enemy_speed
    if enemy_y_pos > screen_height:
        score += 10
        enemy_y_pos = 0
        enemy_x_pos = randint(0, screen_width - enemy_width)

    character_rect = character.get_rect()
    character_rect.left = character_x_pos
    character_rect.top = character_y_pos

    enemy_rect = enemy.get_rect()
    enemy_rect.left = enemy_x_pos
    enemy_rect.top = enemy_y_pos

    if character_rect.colliderect(enemy_rect):
        print("충돌 했어요")
        game_result = 'Game Over'
        running = False

    screen.blit(background, (0, 0)) # 画面に描く
    screen.blit(character, (character_x_pos, character_y_pos)) # キャラクターを指定した位置に描く
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