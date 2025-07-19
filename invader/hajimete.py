import pygame
import random
import sys

# ゲームの初期化
pygame.init()

# 効果音の初期化
pygame.mixer.init()
try:
    shoot_sound = pygame.mixer.Sound("shoot.wav")
    invader_hit_sound = pygame.mixer.Sound("hit.wav")
    player_hit_sound = pygame.mixer.Sound("player_hit.wav")
    win_sound = pygame.mixer.Sound("win.wav")
    lose_sound = pygame.mixer.Sound("lose.wav")
except Exception:
    class DummySound:
        def play(self): pass
    shoot_sound = invader_hit_sound = player_hit_sound = win_sound = lose_sound = DummySound()

# 画面サイズ
WIDTH, HEIGHT = 600, 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("インベーダーゲーム")

# 色
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# プレイヤー設定
player_width, player_height = 60, 20
player_x = WIDTH // 2 - player_width // 2
player_y = HEIGHT - 60
player_speed = 7

# 弾設定
bullet_width, bullet_height = 5, 15
bullet_speed = 10
bullets = []

# インベーダー設定
invader_rows = 5
invader_cols = 8
invader_width, invader_height = 50, 30
invader_padding = 20
invader_offset_x = 50
invader_offset_y = 60
invader_speed = 2
invader_direction = 1  # 1:右, -1:左

invaders = []
for row in range(invader_rows):
    for col in range(invader_cols):
        x = invader_offset_x + col * (invader_width + invader_padding)
        y = invader_offset_y + row * (invader_height + invader_padding)
        invaders.append(pygame.Rect(x, y, invader_width, invader_height))

# 敵の弾
enemy_bullets = []
enemy_bullet_speed = 5

# フォント
font = pygame.font.SysFont(None, 48)

# ゲームオーバー
game_over = False
win = False

clock = pygame.time.Clock()

def draw():
    screen.fill(BLACK)
    # プレイヤー
    pygame.draw.rect(screen, GREEN, (player_x, player_y, player_width, player_height))
    # 弾
    for b in bullets:
        pygame.draw.rect(screen, WHITE, b)
    # インベーダー
    for inv in invaders:
        pygame.draw.rect(screen, RED, inv)
    # 敵の弾
    for eb in enemy_bullets:
        pygame.draw.rect(screen, (0, 200, 255), eb)
    if game_over:
        msg = font.render("GAME OVER", True, WHITE)
        screen.blit(msg, (WIDTH//2 - msg.get_width()//2, HEIGHT//2 - msg.get_height()//2))
    if win:
        msg = font.render("YOU WIN!", True, WHITE)
        screen.blit(msg, (WIDTH//2 - msg.get_width()//2, HEIGHT//2 - msg.get_height()//2))
    pygame.display.flip()

sound_played = False
player_hit_played = False

while True:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if not game_over and not win:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    # 弾を発射
                    bullet = pygame.Rect(player_x + player_width//2 - bullet_width//2, player_y, bullet_width, bullet_height)
                    bullets.append(bullet)
                    # 効果音を確実に再生するためにstopしてからplay
                    shoot_sound.stop()
                    shoot_sound.play()

    keys = pygame.key.get_pressed()
    if not game_over and not win:
        if keys[pygame.K_LEFT] and player_x > 0:
            player_x -= player_speed
        if keys[pygame.K_RIGHT] and player_x < WIDTH - player_width:
            player_x += player_speed

        # 弾の移動
        for b in bullets[:]:
            b.y -= bullet_speed
            if b.y < 0:
                bullets.remove(b)
            else:
                # インベーダーとの当たり判定
                for inv in invaders[:]:
                    if b.colliderect(inv):
                        invaders.remove(inv)
                        if b in bullets:
                            bullets.remove(b)
                        # 効果音を確実に再生するためにstopしてからplay
                        invader_hit_sound.stop()
                        invader_hit_sound.play()
                        break

        # インベーダーの移動
        move_down = False
        for inv in invaders:
            inv.x += invader_speed * invader_direction
            if inv.x <= 0 or inv.x + invader_width >= WIDTH:
                move_down = True
        if move_down:
            invader_direction *= -1
            for inv in invaders:
                inv.y += invader_height // 2

        # 敵の弾発射
        if random.randint(0, 60) == 0 and invaders:
            shooter = random.choice(invaders)
            eb = pygame.Rect(shooter.x + invader_width//2 - bullet_width//2, shooter.y + invader_height, bullet_width, bullet_height)
            enemy_bullets.append(eb)

        # 敵の弾の移動
        for eb in enemy_bullets[:]:
            eb.y += enemy_bullet_speed
            if eb.y > HEIGHT:
                enemy_bullets.remove(eb)
            elif eb.colliderect(pygame.Rect(player_x, player_y, player_width, player_height)):
                game_over = True
                if not player_hit_played:
                    player_hit_sound.stop()
                    player_hit_sound.play()
                    player_hit_played = True

        # インベーダーが下まで来たらゲームオーバー
        for inv in invaders:
            if inv.y + invader_height >= player_y:
                game_over = True
                if not player_hit_played:
                    player_hit_sound.stop()
                    player_hit_sound.play()
                    player_hit_played = True

        # 勝利判定
        if not invaders:
            win = True
            if not sound_played:
                win_sound.stop()
                win_sound.play()
                sound_played = True

    elif game_over and not sound_played:
        lose_sound.stop()
        lose_sound.play()
        sound_played = True

    draw()




