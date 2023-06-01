import pygame
import random
import tkinter as tk

def main_code():
    pygame.init()

    screen_x = 1000
    screen_y = 500

    p_width = 15
    p_height = 100
    p_speed = 15

    points_left = 0
    points_right = 0

    ball_r = 10
    ball_speed = 6
    ball_d = 10 * 2

    ball_start_x = screen_x / 2 - ball_r
    ball_start_y = screen_y / 2 - ball_r

    fps = 60

    screen = pygame.display.set_mode((screen_x, screen_y))

    platform_right = pygame.Rect(screen_x - p_width - 5, screen_y / 2 - p_height / 2, p_width, p_height)
    platform_left = pygame.Rect(5, screen_y / 2 - p_height / 2, p_width, p_height)
    ball = pygame.Rect(ball_start_x, ball_start_y, ball_d, ball_d)

    dx = 1
    dy = -1

    font = pygame.font.Font(None, 50)

    green = (0, 133, 35)

    clock = pygame.time.Clock()

    pygame.display.set_caption("Ping-Pong")

    pause = False
    game = True
    while game:
        screen.fill(green)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()

        key = pygame.key.get_pressed()
        if (key[pygame.K_UP] and platform_right.top > 0):
            platform_right.top -= p_speed
        elif (key[pygame.K_DOWN] and platform_right.bottom < screen_y):
            platform_right.bottom += p_speed
        elif (key[pygame.K_w] and platform_left.top > 0):
            platform_left.top -= p_speed
        elif (key[pygame.K_s] and platform_left.bottom < screen_y):
            platform_left.bottom += p_speed

        pygame.draw.rect(screen, pygame.Color("Black"), platform_right)
        pygame.draw.rect(screen, pygame.Color("White"), platform_left)
        pygame.draw.circle(screen, pygame.Color("White"), ball.center, ball_r)
        ball.x += ball_speed * dx
        ball.y += ball_speed * dy

        if ball.centery < ball_r or ball.centery > screen_y:
            dy = -dy
        elif ball.colliderect(platform_left) or ball.colliderect(platform_right):
            dx = -dx

        if ball.centerx > screen_x:
            points_left += 1
            if points_left >= 10:
                game = False
                winner_text = font.render("Победил игрок слева!", True, pygame.Color("White"))
            else:
                ball.x = ball_start_x
                ball.y = ball_start_y
                dx = 0
                dy = 0
                goal_time = pygame.time.get_ticks()
                pause = True

        elif ball.centerx < 0:
            points_right += 1
            if points_right >= 10:
                game = False
                winner_text = font.render("Победил игрок справа!", True, pygame.Color("White"))
            else:
                ball.x = ball_start_x
                ball.y = ball_start_y
                dx = 0
                dy = 0
                goal_time = pygame.time.get_ticks()
                pause = True
        if pause:
            time = pygame.time.get_ticks()
            if time - goal_time > 3000:
                dx = random.choice((1, -1))
                dy = random.choice((1, -1))
                pause = False

        right_text = font.render(f"{points_right}", True, pygame.Color("White"))
        screen.blit(right_text, (screen_x - 40, 20))
        left_text = font.render(f"{points_left}", True, pygame.Color("White"))
        screen.blit(left_text, (20, 20))

        pygame.display.flip()
        clock.tick(fps)

    screen.fill(green)
    screen.blit(winner_text, (screen_x/2 - 150, screen_y/2 - 50))
    pygame.display.update()
    pygame.time.wait(3000)

    pygame.quit()

def show_rules():
    rules_text = "Правила игры:\n1. Не упустите мячик\n2. Забивайте голы\n3. Получайте удовольствие"
    text_widget = tk.Text(root, wrap="word")
    text_widget.insert("1.0", rules_text)
    text_widget.pack()

def button_click():
    main_code()

root = tk.Tk()
root.geometry("700x500")
root.title("Ping-pong")

label = tk.Label(root, text="Привет, игроки! Нажмите кнопку для начала игры.")
label.pack()

button = tk.Button(root, text="Начать играть", command=button_click)
button.pack()

label = tk.Label(root, text="Вы можете нажать кнопку для получения правил игры.")
label.pack()

rules_button = tk.Button(root, text="Правила игры", command=show_rules)
rules_button.pack()

root.mainloop()