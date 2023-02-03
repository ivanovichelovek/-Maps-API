import pygame
import requests
from functions import detect, draw, deistv
from classes import Button


if __name__ == '__main__':
    pygame.init()
    pygame.display.set_caption('Большая задача по Maps')
    button_x = Button(190, 460, 300, 25, (0, 0, 0), 1)
    button_x_fon = Button(191, 461, 298, 23, (255, 255, 255), 0)
    button_y = Button(190, 495, 300, 25, (0, 0, 0), 1)
    button_y_fon = Button(191, 496, 298, 23, (255, 255, 255), 0)
    button_m = Button(190, 530, 300, 25, (0, 0, 0), 1)
    button_m_fon = Button(191, 531, 298, 23, (255, 255, 255), 0)
    fon = Button(0, 0, 600, 450, (255, 255, 255), 0)
    button_find = Button(500, 495, 100, 25, (0, 0, 0), 1)
    button_find_fon = Button(501, 496, 98, 23, (255, 255, 255), 0)
    running = True
    size = width, height = 600, 560
    screen = pygame.display.set_mode(size)
    map_request = "http://static-maps.yandex.ru/1.x/?ll=0,0&spn=5,5&l=map"
    response = requests.get(map_request)

    # Запишем полученное изображение в файл.
    map_file = "map.png"
    coo_x = "0"
    coo_y = "0"
    mas = "1%"
    d = "y"
    with open(map_file, "wb") as file:
        file.write(response.content)
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                mas, coo_x, coo_y = deistv(event, d, mas, coo_x, coo_y)
                if coo_x and '.' not in coo_x:
                    coo_x = str(int(coo_x))
                elif coo_y and '.' not in coo_y:
                    coo_y = str(int(coo_y))
                elif mas != "%" and '.' not in mas:
                    mas = str(int(mas[:-1])) + "%"
            elif event.type == pygame.MOUSEBUTTONDOWN:
                d = detect(pygame.mouse.get_pos(), d, mas, coo_x, coo_y)
        screen.fill((255, 255, 200))
        fon.render(screen)
        button_x.render(screen)
        button_x_fon.render(screen)
        button_y.render(screen)
        button_y_fon.render(screen)
        button_m.render(screen)
        button_m_fon.render(screen)
        button_find.render(screen)
        button_find_fon.render(screen)
        screen.blit(pygame.image.load(map_file), (0, 0))
        draw(screen, "Координаты по x", [1, 461])
        draw(screen, "Координаты по y", [1, 496])
        draw(screen, coo_x, [191, 463])
        draw(screen, coo_y, [191, 498])
        draw(screen, "Найти", [501, 496])
        draw(screen, "Масштаб", [1, 531])
        draw(screen, mas, [191, 531])
        pygame.display.flip()
