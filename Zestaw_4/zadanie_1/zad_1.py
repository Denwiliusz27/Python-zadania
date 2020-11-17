import pygame, sys
pygame.init()


def main():
    clock = pygame.time.Clock()  # pozwala na ustawienie fps

    pygame.display.set_caption("Pilka")  # nadaje tytul okienka
    icon = pygame.image.load("fifapyth.jpg")  # dodaje ikone w rogu okienka
    pygame.display.set_icon(icon)

    pygame.mixer.music.load("music.wav")  # dodaje muzyke
    pygame.mixer.music.play(-1)  # odtwarzanie w pętli

    window_size = window_width, window_height = 1000, 700  # rozmiary okienka
    window = pygame.display.set_mode(window_size)  # utworzone okienko

    background_image = pygame.image.load("football-field.jpg")  # ustawia obraz w tle
    background_image = pygame.transform.scale(background_image, window_size)  # nadaje mu wymiary okna

    surf_center = (  # wylicza srodek
        (window_width - background_image.get_width()) / 2,
        (window_height - background_image.get_height()) / 2
    )

    ball_size = b_width, b_heigh = 100, 100

    window.blit(background_image, surf_center)  # maluje tło
    ball = pygame.image.load("jabulani.png")
    ball = pygame.transform.scale(ball, ball_size)
    window.blit(ball, (window_width / 2, window_height / 2))
    ballrect = ball.get_rect(center=(window_width / 2, window_height / 2))
    pygame.display.flip()  # odswieza, przerysowuje

    speed = [0, 0]
    accel = [2, 2]
    time = 1

    while True:
        clock.tick(60)  # ustawia ilosc fps
        pygame.time.delay(50)  # ustawia opoznienie
        # print(clock.get_fps())

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        keys = pygame.key.get_pressed()

        if keys[pygame.K_ESCAPE]:
            sys.exit()
        elif keys[pygame.K_UP]:
            speed = [speed[0], speed[1] - time * accel[1]]
        elif keys[pygame.K_DOWN]:
            speed = [speed[0], speed[1] + time * accel[1]]
        elif keys[pygame.K_LEFT]:
            speed = [speed[0] - time * accel[0], speed[1]]
        elif keys[pygame.K_RIGHT]:
            speed = [speed[0] + time * accel[0], speed[1]]

        ballrect = ballrect.move(speed)
        if ballrect.right > window_width:
            speed[0] = -speed[0]
            ball_y = ballrect.centery
            ballrect = ball.get_rect(center=(window_width - b_width/2, ball_y))
        if ballrect.left < 0:
            speed[0] = -speed[0]
            ball_y = ballrect.centery
            ballrect = ball.get_rect(center=(b_width/2, ball_y))
        if  ballrect.bottom > window_height:
            speed[1] = -speed[1]
            ball_x = ballrect.centerx
            ballrect = ball.get_rect(center=(ball_x, window_height - b_heigh/2))
        if ballrect.top < 0:
            speed[1] = -speed[1]
            ball_x = ballrect.centerx
            ballrect = ball.get_rect(center=(ball_x, b_heigh/2))


        window.blit(background_image, surf_center)  # rysuje tlo w oknie
        window.blit(ball, ballrect)
        pygame.display.flip()  # przerysowuje wszystko


if __name__ == '__main__':
    main()
    pygame.quit()
    sys.exit()
