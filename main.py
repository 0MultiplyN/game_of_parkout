import pygame
import os
import random
import sys
pygame.init()

# Global Constants
SCREEN_HEIGHT = 600
SCREEN_WIDTH = 1100
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

RUNNING = [pygame.image.load(os.path.join("Assets/turtle", "turtleRun1.png")),
           pygame.image.load(os.path.join("Assets/turtle", "turtleRun2.png"))]
JUMPING = pygame.image.load(os.path.join("Assets/turtle", "turtleJump.png"))
DUCKING = [pygame.image.load(os.path.join("Assets/turtle", "turtleDuck1.png")),
           pygame.image.load(os.path.join("Assets/turtle", "turtleDuck2.png"))]
DEAD = pygame.image.load(os.path.join("Assets/turtle", "turtleDead.png"))

STARTING = pygame.image.load(os.path.join("Assets/Dino", "DinoStart.png"))
RUNNING1 = [pygame.image.load(os.path.join("Assets/Chic", "ChickenRun1.png")),
           pygame.image.load(os.path.join("Assets/Chic", "ChickenRun2.png"))]
JUMPING1 = pygame.image.load(os.path.join("Assets/Chic", "ChickenJump.png"))
DUCKING1 = [pygame.image.load(os.path.join("Assets/Chic", "ChickenDuck1.png")),
           pygame.image.load(os.path.join("Assets/Chic", "ChickenDuck2.png"))]
DEAD1 = pygame.image.load(os.path.join("Assets/Chic", "ChickenDead.png"))

# RUNNING2 = [pygame.image.load(os.path.join("Assets/Alpaca", "AlpacaRun1.png")),
#            pygame.image.load(os.path.join("Assets/Alpaca", "AlpacaRun2.jpg"))]
# JUMPING2 = pygame.image.load(os.path.join("Assets/Alpaca", "AlpacaJump.png"))
# DUCKING2 = [pygame.image.load(os.path.join("Assets/Alpaca", "AlpacaDuck1.jpg")),
#            pygame.image.load(os.path.join("Assets/Alpaca", "AlpacaDuck2.jpg"))]
# DEAD2 = pygame.image.load(os.path.join("Assets/Alpaca", "AlpacaDie.jpg"))

RUNNING2 = [pygame.image.load(os.path.join("Assets/Alpaca", "AlpacaRun1.png")),
           pygame.image.load(os.path.join("Assets/Alpaca", "AlpacaRun2.png"))]
JUMPING2 = pygame.image.load(os.path.join("Assets/Alpaca", "AlpacaJump.png"))
DUCKING2 = [pygame.image.load(os.path.join("Assets/Alpaca", "AlpacaDuck1.png")),
           pygame.image.load(os.path.join("Assets/Alpaca", "AlpacaDuck2.png"))]
DEAD2 = pygame.image.load(os.path.join("Assets/Alpaca", "AlpacaStart.png"))

SMALL_CACTUS = [pygame.image.load(os.path.join("Assets/Cactus", "SmallCactus1.png")),
                pygame.image.load(os.path.join("Assets/Cactus", "SmallCactus2.png")),
                pygame.image.load(os.path.join("Assets/Cactus", "SmallCactus3.png"))]
LARGE_CACTUS = [pygame.image.load(os.path.join("Assets/Cactus", "LargeCactus1.png")),
                pygame.image.load(os.path.join("Assets/Cactus", "LargeCactus2.png")),
                pygame.image.load(os.path.join("Assets/Cactus", "LargeCactus3.png"))]

BIRD = [pygame.image.load(os.path.join("Assets/Bird", "Bird1.png")),
        pygame.image.load(os.path.join("Assets/Bird", "Bird2.png"))]

CLOUD = pygame.image.load(os.path.join("Assets/Other", "Cloud.png"))

BG = pygame.image.load(os.path.join("Assets/Other", "Track.png"))


