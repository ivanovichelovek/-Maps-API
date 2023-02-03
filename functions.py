import pygame
import requests



def painting(mas, coo_x, coo_y):
    map_request = f"http://static-maps.yandex.ru/1.x/?ll={float(coo_x)},{float(coo_y)}&spn={5 * (1 / float(mas[:-1]))},{5 * (1 / float(mas[:-1]))}&l=map"
    response = requests.get(map_request)

    if response:
        map_file = "map.png"
        with open(map_file, "wb") as file:
            file.write(response.content)

def detect(pos, d, mas, coo_x, coo_y):
    if (190 <= int(pos[0]) <= 490):
        if (460 <= int(pos[1]) <= 485):
            d = "x"
        elif (495 <= int(pos[1]) <= 520):
            d = "y"
        elif (530 <= int(pos[1]) <= 555):
            d = "m"
    elif (500 <= int(pos[0]) <= 600 and 495 <= int(pos[1]) <= 520):
        map_request = f"http://static-maps.yandex.ru/1.x/?ll={float(coo_x)},{float(coo_y)}&spn={5 * (1 / float(mas[:-1]))},{5 * (1 / float(mas[:-1]))}&l=map"
        response = requests.get(map_request)

        if response:
            map_file = "map.png"
            with open(map_file, "wb") as file:
                file.write(response.content)
    return d


def deistv(event, d, mas, coo_x, coo_y):
    if (event.type == pygame.KEYDOWN):
        if (event.key == pygame.K_BACKSPACE):
            if d == "m":
                mas = mas[:-2] + "%"
            elif d == "y":
                coo_y = coo_y[:-1]
            elif d == "x":
                coo_x = coo_x[:-1]
        if (event.key == 1102):
            if d == "m":
                mas = mas[:-1] + ".%"
            elif d == "y":
                coo_y += "."
            elif d == "x":
                coo_x += "."
        if (event.key == pygame.K_0):
            if d == "m":
                mas = mas[:-1] + "0%"
            elif d == "y":
                coo_y += "0"
            elif d == "x":
                coo_x += "0"
        if (event.key == pygame.K_1):
            if d == "m":
                mas = mas[:-1] + "1%"
            elif d == "y":
                coo_y += "1"
            elif d == "x":
                coo_x += "1"
        if (event.key == pygame.K_2):
            if d == "m":
                mas = mas[:-1] + "2%"
            elif d == "y":
                coo_y += "2"
            elif d == "x":
                coo_x += "2"
        if (event.key == pygame.K_3):
            if d == "m":
                mas = mas[:-1] + "3%"
            elif d == "y":
                coo_y += "3"
            elif d == "x":
                coo_x += "3"
        if (event.key == pygame.K_4):
            if d == "m":
                mas = mas[:-1] + "4%"
            elif d == "y":
                coo_y += "4"
            elif d == "x":
                coo_x += "4"
        if (event.key == pygame.K_5):
            if d == "m":
                mas = mas[:-1] + "5%"
            elif d == "y":
                coo_y += "5"
            elif d == "x":
                coo_x += "5"
        if (event.key == pygame.K_6):
            if d == "m":
                mas = mas[:-1] + "6%"
            elif d == "y":
                coo_y += "6"
            elif d == "x":
                coo_x += "6"
        if (event.key == pygame.K_7):
            if d == "m":
                mas = mas[:-1] + "7%"
            elif d == "y":
                coo_y += "7"
            elif d == "x":
                coo_x += "7"
        if (event.key == pygame.K_8):
            if d == "m":
                mas = mas[:-1] + "8%"
            elif d == "y":
                coo_y += "8"
            elif d == "x":
                coo_x += "8"
        if (event.key == pygame.K_9):
            if d == "m":
                mas = mas[:-1] + "9%"
            elif d == "y":
                coo_y += "9"
            elif d == "x":
                coo_x += "9"
        if event.key == 1073741899:
            if '.' in mas:
                mas = str(float(mas[:-1]) + 20) + "%"
            else:
                mas = str(int(mas[:-1]) + 20) + "%"
            painting(mas, coo_x, coo_y)
        if event.key == 1073741902:
            if float(mas[:-1]) >= 21:
                if '.' in mas:
                    mas = str(float(mas[:-1]) - 20) + "%"
                else:
                    mas = str(int(mas[:-1]) - 20) + "%"
            painting(mas, coo_x, coo_y)
        if event.key == pygame.K_LEFT:
            coo_x = str(float(coo_x) - 0.01)
            painting(mas, coo_x, coo_y)
        if event.key == pygame.K_RIGHT:
            coo_x = str(float(coo_x) + 0.01)
            painting(mas, coo_x, coo_y)
        if event.key == pygame.K_UP:
            coo_y = str(float(coo_y) + 0.01)
            painting(mas, coo_x, coo_y)
        if event.key == pygame.K_DOWN:
            coo_y = str(float(coo_y) - 0.01)
            painting(mas, coo_x, coo_y)
    return mas, coo_x, coo_y


def draw(screen, text, coords):
    font = pygame.font.Font(None, 31)
    text = font.render(text, True, (0, 0, 0))
    screen.blit(text, (coords[0], coords[1]))
