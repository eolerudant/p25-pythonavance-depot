from random import randint
import pygame as pg
import random

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
    if new_head in snake :
        return False         #si la nouvelle tete est déja dans le serpent game over

    snake.append(new_head)   # ajoute la nouvelle tête
    snake.pop(0)             # enlève la queue
    return snake
def create_fruit():
    fruit = random.randint(0, 29), random.randint(0, 29)
    return fruit

def draw_fruit(fruit):
    x,y=fruit
    rect = pg.Rect(x*20, y*20, 20, 20)
    color = (0, 255, 0)
    pg.draw.rect(screen, color, rect)
    

def eat(snake, fruit, score):
    if snake[-1] == fruit :
        snake.insert(0, snake[0])
        fruit=create_fruit()
        draw_fruit(fruit)
        score+=1
    return fruit, snake, score 
    

    

# on rajoute une condition à la boucle: si on la passe à False le programme s'arrête
running = True
fruit = create_fruit()
direction=(1,0) #initialise le mouvement pour eviter le false dans l'appel de la fonction moove
score = 0
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
            if event.key == pg.K_DOWN :
                direction = (0,1)
            elif event.key == pg.K_UP :
                direction = (0,-1)
            elif event.key == pg.K_RIGHT :
                direction = (1,0)
            elif event.key == pg.K_LEFT :
                direction = (-1,0)
        
        


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
    draw_fruit(fruit)
    snake_draw(snake)
    eat(snake, fruit, direction)
    snake = moove(snake, direction)
    
    pg.display.set_caption(f"Score: {score}")

    pg.display.update()

# Enfin on rajoute un appel à pg.quit()
# Cet appel va permettre à Pygame de "bien s'éteindre" et éviter des bugs sous Windows
pg.quit()