class Dinosaur:
    X_POS = 80
    Y_POS = 310
    Y_POS_DUCK = 340
    JUMP_VEL = 8.5

    def __init__(self):
        self.duck_img = DUCKING
        self.run_img = RUNNING
        self.jump_img = JUMPING

        self.dino_duck = False
        self.dino_run = True
        self.dino_jump = False

        self.step_index = 0
        self.jump_vel = self.JUMP_VEL
        self.image = self.run_img[0]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.X_POS
        self.dino_rect.y = self.Y_POS

    def update(self, userInput):
        if self.dino_duck:
            self.duck()
        if self.dino_run:
            self.run()
        if self.dino_jump:
            self.jump()

        if self.step_index >= 10:
            self.step_index = 0

        if userInput[pygame.K_UP] and not self.dino_jump:
            self.dino_duck = False
            self.dino_run = False
            self.dino_jump = True
        elif userInput[pygame.K_DOWN] and not self.dino_jump:
            self.dino_duck = True
            self.dino_run = False
            self.dino_jump = False
        elif not (self.dino_jump or userInput[pygame.K_DOWN]):
            self.dino_duck = False
            self.dino_run = True
            self.dino_jump = False

    def duck(self):
        self.image = self.duck_img[self.step_index // 5]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.X_POS
        self.dino_rect.y = self.Y_POS_DUCK
        self.step_index += 1

    def run(self):
        self.image = self.run_img[self.step_index // 5]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.X_POS
        self.dino_rect.y = self.Y_POS
        self.step_index += 1

    def jump(self):
        self.image = self.jump_img
        if self.dino_jump:
            self.dino_rect.y -= self.jump_vel * 4
            self.jump_vel -= 0.8
        if self.jump_vel < - self.JUMP_VEL:
            self.dino_jump = False
            self.jump_vel = self.JUMP_VEL

    def draw(self, SCREEN):
        SCREEN.blit(self.image, (self.dino_rect.x, self.dino_rect.y))

class Chicken:
    X_POS = 80
    Y_POS = 310
    Y_POS_DUCK = 340
    JUMP_VEL = 8.5

    def __init__(self):
        self.duck_img = DUCKING1
        self.run_img = RUNNING1
        self.jump_img = JUMPING1

        self.chic_duck = False
        self.chic_run = True
        self.chic_jump = False

        self.step_index = 0
        self.jump_vel = self.JUMP_VEL
        self.image = self.run_img[0]
        self.chic_rect = self.image.get_rect()
        self.chic_rect.x = self.X_POS
        self.chic_rect.y = self.Y_POS

    def update(self, userInput):
        if self.chic_duck:
            self.duck()
        if self.chic_run:
            self.run()
        if self.chic_jump:
            self.jump()

        if self.step_index >= 10:
            self.step_index = 0

        if userInput[pygame.K_UP] and not self.chic_jump:
            self.chic_duck = False
            self.chic_run = False
            self.chic_jump = True
        elif userInput[pygame.K_DOWN] and not self.chic_jump:
            self.chic_duck = True
            self.chic_run = False
            self.chic_jump = False
        elif not (self.chic_jump or userInput[pygame.K_DOWN]):
            self.chic_duck = False
            self.chic_run = True
            self.chic_jump = False

    def duck(self):
        self.image = self.duck_img[self.step_index // 5]
        self.chic_rect = self.image.get_rect()
        self.chic_rect.x = self.X_POS
        self.chic_rect.y = self.Y_POS_DUCK
        self.step_index += 1

    def run(self):
        self.image = self.run_img[self.step_index // 5]
        self.chic_rect = self.image.get_rect()
        self.chic_rect.x = self.X_POS
        self.chic_rect.y = self.Y_POS
        self.step_index += 1

    def jump(self):
        self.image = self.jump_img
        if self.chic_jump:
            self.chic_rect.y -= self.jump_vel * 4
            self.jump_vel -= 0.8
        if self.jump_vel < - self.JUMP_VEL:
            self.chic_jump = False
            self.jump_vel = self.JUMP_VEL

    def draw(self, SCREEN):
        SCREEN.blit(self.image, (self.chic_rect.x, self.chic_rect.y))

class Alpaca:
    X_POS = 80
    Y_POS = 310
    Y_POS_DUCK = 340
    JUMP_VEL = 8.5

    def __init__(self):
        self.duck_img = DUCKING2
        self.run_img = RUNNING2
        self.jump_img = JUMPING2

        self.alpa_duck = False
        self.alpa_run = True
        self.alpa_jump = False

        self.step_index = 0
        self.jump_vel = self.JUMP_VEL
        self.image = self.run_img[0]
        self.alpa_rect = self.image.get_rect()
        self.alpa_rect.x = self.X_POS
        self.alpa_rect.y = self.Y_POS

    def update(self, userInput):
        if self.alpa_duck:
            self.duck()
        if self.alpa_run:
            self.run()
        if self.alpa_jump:
            self.jump()

        if self.step_index >= 10:
            self.step_index = 0

        if userInput[pygame.K_UP] and not self.alpa_jump:
            self.alpa_duck = False
            self.alpa_run = False
            self.alpa_jump = True
        elif userInput[pygame.K_DOWN] and not self.alpa_jump:
            self.alpa_duck = True
            self.alpa_run = False
            self.alpa_jump = False
        elif not (self.alpa_jump or userInput[pygame.K_DOWN]):
            self.alpa_duck = False
            self.alpa_run = True
            self.alpa_jump = False

    def duck(self):
        self.image = self.duck_img[self.step_index // 5]
        self.alpa_rect = self.image.get_rect()
        self.alpa_rect.x = self.X_POS
        self.alpa_rect.y = self.Y_POS_DUCK
        self.step_index += 1

    def run(self):
        self.image = self.run_img[self.step_index // 5]
        self.alpa_rect = self.image.get_rect()
        self.alpa_rect.x = self.X_POS
        self.alpa_rect.y = self.Y_POS
        self.step_index += 1

    def jump(self):
        self.image = self.jump_img
        if self.alpa_jump:
            self.alpa_rect.y -= self.jump_vel * 4
            self.jump_vel -= 0.8
        if self.jump_vel < - self.JUMP_VEL:
            self.alpa_jump = False
            self.jump_vel = self.JUMP_VEL

    def draw(self, SCREEN):
        SCREEN.blit(self.image, (self.alpa_rect.x, self.alpa_rect.y))

class Cloud:
    def __init__(self):
        self.x = SCREEN_WIDTH + random.randint(800, 1000)
        self.y = random.randint(50, 100)
        self.image = CLOUD
        self.width = self.image.get_width()

    def update(self):
        self.x -= game_speed
        if self.x < -self.width:
            self.x = SCREEN_WIDTH + random.randint(2500, 3000)
            self.y = random.randint(50, 100)

    def draw(self, SCREEN):
        SCREEN.blit(self.image, (self.x, self.y))


class Obstacle:
    def __init__(self, image, type):
        self.image = image
        self.type = type
        self.rect = self.image[self.type].get_rect()
        self.rect.x = SCREEN_WIDTH

    def update(self):
        self.rect.x -= game_speed
        if self.rect.x < -self.rect.width:
            obstacles.pop()

    def draw(self, SCREEN):
        SCREEN.blit(self.image[self.type], self.rect)


class SmallCactus(Obstacle):
    def __init__(self, image):
        self.type = random.randint(0, 2)
        super().__init__(image, self.type)
        self.rect.y = 325


class LargeCactus(Obstacle):
    def __init__(self, image):
        self.type = random.randint(0, 2)
        super().__init__(image, self.type)
        self.rect.y = 300


class Bird(Obstacle):
    def __init__(self, image):
        self.type = 0
        super().__init__(image, self.type)
        self.rect.y = 250
        self.index = 0

    def draw(self, SCREEN):
        if self.index >= 9:
            self.index = 0
        SCREEN.blit(self.image[self.index//5], self.rect)
        self.index += 1


def load_leaderboard():
    with open("scorea.txt", "r") as f:
        lines = f.readlines()
        # 去除每行末尾的換行符號
        lines = [line.rstrip("\n") for line in lines]
        # 轉換成數字並回傳
        return [int(line) for line in lines]

def display_leaderboard(difficulty):
    global points
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:  # 按下 enter 鍵返回主菜單
                    main(difficulty)
                    run = False 
                if event.key == pygame.K_ESCAPE:  # 按下 escape 鍵結束遊戲
                    pygame.quit()
                    sys.exit()

        SCREEN.fill((255, 255, 255))
        font = pygame.font.Font('freesansbold.ttf', 30)
        title = font.render("Leaderboard", True, (0, 0, 0))
        title_rect = title.get_rect()
        title_rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 200)
        SCREEN.blit(title, title_rect)

        scores = load_leaderboard()
        if len(scores) > 0:
            for i in range(len(scores)):
                text = font.render(str(i + 1) + ". " + str(scores[i]), True, (0, 0, 0))
                text_rect = text.get_rect()
                text_rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 150 + i * 50)
                SCREEN.blit(text, text_rect)

            # 如果排行榜只有一名玩家，其他两名玩家分数为 None
            if len(scores) == 1:
                for i in range(1, 3):
                    text = font.render(str(i + 1) + ". None", True, (0, 0, 0))
                    text_rect = text.get_rect()
                    text_rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 150 + (i + 1) * 50)
                    SCREEN.blit(text, text_rect)

        pygame.display.update()




def main(select_role):
    global game_speed, x_pos_bg, y_pos_bg, points, obstacles
    game_speed = 20
    run = True
    clock = pygame.time.Clock()
    cloud = Cloud()
    x_pos_bg = 0
    y_pos_bg = 380
    points = 0
    font = pygame.font.Font('freesansbold.ttf', 20)
    obstacles = []
    death_count = 0
    if select_role == 0:
        player = Dinosaur()
    elif select_role == 1:
        player = Chicken()
    else:
        player = Alpaca()
    

    def score():
        global points, game_speed
        points += 1
        if points % 100 == 0:
            game_speed += 1

        text = font.render("Points: " + str(points), True, (0, 0, 0))
        textRect = text.get_rect()
        textRect.center = (1000, 40)
        SCREEN.blit(text, textRect)

    def background():
        global x_pos_bg, y_pos_bg
        image_width = BG.get_width()
        SCREEN.blit(BG, (x_pos_bg, y_pos_bg))
        SCREEN.blit(BG, (image_width + x_pos_bg, y_pos_bg))
        if x_pos_bg <= -image_width:
            SCREEN.blit(BG, (image_width + x_pos_bg, y_pos_bg))
            x_pos_bg = 0
        x_pos_bg -= game_speed

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                sys.exit()
            # if event.type == pygame.KEYDOWN:
            #     if event.key == pygame.K_q:
            #         run = False
            #         game_over(difficulty)

        SCREEN.fill((255, 255, 255))
        userInput = pygame.key.get_pressed()

        player.draw(SCREEN)
        player.update(userInput)

        if len(obstacles) == 0:
            if random.randint(0, 2) == 0:
                obstacles.append(SmallCactus(SMALL_CACTUS))
            elif random.randint(0, 2) == 1:
                obstacles.append(LargeCactus(LARGE_CACTUS))
            elif random.randint(0, 2) == 2:
                obstacles.append(Bird(BIRD))

        for obstacle in obstacles:
            obstacle.draw(SCREEN)
            obstacle.update()
            if select_role == 0 :
                if player.dino_rect.colliderect(obstacle.rect):
                    pygame.draw.rect(SCREEN, (255,0,0) , player.dino_rect , 2 )
                    background()
                    cloud.draw(SCREEN)
                    cloud.update()
                    score()
                    clock.tick(30)
                    pygame.display.update()
                    pygame.time.delay(2000)
                    death_count += 1
                    menu(death_count,select_role)
            elif select_role == 1 :
                if player.chic_rect.colliderect(obstacle.rect):
                    pygame.draw.rect(SCREEN, (255,0,0) , player.chic_rect , 2 )
                    background()
                    cloud.draw(SCREEN)
                    cloud.update()
                    score()
                    clock.tick(30)
                    pygame.display.update()
                    pygame.time.delay(2000)
                    death_count += 1
                    menu(death_count,select_role)
            elif select_role == 2 :
                if player.alpa_rect.colliderect(obstacle.rect):
                    pygame.draw.rect(SCREEN, (255,0,0) , player.alpa_rect , 2 )
                    background()
                    cloud.draw(SCREEN)
                    cloud.update()
                    score()
                    clock.tick(30)
                    pygame.display.update()
                    pygame.time.delay(2000)
                    death_count += 1
                    menu(death_count,select_role)

        background()

        cloud.draw(SCREEN)
        cloud.update()

        score()

        clock.tick(30)
        pygame.display.update()

# def game_over(difficulty):
#     global points
#     run = True
#     while run:
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 pygame.quit()
#                 sys.exit()
#             if event.type == pygame.KEYDOWN:
#                 if event.key == pygame.K_RETURN:  # 按下 enter 鍵重置遊戲
#                     main(difficulty)
#                 if event.key == pygame.K_ESCAPE:  # 按下 escape 鍵結束遊戲
#                     pygame.quit()
#                     sys.exit()

#         SCREEN.fill((255, 255, 255))
#         font = pygame.font.Font('freesansbold.ttf', 30)
#         text = font.render("Game Over", True, (0, 0, 0))
#         textRect = text.get_rect()
#         textRect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 50)
#         SCREEN.blit(text, textRect)

#         score_text = font.render("Score: " + str(points), True, (0, 0, 0))
#         score_rect = score_text.get_rect()
#         score_rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
#         SCREEN.blit(score_text, score_rect)

#         restart_text = font.render("Press Enter to play again", True, (0, 0, 0))
#         restart_rect = restart_text.get_rect()
#         restart_rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 50)
#         SCREEN.blit(restart_text, restart_rect)

#         quit_text = font.render("Press Esc to quit", True, (0, 0, 0))
#         quit_rect = quit_text.get_rect()
#         quit_rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 100)
#         SCREEN.blit(quit_text, quit_rect)
#         #省略上面程式碼
#         with open('scorea.txt', 'a') as f:
#             f.write(str(points) + '\n')
#         # 显示排行榜
#         display_leaderboard(difficulty)

#         pygame.display.update()


def game_begin0():
    run = True
    line_color = (0, 0, 0)  # 黑色
    line_width = 2
    start_x = SCREEN_WIDTH // 2 - 120
    start_y = SCREEN_HEIGHT // 2 - 205
    end_x = SCREEN_WIDTH // 2 + 170
    end_y = SCREEN_HEIGHT // 2 - 205
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    run = False
                    pygame.quit()
                    sys.exit()
                else:
                    game_begin1()  # 開始新遊戲

        SCREEN.fill((255, 255, 255))
         
        font = pygame.font.Font('freesansbold.ttf', 30)
        text0 = font.render("Game Rule", True, (20, 10, 10))
        text = font.render("In the game, you need to use the arrow keys ", True, (20, 10, 10))
        text2 = font.render("to control the direction of movement of the character.", True, (20, 20, 20))
        text4 = font.render("The space bar allows her to jump.", True, (20, 20, 20))
        text3 = font.render("With practice and determination,", True, (128,42,42))
        text5 = font.render("you can master the controls and achieve high scores in the game.", True, (128,42,42))
        textRect0 = text0.get_rect()
        textRect = text.get_rect()
        textRect2 = text2.get_rect()
        textRect3 = text3.get_rect()
        textRect4 = text4.get_rect()
        textRect5 = text5.get_rect()
        textRect0.center = (SCREEN_WIDTH // 2 + 26 , SCREEN_HEIGHT // 2 - 235)
        textRect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 20)
        textRect2.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 30 )
        textRect4.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 80 )
        textRect3.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 130)
        textRect5.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 180)
        SCREEN.blit(text, textRect)
        SCREEN.blit(text0, textRect0)
        SCREEN.blit(text2, textRect2)
        SCREEN.blit(text3, textRect3)
        SCREEN.blit(text4, textRect4)
        SCREEN.blit(text5, textRect5)
        SCREEN.blit(STARTING, (SCREEN_WIDTH // 2 - 20, SCREEN_HEIGHT // 2 - 175))   
        pygame.draw.line( SCREEN ,  line_color, (start_x, start_y), (end_x, end_y), line_width)
       
        pygame.display.update()

def game_begin1():
    run = True
    select_role = 0 
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    run = False
                    pygame.quit()
                    sys.exit()
                elif event.key == pygame.K_LEFT:
                    game_begin0()
                else:
                    menu(0,0)  # 開始新遊戲

        SCREEN.fill((255, 255, 255))
        font = pygame.font.Font('freesansbold.ttf', 30)
        text = font.render("Come and start this exciting running game!", True, (20, 10, 10))
        text2 = font.render("Help the character escape from the dangerous pineapple field", True, (20, 20, 20))
        text4 = font.render("Challenge your reaction speed and skills", True, (20, 20, 20))
        text3 = font.render("Let us survive at National Chung Cheng University!!", True, (128,42,42))
        textRect = text.get_rect()
        textRect2 = text2.get_rect()
        textRect3 = text3.get_rect()
        textRect4 = text4.get_rect()
        textRect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 20)
        textRect2.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 40 )
        textRect4.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 100 )
        textRect3.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 155)
        SCREEN.blit(text, textRect)
        SCREEN.blit(text2, textRect2)
        SCREEN.blit(text3, textRect3)
        SCREEN.blit(text4, textRect4)
        SCREEN.blit(RUNNING1[0], (SCREEN_WIDTH // 2 - 180, SCREEN_HEIGHT // 2 - 180))  
        SCREEN.blit(RUNNING1[0], (SCREEN_WIDTH // 2 - 20, SCREEN_HEIGHT // 2 - 180))   
        SCREEN.blit(RUNNING1[0], (SCREEN_WIDTH // 2 + 140, SCREEN_HEIGHT // 2 - 180))    
        
       
        pygame.display.update()

def menu(death_count,select_role):
    global points
    run = True
    border_color = (0, 0, 0)  # 黑色
    border_width = 3
    while run:
        SCREEN.fill((255, 255, 255))
        font = pygame.font.Font('freesansbold.ttf', 30)
        if death_count == 0:
            text2 = font.render("Press <- Key to use Chicken", True, (30, 30, 0))
            text4 = font.render("|", True, (30, 30, 0))
            text3 = font.render("Press    Key to use Dinosaur", True, (30, 30, 0))
            text5 = font.render("v", True, (30, 30, 0))
            text = font.render("Press ESC for quit", True, (45, 20, 20))
            text6 = font.render("Press -> Key to use Alpapa", True, (30, 30, 0))
            textRect = text.get_rect()
            textRect2 = text2.get_rect()
            textRect3 = text3.get_rect()
            textRect4 = text4.get_rect()
            textRect5 = text5.get_rect()
            textRect6 = text6.get_rect()
            textRect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 5)
            textRect2.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 50 )
            textRect3.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 105 )
            textRect4.center = (SCREEN_WIDTH // 2 - 105, SCREEN_HEIGHT // 2 + 95 )
            textRect5.center = (SCREEN_WIDTH // 2 - 105 , SCREEN_HEIGHT // 2 + 110 )
            textRect6.center = (SCREEN_WIDTH // 2 - 15 , SCREEN_HEIGHT // 2 + 165 )
            SCREEN.blit(text, textRect)
            SCREEN.blit(text2, textRect2)
            SCREEN.blit(text3, textRect3)
            SCREEN.blit(text4, textRect4)
            SCREEN.blit(text5, textRect5)
            SCREEN.blit(text6, textRect6)
            SCREEN.blit(STARTING, (SCREEN_WIDTH // 2 - 20, SCREEN_HEIGHT // 2 - 177))
            pygame.draw.rect(SCREEN, border_color,(280, 250, 540, 255), border_width)
            # text = font.render("Press --> for Dinosaur", True, (20, 10, 10))
            # text2 = font.render("Press <-- for Chicken", True, (20, 20, 20))
            # text3 = font.render("Use the arrow keys to select your favorite character >///<", True, (128,42,42))
            # textRect = text.get_rect()
            # textRect2 = text2.get_rect()
            # textRect3 = text3.get_rect()
            # textRect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 60)
            # textRect2.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 100 )
            # textRect3.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 188)
            # SCREEN.blit(text, textRect)
            # SCREEN.blit(text2, textRect2)
            # SCREEN.blit(text3, textRect3)
            # SCREEN.blit(RUNNING1[0], (SCREEN_WIDTH // 2 - 20, SCREEN_HEIGHT // 2 - 120))   
            # pygame.draw.rect(SCREEN, border_color, (360, 300, 410, 170), border_width)
        elif death_count > 0 and select_role == 0 :
            text2 = font.render("Press <- Key to use ChickenRestart", True, (30, 30, 0))
            text4 = font.render("|", True, (30, 30, 0))
            text3 = font.render("Press    Key to use DinosaurRestart", True, (30, 30, 0))
            text5 = font.render("v", True, (30, 30, 0))
            text6 = font.render("Press -> Key to use AlpapaRestart", True, (30, 30, 0))
            text = font.render("Press ESC for quit", True, (45, 20, 20))
            score = font.render("Your Score: " + str(points), True, (40, 40, 0))
            scoreRect = score.get_rect()
            scoreRect.center = (SCREEN_WIDTH // 2 + 5 , SCREEN_HEIGHT // 2 + 198)
            SCREEN.blit(score, scoreRect)
            textRect = text.get_rect()
            textRect2 = text2.get_rect()
            textRect3 = text3.get_rect()
            textRect4 = text4.get_rect()
            textRect5 = text5.get_rect()
            textRect6 = text6.get_rect()
            textRect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 5)
            textRect2.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 50 )
            textRect3.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 105 )
            textRect4.center = (SCREEN_WIDTH // 2 - 155 , SCREEN_HEIGHT // 2 + 95 )
            textRect5.center = (SCREEN_WIDTH // 2 - 155 , SCREEN_HEIGHT // 2 + 110 )
            textRect6.center = (SCREEN_WIDTH // 2 -4  , SCREEN_HEIGHT // 2 + 155 )
            SCREEN.blit(text, textRect)
            SCREEN.blit(text2, textRect2)
            SCREEN.blit(text3, textRect3)
            SCREEN.blit(text4, textRect4)
            SCREEN.blit(text5, textRect5)
            SCREEN.blit(text6, textRect6)
            SCREEN.blit(DEAD, (SCREEN_WIDTH // 2 - 7, SCREEN_HEIGHT // 2 - 177))
            pygame.draw.rect(SCREEN, border_color,(280, 240, 561, 295), border_width)
        elif death_count > 0 and select_role == 1 :
            text2 = font.render("Press <- Key to use ChickenRestart", True, (30, 30, 0))
            text4 = font.render("|", True, (30, 30, 0))
            text3 = font.render("Press    Key to use DinosaurRestart", True, (30, 30, 0))
            text5 = font.render("v", True, (30, 30, 0))
            text6 = font.render("Press -> Key to use AlpapaRestart", True, (30, 30, 0))
            text = font.render("Press ESC for quit", True, (45, 20, 20))
            score = font.render("Your Score: " + str(points), True, (40, 40, 0))
            scoreRect = score.get_rect()
            scoreRect.center = (SCREEN_WIDTH // 2 + 5 , SCREEN_HEIGHT // 2 + 198)
            SCREEN.blit(score, scoreRect)
            textRect = text.get_rect()
            textRect2 = text2.get_rect()
            textRect3 = text3.get_rect()
            textRect4 = text4.get_rect()
            textRect5 = text5.get_rect()
            textRect6 = text6.get_rect()
            textRect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 5)
            textRect2.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 50 )
            textRect3.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 105 )
            textRect4.center = (SCREEN_WIDTH // 2 - 155 , SCREEN_HEIGHT // 2 + 95 )
            textRect5.center = (SCREEN_WIDTH // 2 - 155 , SCREEN_HEIGHT // 2 + 110 )
            textRect6.center = (SCREEN_WIDTH // 2 -4  , SCREEN_HEIGHT // 2 + 155 )
            SCREEN.blit(text, textRect)
            SCREEN.blit(text2, textRect2)
            SCREEN.blit(text3, textRect3)
            SCREEN.blit(text4, textRect4)
            SCREEN.blit(text5, textRect5)
            SCREEN.blit(text6, textRect6)
            SCREEN.blit(DEAD1, (SCREEN_WIDTH // 2 - 7, SCREEN_HEIGHT // 2 - 177))
            pygame.draw.rect(SCREEN, border_color,(280, 240, 561, 295), border_width)   
        elif death_count > 0 and select_role == 2 :
            text2 = font.render("Press <- Key to use ChickenRestart", True, (30, 30, 0))
            text4 = font.render("|", True, (30, 30, 0))
            text3 = font.render("Press    Key to use DinosaurRestart", True, (30, 30, 0))
            text5 = font.render("v", True, (30, 30, 0))
            text6 = font.render("Press -> Key to use AlpapaRestart", True, (30, 30, 0))
            text = font.render("Press ESC for quit", True, (45, 20, 20))
            score = font.render("Your Score: " + str(points), True, (40, 40, 0))
            scoreRect = score.get_rect()
            scoreRect.center = (SCREEN_WIDTH // 2 + 5 , SCREEN_HEIGHT // 2 + 198)
            SCREEN.blit(score, scoreRect)
            textRect = text.get_rect()
            textRect2 = text2.get_rect()
            textRect3 = text3.get_rect()
            textRect4 = text4.get_rect()
            textRect5 = text5.get_rect()
            textRect6 = text6.get_rect()
            textRect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 5)
            textRect2.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 50 )
            textRect3.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 105 )
            textRect4.center = (SCREEN_WIDTH // 2 - 155 , SCREEN_HEIGHT // 2 + 95 )
            textRect5.center = (SCREEN_WIDTH // 2 - 155 , SCREEN_HEIGHT // 2 + 110 )
            textRect6.center = (SCREEN_WIDTH // 2 -4  , SCREEN_HEIGHT // 2 + 155 )
            SCREEN.blit(text, textRect)
            SCREEN.blit(text2, textRect2)
            SCREEN.blit(text3, textRect3)
            SCREEN.blit(text4, textRect4)
            SCREEN.blit(text5, textRect5)
            SCREEN.blit(text6, textRect6)
            SCREEN.blit(DEAD2, (SCREEN_WIDTH // 2 - 7, SCREEN_HEIGHT // 2 - 200))
            pygame.draw.rect(SCREEN, border_color,(280, 240, 561, 295), border_width) 
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    run = False
                    pygame.quit()
                    sys.exit()
                elif event.key == pygame.K_LEFT:
                    select_role = 1
                    points = 0  # 重置分數
                    main(select_role)  # 開始新遊戲
                elif event.key == pygame.K_RIGHT:
                    select_role = 2
                    points = 0  # 重置分數
                    main(select_role)  # 開始新遊戲
                else:
                    points = 0  # 重置分數
                    select_role = 0 
                    main(select_role)  # 開始新遊戲
# menu(death_count=0)
game_begin0()