import pygame
import random
import time

pygame.init()

clock = pygame.time.Clock()
all_sprites = pygame.sprite.Group()
players = pygame.sprite.Group()
green_blocks = pygame.sprite.Group()
green_blocks1 = pygame.sprite.Group()
yellow_blocks = pygame.sprite.Group()
red_bullets = pygame.sprite.Group()
red_bullet_timer = 0
green_block_timer = 0
green_block1_timer = 0
yellow_block_timer = 0
question_event_timer = 0
screenWIDTH = 720
screenHEIGHT = 800
screen = pygame.display.set_mode((screenWIDTH, screenWIDTH))
background_image = pygame.image.load('background.png').convert()
background_image = pygame.transform.scale(background_image, (screenWIDTH, screenHEIGHT))
# 定義顏色
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
# 定義角色的寬度和高度
PLAYER_WIDTH = 50
PLAYER_HEIGHT = 50

# 計算角色的位置
player_x = screenWIDTH / 2 - PLAYER_WIDTH / 2
player_y = screenHEIGHT - PLAYER_HEIGHT -100
# 定義 Player class
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('bullet.png').convert()
        self.image = pygame.transform.scale(self.image, (75, 75))
        self.rect = self.image.get_rect()
        self.health = 100
        self.health_max = 100
# 創建 Player 物件
player = Player()
player_health = player.health
player_health_max = player.health_max
players.add(player)
all_sprites.add(player)

# 定义血量条大小和位置
health_bar_length = screenWIDTH * (player_health / player_health_max)
health_bar_height = 30
health_bar_x = 0
health_bar_y = screenHEIGHT - 30
health_red_length = screenWIDTH
health_red_height = 30
health_red_x = 0
health_red_y = screenHEIGHT - 30
# 定义方形的位置、大小和线宽
rect1 = pygame.Rect(0, 200, 360, 275)
rect2 = pygame.Rect(360, 200, 360, 275)
rect3 = pygame.Rect(0, 475, 360, 275)
rect4 = pygame.Rect(360, 475, 360, 275)
line_width = 3

# 定义四个不同颜色的空心方形
color1 = (255, 0, 0)
color2 = (0, 255, 0)
color3 = (0, 0, 255)
color4 = (255, 255, 0)

# 定義魔王方塊的大小和初始位置
BOSS_WIDTH = 50
BOSS_HEIGHT = 50
boss_x = 360 - BOSS_WIDTH / 2
boss_y = 100 - BOSS_HEIGHT / 2
# 定義玩家和魔王的移動速度
PLAYER_SPEED = 5
BOSS_SPEED = 2
# 定义红色子弹半径和速度
BULLET_RADIUS = 10
BULLET_SPEED = 10
# 設定每3秒產生一個綠色方塊
class GreenBlock(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('greena.jpg').convert()
        self.image = pygame.transform.scale(self.image, (55, 55))
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, screenWIDTH - self.rect.width)
        self.rect.y = -150
        self.speed = random.randint(2, 5)
class GreenBlock1(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('greenb.jpg').convert()
        self.image = pygame.transform.scale(self.image, (60, 60))
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, screenWIDTH - self.rect.width)
        self.rect.y = -150
        self.speed = random.randint(1, 4)
class YellowBlock(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('blood.jpg').convert()
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, screenWIDTH - self.rect.width)
        self.rect.y = -150
        self.speed = random.randint(2, 3)

