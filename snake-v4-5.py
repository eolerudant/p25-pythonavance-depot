from random import randint
import pygame as pg

pg.init()

N=30 #nombre de cases du jeu 
taille=20 #taille des cases 
screen = pg.display.set_mode((N*taille, N*taille))
clock = pg.time.Clock()
snake = [
(10, 15),
(11, 15),
(12, 15),
]
def snake_draw(snake):
    for couple in snake :
        x,y=couple
        rect = pg.Rect(x*20, y*20, 20, 20)
        color = (255, 0, 0)
        pg.draw.rect(screen, color, rect)
    return

def moove(snake, direction):
    head_x, head_y = snake[-1]
    dir_x, dir_y = direction
    new_head = (head_x + dir_x, head_y + dir_y)

    snake.append(new_head)   # ajoute la nouvelle tête
    snake.pop(0)             # enlève la queue
    return snake

direction = (1, 0)
# on rajoute une condition à la boucle: si on la passe à False le programme s'arrête
running = True
while running:

    clock.tick(1)

    # on itère sur tous les évênements qui ont eu lieu depuis le précédent appel
    # ici donc tous les évènements survenus durant la seconde précédente
    for event in pg.event.get():
        # chaque évênement à un type qui décrit la nature de l'évênement
        # un type de pg.QUIT signifie que l'on a cliqué sur la "croix" de la fenêtre
        if event.type == pg.QUIT:
            running = False
        # un type de pg.KEYDOWN signifie que l'on a appuyé une touche du clavier
        elif event.type == pg.KEYDOWN:
            # si la touche est "Q" on veut quitter le programme
            if event.key == pg.K_q:
                running = False

    # xxx ici c'est discutable, car si on tape 'q'
    # on va quand même changer de couleur avant de sortir...

 
    for i in range (N):
        for j in range (N):
            x,y =taille*i, taille*j
            width, height = taille, taille
            rect = pg.Rect(x, y, width, height)
            if i%2==0 :
                if j%2==0:
                    color = (255, 255, 255)
                else :
                    color = (0, 0, 0) 
            else :
                if j%2==0 :
                    color = (0, 0, 0)
                else :
                    color = (255, 255, 255)
            
            pg.draw.rect(screen, color, rect)
    snake = moove(snake, direction)
    snake_draw(snake)
    pg.display.update()

# Enfin on rajoute un appel à pg.quit()
# Cet appel va permettre à Pygame de "bien s'éteindre" et éviter des bugs sous Windows
pg.quit()