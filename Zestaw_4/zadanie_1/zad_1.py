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
    accel = [0.01, 0.01]

    while True:
        clock.tick(60)  # ustawia ilosc fps
        # print(clock.get_fps())
        pygame.time.delay(50)  # ustawia opoznienie

        for event in pygame.event.get():
            print(event)
            if event.type == pygame.QUIT:
                sys.exit()

        keys = pygame.key.get_pressed()

        if keys[pygame.K_ESCAPE]:
            sys.exit()
        elif keys[pygame.K_UP]:
            speed = [speed[0], speed[1] - ballrect.top * accel[1]]
        elif keys[pygame.K_DOWN]:
            speed = [speed[0], speed[1] + ballrect.bottom * accel[1]]
        elif keys[pygame.K_LEFT]:
            speed = [speed[0] - ballrect.left * accel[0], speed[1]]
        elif keys[pygame.K_RIGHT]:
            speed = [speed[0] + ballrect.right * accel[0], speed[1]]


        ballrect = ballrect.move(speed)
        if ballrect.left < 0 or ballrect.right > window_width:
            speed[0] = -speed[0]
        if ballrect.top < 0 or ballrect.bottom > window_height:
            speed[1] = -speed[1]

        window.blit(background_image, surf_center)  # rysuje tlo w oknie
        window.blit(ball, ballrect)
        pygame.display.flip()  # przerysowuje wszystko


if __name__ == '__main__':
    main()
    pygame.quit()
    sys.exit()
