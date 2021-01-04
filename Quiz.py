import pygame
import random

pygame.init() #초기화 (반드시 필요)

#---------------------------------------화면 크기 설정
screen_width = 480 #가로 크기
screen_height = 640 #세로 크기
screen = pygame.display.set_mode((screen_width, screen_height))

#---------------------------------------화면 타이틀 설정
pygame.display.set_caption("Quiz") #게임 이름

#---------------------------------------FPS
clock = pygame.time.Clock()

# 1. 사용자 게임 초기화 (배경화면, 게임 이미지, 좌표, 속도, 폰트 등)

#---------------------------------------배경이미지 불러오기
background = pygame.image.load("C:\\Users\\user\\Desktop\\파이썬 공부\\python game\\background1.jpg")

#---------------------------------------스프라이트(캐릭터) 불러오기
character = pygame.image.load("C:\\Users\\user\\Desktop\\파이썬 공부\\python game\\character.png")
character_size = character.get_rect().size #이미지의 크기를 구해옴
character_width = character_size[0] #캐릭터의 가로 크기
character_height = character_size[1] #캐릭터의 세로 크기
character_x_pos = (screen_width / 2) - (character_width / 2) #화면 가로의 절반 크기에 해당하는 곳에 위치(가로위치)
character_y_pos = screen_height - character_height #화면 세로 크기 가장 아래에 해당하는 곳에 위치(세로위치)

#---------------------------------------이동할 좌표
to_x = 0

#---------------------------------------캐릭터 이동 속도
character_speed = 0.6

#---------------------------------------똥 만들기
ddong = pygame.image.load("C:\\Users\\user\\Desktop\\파이썬 공부\\python game\\enemy.png")
ddong_size = ddong.get_rect().size #이미지의 크기를 구해옴
ddong_width = ddong_size[0] #똥의 가로 크기
ddong_height = ddong_size[1] #똥의 세로 크기
ddong_x_pos = random.randint(0, screen_width - ddong_width) #화면 가로의 절반 크기에 해당하는 곳에 위치(가로위치)
ddong_y_pos = 0 #화면 세로 크기 가장 아래에 해당하는 곳에 위치(세로위치)
ddong_speed = 10

#---------------------------------------폰트 정의
game_font = pygame.font.Font(None, 40) #폰트 객체 생성(폰트, 크기)

#---------------------------------------총 시간
total_time = 10

#---------------------------------------시간 계산
start_ticks = pygame.time.get_ticks() #시작tick을 받아옴

#---------------------------------------이벤트 루프
running = True #게임이 진행중인가?
while running:
    dt = clock.tick(60) #게임화면의 초당 프레임 수를 설정

    # 2. 이벤트 처리 (키보드, 마우스 등)

    for event in pygame.event.get(): #어떤 이벤트가 발생하였는가?
        if event.type == pygame.QUIT: #창이 닫히는 이벤트가 발생하였는가?
            running = False #게임이 진행중이 아님

        if event.type == pygame.KEYDOWN: #키가 눌러졌는지 확인
            if event.key == pygame.K_LEFT: #캐릭터를 왼쪽으로
                to_x -= character_speed 
            elif event.key == pygame.K_RIGHT: #캐릭터를 오른쪽으로
                to_x += character_speed

        if event.type == pygame.KEYUP: #방향키를 떼면 멈춤
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0

    # 3. 게임 캐릭터 위치 정의

    character_x_pos += to_x * dt #-면 왼쪽 +면 오른쪽

#----------------------------------------가로 경계값 처리
    if character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width:
        character_x_pos = screen_width - character_width

#----------------------------------------세로 경계값 처리
    if character_y_pos < 0:
        character_y_pos = 0
    elif character_y_pos > screen_height - character_height:
        character_y_pos = screen_height - character_height
    
    ddong_y_pos += ddong_speed
    
    if ddong_y_pos > screen_height:
        ddong_y_pos = 0
        ddong_x_pos = random.randint(0, screen_width - ddong_width)

# 4. 충돌 처리

#----------------------------------------충돌 처리를 위한 rect 정보 업데이트
    character_rect = character.get_rect()
    character_rect.left = character_x_pos
    character_rect.top = character_y_pos

    ddong_rect = ddong.get_rect()
    ddong_rect.left = ddong_x_pos
    ddong_rect.top = ddong_y_pos

#----------------------------------------충돌 체크
    if character_rect.colliderect(ddong_rect):
      print("충돌 했어요")
      running = False

# 5. 화면에 그리기

#----------------------------------------배경 그리기
    screen.blit(background, (0, 0))

#----------------------------------------캐릭터 그리기
    screen.blit(character, (character_x_pos, character_y_pos))

#----------------------------------------적 캐릭터 그리기
    screen.blit(ddong, (ddong_x_pos, ddong_y_pos))

#----------------------------------------타이머 집어 넣기, 경과 시간 계산
    elapsed_time = (pygame.time.get_ticks() - start_ticks) / 1000 #경과시간(ms)을 1000으로 나눠서 초(s) 단위로 표시
    timer = game_font.render(str(int(total_time - elapsed_time)), True, (255, 255, 255)) #출력할 글자, True, 글자 색상

#----------------------------------------타이머 그리기
    screen.blit(timer, (10, 10))

#----------------------------------------시간이 0 이하면 게임 종료
    if total_time - elapsed_time <= 0:
        print("타임 아웃")
        running = False

#----------------------------------------게임화면 다시 그리기
    pygame.display.update()

#----------------------------------------잠시 대기
pygame.time.delay(1000) #1초 정도 대기(ms)

#----------------------------------------pygame 종료
pygame.quit() 