questions = [
    {
    "question": "以下關於紅血球、白血球、血小板的敘述，何者正確？",
    "options": [
        "只有白血球有細胞核",
        "白血球、血小板有細胞核，紅血球不具細胞核",
        "白血球具有凝血的功能",
        "血球數量大小：白血球>紅血球>血小板"
    ],
    "answer": "只有白血球有細胞核"
}
    # add more questions here
]
# 預設沒有收到藍色方塊出現的事件
blue_block_event_received = False
show_question = False
answer = None
group = None
# 設定遊戲視窗大小和標題
screen = pygame.display.set_mode((screenWIDTH, screenHEIGHT))
pygame.display.set_caption("My Game")
# 繪製開始畫面
font = pygame.font.SysFont("微软正黑体.ttf", 48)
text = font.render("Click Anywhere to Start", True, WHITE)
text_rect = text.get_rect()
text_rect.center = (screenWIDTH / 2, screenHEIGHT / 2)
screen.fill(BLACK)
screen.blit(text, text_rect)
pygame.display.flip()
# 等待玩家點擊開始
waiting = True
while waiting:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            waiting = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            waiting = False
score = 0
game_font = pygame.font.SysFont("微软正黑体.ttf", 36)
gameover = False
# 更新遊戲畫面
pygame.display.flip()
# 遊戲主迴圈
running = True
while running:
    # 控制每秒更新畫面的次數為 120
    clock.tick(120)
    StartTimer = pygame.time.get_ticks()
    player.rect.center = (player_x + PLAYER_WIDTH / 2, player_y + PLAYER_HEIGHT / 2)
    score += 1/12
    score_float = float("{:.1f}".format(score))
    score_text = game_font.render("Score: " + str(int(score_float)), True, WHITE)
    score_rect = score_text.get_rect()
    score_rect.topright = (screenWIDTH - 10, 25)
    
    if not blue_block_event_received and StartTimer - question_event_timer > 8000 and not show_question:
        blue_block_event_received = True
    health_bar_length = screenWIDTH * (player_health / player_health_max)
    if health_bar_length < health_red_length:
        health_red_length -= (health_red_length - health_bar_length) / 20
    if player_health > player_health_max:
        player_health = player_health_max
    if player_health <= 0:
        gameover = True
    # 更新玩家位置
    keys = pygame.key.get_pressed()
    if keys[pygame.K_a] and player_x > 0:
        player_x -= PLAYER_SPEED
    elif keys[pygame.K_d] and (player_x + PLAYER_WIDTH) < screenWIDTH:
        player_x += PLAYER_SPEED
    if keys[pygame.K_w] and player_y > 200:
        #if blue_block_event_received:
        player_y -= PLAYER_SPEED
    elif keys[pygame.K_s] and (player_y + PLAYER_HEIGHT) < (screenHEIGHT - 50):
        #if blue_block_event_received:
        player_y += PLAYER_SPEED
    if keys[pygame.K_SPACE]:
     # 在红色方块位置生成红色子弹
        if StartTimer - red_bullet_timer >= 10:
            bullet = pygame.sprite.Sprite()
            bullet.image = pygame.Surface((20, 20))  # 創建一個 20x20 的 Surface 物件
            bullet.image.set_colorkey((0, 0, 0))  # 將 Surface 的黑色設為透明
            pygame.draw.circle(bullet.image, (255, 0, 0), (10, 10), 10)  # 畫一個紅色圓形
            bullet.rect = bullet.image.get_rect()
            bullet.rect.center = (player_x + PLAYER_WIDTH / 2, player_y)
            red_bullets.add(bullet)
            red_bullet_timer = StartTimer

    # 更新红色子弹位置
    for bullet in red_bullets:
        bullet.rect.y -= BULLET_SPEED
        if bullet.rect.y < 0:
            red_bullets.remove(bullet)
    for green_block in green_blocks:
        green_block.rect.y += green_block.speed
        if green_block.rect.y > screenHEIGHT:
            green_blocks.remove(green_block)
    for green_block1 in green_blocks1:
        green_block1.rect.y += green_block1.speed
        if green_block1.rect.y > screenHEIGHT:
            green_blocks.remove(green_block1)
    for yellow_block in yellow_blocks:
        yellow_block.rect.y += yellow_block.speed
        if yellow_block.rect.y > screenHEIGHT:
            yellow_blocks.remove(yellow_block)
    # 碰撞检测，红色子弹和绿色方块碰撞时，子弹和方块都消失
    for bullet in red_bullets:
        hit_list = pygame.sprite.spritecollide(bullet, green_blocks, True)
        if len(hit_list) > 0:
            red_bullets.remove(bullet)
            score += 10
    for bullet in red_bullets:
        hit_list = pygame.sprite.spritecollide(bullet, yellow_blocks, True)
        if len(hit_list) > 0:
            red_bullets.remove(bullet)
            player_health -= 3
            score -= 20
    for player in players:
        hit_list = pygame.sprite.spritecollide(player, green_blocks, True)
        if len(hit_list) > 0:
            player_health -= 10
    for player in players:
        hit_list = pygame.sprite.spritecollide(player, green_blocks1, True)
        if len(hit_list) > 0:
            player_health -= 10
    # 每3秒創建一個綠色方塊
    if StartTimer - green_block_timer >= 25000 / (12 + green_block_timer * 0.002):
        green_block = GreenBlock()
        all_sprites.add(green_block)
        green_blocks.add(green_block)
        green_block_timer = StartTimer
    # 每3秒創建一個綠色方塊
    if StartTimer - green_block1_timer >= 50000 / (10 + green_block1_timer * 0.0005):
        green_block1 = GreenBlock1()
        all_sprites.add(green_block1)
        green_blocks1.add(green_block1)
        green_block1_timer = StartTimer
    # 每3秒創建一個黃色方塊
    if StartTimer - yellow_block_timer >= 50000 / (10 + score * 0.002):
        yellow_block = YellowBlock()
        all_sprites.add(yellow_block)
        yellow_blocks.add(yellow_block)
        yellow_block_timer = StartTimer
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # 當收到藍色方塊出現的事件時
    
    green_blocks.update()
    # 繪製遊戲元素
    screen.fill(BLACK)
    
    if blue_block_event_received:
        ques_font = pygame.font.Font("微软正黑体.ttf", 24)
        if not show_question:
            question_time_max = 2 + 10 / ( 1 + StartTimer//6000)
            question_time = question_time_max  # 初始化問題時間為最大時間
            # 随机选择一个问题
            question = random.choice(questions)
            # 将选项随机分配给不同的变量
            option1, option2, option3, option4 = random.sample(question["options"], 4)
            # 保存正确的答案
            answer = question["answer"]
            show_question = True
            question_text = ques_font.render(question["question"], True, WHITE)
        if blue_block_event_received and show_question :
            time_bar_length = screenWIDTH * (question_time / question_time_max)  # 更新時間條寬度
            time_bar_height = 20
            time_bar_x = 0
            time_bar_y = 0
            question_time -= 0.1 / 12  # 更新問題時間
            if question_time <= 0:
                # 判斷玩家回答問題是否正確，並相應地加減分和生命值
                if player_x < 360 and player_y < 475:
                    group = str(option1)
                elif player_x >= 360 and player_y < 475:
                    group = str(option2)
                elif player_x < 360 and player_y >= 475:
                    group = str(option3)
                elif player_x >= 360 and player_y >= 475:
                    group = str(option4)
                if group == answer:
                    score += 200
                    player_health += 10
                else:
                    player_health -= 30
                question_event_timer = StartTimer
                blue_block_event_received = False
                show_question = False
                group = -1
    else:
        question_text = game_font.render("", True, WHITE)
    question_rect = question_text.get_rect()
    question_rect.center = (screenWIDTH / 2, 100)

    if not gameover:
        screen.blit(background_image, (0, 0))
        all_sprites.draw(screen)
        #pygame.draw.rect(screen, RED, pygame.Rect(player_x, player_y, PLAYER_WIDTH, PLAYER_HEIGHT))
        screen.blit(player.image, player.rect)
        pygame.draw.rect(screen, RED, pygame.Rect(health_red_x, health_red_y, health_red_length, health_red_height))
        pygame.draw.rect(screen, WHITE, pygame.Rect(health_bar_x, health_bar_y, health_bar_length, health_bar_height))
        for bullet in red_bullets:
            pygame.draw.circle(screen, (255, 0, 0), bullet.rect.center, 10)
        screen.blit(score_text, score_rect)
        if blue_block_event_received:
            screen.blit(question_text, question_rect)
            pygame.draw.rect(screen, WHITE, pygame.Rect(time_bar_x, time_bar_y, time_bar_length, time_bar_height))
            # 绘制四个空心方形
            pygame.draw.rect(screen, color1, rect1, line_width)
            pygame.draw.rect(screen, color2, rect2, line_width)
            pygame.draw.rect(screen, color3, rect3, line_width)
            pygame.draw.rect(screen, color4, rect4, line_width)
            # 创建一个字体对象，设置字体和字体大小
            option_font = pygame.font.Font("微软正黑体.ttf", 17)

            # 在第一个格子的中心绘制选项1文本
            option1_text = option_font.render(option1, True, WHITE)
            option1_rect = option1_text.get_rect(center=(180, 337))
            screen.blit(option1_text, option1_rect)

            # 在第二个格子的中心绘制选项2文本
            option2_text = option_font.render(option2, True, WHITE)
            option2_rect = option2_text.get_rect(center=(540, 337))
            screen.blit(option2_text, option2_rect)

            # 在第三个格子的中心绘制选项3文本
            option3_text = option_font.render(option3, True, WHITE)
            option3_rect = option3_text.get_rect(center=(180, 612))
            screen.blit(option3_text, option3_rect)

            # 在第四个格子的中心绘制选项4文本
            option4_text = option_font.render(option4, True, WHITE)
            option4_rect = option4_text.get_rect(center=(540, 612))
            screen.blit(option4_text, option4_rect)
        
        pygame.display.flip()
    else:
        text0 = font.render("Game Over", True, WHITE)
        text1 = font.render("Score: "+str(int(score)), True, WHITE)
        text0_rect = text0.get_rect()
        text1_rect = text1.get_rect()
        text0_rect.center = (screenWIDTH / 2, screenHEIGHT / 2 - 20)
        text1_rect.center = (screenWIDTH / 2, screenHEIGHT / 2 + 20)
        screen.fill(BLACK)
        screen.blit(text0, text0_rect)
        screen.blit(text1, text1_rect)
        pygame.display.flip()
        break
        # 更新遊戲畫面
    
time.sleep(5)
pygame.quit()