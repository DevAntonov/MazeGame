import turtle
from math import sqrt
from random import choice, randint

#
#
#

# Променлива за обект, извеждащ екрана
windowScreen = turtle.Screen()
# Задаване на цвят на фона
windowScreen.bgcolor("black")
# Задаване на заглавие на екрана
windowScreen.title("MazeGame")
# Задаване на големината на екрана
windowScreen.setup(800, 1000)
windowScreen.tracer(0)

# Регистриране на изображенията
turtle.register_shape("avatar.gif")
turtle.register_shape("brickwall.gif")
turtle.register_shape("money.gif")
turtle.register_shape("enemy.gif")
turtle.register_shape("portal.gif")
turtle.register_shape("wooden.gif")
turtle.register_shape("npc.gif")

# Променливи за броя точки опит за всяко ниво, които
# играча трябва да има играча и добавянето им в списък
LEVEL_1 = 500
LEVEL_2 = 2000
LEVEL_3 = 5000
LEVEL_4 = 10000
LEVEL_5 = 20000
hero_levels_exp_requirements = [LEVEL_1, LEVEL_2, LEVEL_3, LEVEL_4, LEVEL_5]

# Конструкцията на нивата
level_1 = [
    "$$$$$$$$$$$$$$$$$$$$$$$$$$$$",
    "$P        $$$$$$$$$$$$$$$$$$",
    "$$$$$$$   $$$$$$$$$$$$$$$$$$",
    "$$$$$$$            M$$$$$$$$",
    "$$$$$$$             $$$$$$$$",
    "$$$$$$$             $$$$$$$$",
    "$$$$$$$   $$$$$$$   $$$$$$$$",
    "$$$$$$$   $$$$$$$   $$$$$$$$",
    "$$$$$$$   $$$$$$$   $$$$$$$$",
    "$$$$$$$             $$$$$$$$",
    "$$$$$$$E                  0$",
    "$$$$$$$$$$$$$$$$$$$$$$$$$$$$",
    "!!!!!!!!!!!!!!!!!!!!!!!!!!!!",
    "!!$!!$!$$$$!$!!!!$!!!!!$$$!!",
    "!!$!!$!$!!!!$!!!!$!!!!$!!!$!",
    "!!$$$$!$$$$!$!!!!$!!!!$!!!$!",
    "!!$!!$!$!!!!$!!!!$!!!!$!!!$!",
    "!!$!!$!$$$$!$$$$!$$$$!!$$$!!",
    "!!!!!!!!!!!!!!!!!!!!!!!!!!!!",
    "!!!!!!!!!!!!!!!!!!!!!!!!!!!!",
    "!!!!!!!!!!!!!!!!!!!!!!!!!!!!",
    "!!!!!!!!!!!!!!!!!!!!!!!!!!!!",
    "!!!!!!!!!!!!!!!!!!!!!!!!!!!!",
    "!!!!!!!!!!!!!!!!!!!!!!!!!!!!",
    "!!!!!!!!!!!!!!!!!!!!!!!!!!!!",
    "!!!!!!!!!!!!!!!!!!!!!!!!!!!!",
    "!!!!!!!!!!!!!!!!!!!!!!!!!!!!"]

level_2 = [
    "$$$$$$$$$$$$$$$$$$$$$$$$$$$$",
    "$P      $$$$$$$$$$$$$$$$$$$$",
    "$$$$      $        $$$$$$$$$",
    "$$$$$$$$  $$$$  $$$$$$$$$$$$",
    "$$$$$M $  $     $  $$$$$$$$$",
    "$$$$$  $  $  $$$$  $$$$$$$$$",
    "$$$$$             E$$$$$$$$$",
    "$$$$$$$$  $  $$$$$$$$$$$$$$$",
    "$$$$$     $     $  $$$$$$$$$",
    "$$$$$  $  $  $$$$  $$$$$$$$$",
    "$$$$$M $  $E       $$$$$$$$$",
    "$$$$$$$$$$$$$$$$$     0$$$$$",
    "$$$$$$$$$$$$$$$$$$$$$$$$$$$$",
    "!!!!!!!!!!!!!!!!!!!!!!!!!!!!",
    "!!!!!!!!!!!!!!!!!!!!!!!!!!!!",
    "!!!!!!!!!!!!!!!!!!!!!!!!!!!!",
    "!!!!!!!!!!!!!!!!!!!!!!!!!!!!",
    "!!!!!!!!!!!!!!!!!!!!!!!!!!!!",
    "!!!!!!!!!!!!!!!!!!!!!!!!!!!!",
    "!!!!!!!!!!!!!!!!!!!!!!!!!!!!",
    "!!!!!!!!!!!!!!!!!!!!!!!!!!!!",
    "!!!!!!!!!!!!!!!!!!!!!!!!!!!!",
    "!!!!!!!!!!!!!!!!!!!!!!!!!!!!",
    "!!!!!!!!!!!!!!!!!!!!!!!!!!!!",
    "!!!!!!!!!!!!!!!!!!!!!!!!!!!!",
    "!!!!!!!!!!!!!!!!!!!!!!!!!!!!",
    "!!!!!!!!!!!!!!!!!!!!!!!!!!!!",
    "!!!!!!!!!!!!!!!!!!!!!!!!!!!!"]

level_3 = [
    "$$$$$$$$$$$$$$$$$$$$$$$$$$$$",
    "$P  $$$$$$$$$$$$$$$$$$$$$$$$",
    "$            $        $M $$$",
    "$$$$$  $$$$$$$  $  $$$$  $$$",
    "$$     $  $  $  $E       $$$",
    "$$  $$$$  $  $$$$$$$$$$  $$$",
    "$$  $  $     $  $ M$     $$$",
    "$$  $  $  $$$$  $  $  $$$$$$",
    "$$        $     $     $M $$$",
    "$$$$$  $$$$  $  $$$$  $  $$$",
    "$$E       $  $E       $  $$$",
    "$$$$$$$$  $  $  $  $$$$  $$$",
    "$$     $     $  $     $  $$$",
    "$$  $  $  $$$$$$$$$$  $  $$$",
    "$$ M$     $  $  $  $     $$$",
    "$$$$$$$$  $  $  $  $  $$$$$$",
    "$$           $           $$$",
    "$$$$$$$$$$$$$$$$$$$$$$$   0$",
    "$$$$$$$$$$$$$$$$$$$$$$$$$$$$",
    "!!!!!!!!!!!!!!!!!!!!!!!!!!!!",
    "!!!!!!!!!!!!!!!!!!!!!!!!!!!!",
    "!!!!!!!!!!!!!!!!!!!!!!!!!!!!",
    "!!!!!!!!!!!!!!!!!!!!!!!!!!!!",
    "!!!!!!!!!!!!!!!!!!!!!!!!!!!!",
    "!!!!!!!!!!!!!!!!!!!!!!!!!!!!",
    "!!!!!!!!!!!!!!!!!!!!!!!!!!!!",
    "!!!!!!!!!!!!!!!!!!!!!!!!!!!!",
    "!!!!!!!!!!!!!!!!!!!!!!!!!!!!"]

level_4 = [
    "$$$$$$$$$$$$$$$$$$$$$$$$$$$$",
    "$ P               $     $  $",
    "$  $$$$  $  $$$$$$$  $  $  $",
    "$  $  $  $     $M    $     $",
    "$  $  $$$$  $$$$$$$$$$  $  $",
    "$  $           $     $  $  $",
    "$$$$$$$$$$  $$$$  $  $$$$  $",
    "$     $           $E       $",
    "$  $  $  $  $$$$  $$$$  $  $",
    "$M $  $  $     $     $  $M $",
    "$$$$  $$$$$$$$$$  $$$$$$$$$$",
    "$     $E                   $",
    "$  $$$$  $  $$$$  $  $$$$  $",
    "$     $  $     $  $  $  $  $",
    "$$$$  $$$$  $$$$  $  $  $$$$",
    "$              $  $        $",
    "$$$$$$$$$$  $$$$$$$  $  $  $",
    "$          E$M       $  $  $",
    "$  $$$$$$$$$$$$$$$$$$$  $$$$",
    "$      $           $$$    M$",
    "$  $$$$$  $$$$$$   $ $$$$$$$",
    "$  $      $N $$$ $$$       $",
    "$  $ $$$$$$$W$   $$$$$  $$$$",
    "$    $       $    $$$$ $$$$$",
    "$  $$$$$$$$  $$$$ $$      $$",
    "$  $E        $    $$  $$$  $",
    "$     $$$$$$$$  $       $ 0$",
    "$$$$$$$$$$$$$$$$$$$$$$$$$$$$"]

level_5 = [
    "$$$$$$$$$$$$$$$$$$$$$$$$$$$$",
    "$P       $  $  $  $    M$  $",
    "$$$$  $$$$  $  $  $  $$$$  $",
    "$$$$  $  $E                $",
    "$$$$  $  $$$$  $  $$$$$$$$$$",
    "$M $     $  $  $     $M    $",
    "$  $$$$  $  $$$$$$$  $$$$  $",
    "$     $           $     $  $",
    "$$$$  $$$$  $  $  $  $$$$  $",
    "$E          $  $     $  $  $",
    "$  $$$$$$$  $$$$$$$$$$  $  $",
    "$  $E          $ M$        $",
    "$  $  $$$$$$$$$$  $$$$$$$  $",
    "$  $        $              $",
    "$  $$$$$$$  $$$$$$$  $$$$  $",
    "$  $     $E             $E $",
    "$  $  $  $$$$  $$$$  $  $$$$",
    "$  $  $  $  $     $  $     $",
    "$  $  $  $  $  $  $$$$$$$$$$",
    "$  $ M$        $  $     $  $",
    "$  $$$$  $  $  $$$$$$$  $  $",
    "$     $  $  $E             $",
    "$$$$  $  $$$$$$$  $$$$$$$  $",
    "$  $  $     $  $  $     $  $",
    "$  $$$$$$$  $  $$$$$$$  $  $",
    "$E               $         $",
    "$$$$$$$$$$$$$$$$$$$$$$$$$ 0$",
    "$$$$$$$$$$$$$$$$$$$$$$$$$$$$"]


# Клас "Писалка за чертаене"
class DrawingPen(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.shape("blank")
        self.color("black")
        self.penup()
        self.speed(0)


# Клас "Играч"
class Player(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("avatar.gif")
        self.color("blue")
        self.penup()
        self.speed(0)
        self.money = 100
        self.exp_pts = 0
        self.level = 0
        self.bullets = 3
        self.currentLevel = 1

    # Функция за придвижване нагоре
    def up(self):
        # Пресмятане на следващия ход и проверка дали точката
        # на следващия ход съвпада с точка на някоя стена
        if (player.xcor(), player.ycor() + 28) not in wallsList:
            self.setheading(90)
            self.forward(28)

    # Функция за придвижване надолу
    def down(self):

        if (player.xcor(), player.ycor() - 28) not in wallsList:
            self.setheading(270)
            self.forward(28)

    # Функция за придвижване наляво
    def left(self):

        if (player.xcor() - 28, player.ycor()) not in wallsList:
            self.setheading(180)
            self.forward(28)

    # Функция за придвижване надясно
    def right(self):

        if (player.xcor() + 28, player.ycor()) not in wallsList:
            self.setheading(0)
            self.forward(28)

    # Функция за излизане от играта
    def exit_game(self):
        windowScreen.bye()

    # функцията "сблъсък" за проверка на разстоянието между две точки
    def collision(self, obj):
        # Изчисляване на разстоянието с помоща на питагоровата теорема
        distance = sqrt(((self.xcor() - obj.xcor()) ** 2) + ((self.ycor() - obj.ycor()) ** 2))

        if distance < 5:
            return True
        else:
            return False

    # Функция за купуване на куршуми от играча
    def buy_bullets(self):
        if self.money >= 50:
            self.bullets += 1
            self.money -= 50
            show_bullets_quantity()
            show_money()

    # Функция за качване на нивото на героят
    def levelup(self):

        # Проверка дали героят е натрупал достатъчно точки опит
        if self.exp_pts >= hero_levels_exp_requirements[self.level]:
            self.level += 1
            bullet.speed += 1
            show_hero_level()

    # Функция за скриване
    def hide(self):
        self.goto(5000, 5000)
        self.hideturtle()


# Клас "Неигрови персонаж"
class NPC(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("npc.gif")
        self.color("blue")
        self.penup()
        self.speed(0)

    def hide(self):
        self.goto(5000, 5000)
        self.hideturtle()


# Клас "Препятствие"
class Obstacle(turtle.Turtle):
    def __init__(self, x, y):
        turtle.Turtle.__init__(self)
        self.shape("wooden.gif")
        self.color("blue")
        self.penup()
        self.speed(0)
        self.goto(x, y)
        wallsList.append((x, y))

    def hide(self):
        self.goto(2000, 2000)
        self.hideturtle()


# Клас "Противник"
class Enemy(turtle.Turtle):
    def __init__(self, x, y):
        turtle.Turtle.__init__(self)
        self.shape("enemy.gif")
        self.color("yellow")
        self.penup()
        self.speed(0)
        self.goto(x, y)
        # Запазване на определената, чрез случаен избор, посока
        self.direction = choice(["Up", "Down", "Left", "Right"])

    # Функция за придвижване на противника
    def enemy_move(self):

        # Пресмятане на следващия ход на противника
        if self.direction == "Up":
            self.setheading(90)
            x = self.xcor()
            y = self.ycor() + 28
        elif self.direction == "Down":
            self.setheading(270)
            x = self.xcor()
            y = self.ycor() - 28
        elif self.direction == "Left":
            self.setheading(180)
            x = self.xcor() - 28
            y = self.ycor()
        elif self.direction == "Right":
            self.setheading(0)
            x = self.xcor() + 28
            y = self.ycor()
        else:
            x = self.xcor()
            y = self.ycor()

        if self.sense(player):
            if player.xcor() < self.xcor():
                self.direction = "Left"
            elif player.xcor() > self.xcor():
                self.direction = "Right"
            elif player.ycor() > self.ycor():
                self.direction = "Up"
            elif player.xcor() < self.xcor():
                self.direction = "Down"

        if (x, y) not in wallsList:
            self.forward(28)
        else:
            self.direction = choice(["Up", "Down", "Left", "Right"])

        turtle.ontimer(self.enemy_move, t=randint(500, 500))

    # Функция за проверяване дали героят на играча е наблизо
    def sense(self, obj):
        distance = sqrt(((self.xcor() - obj.xcor()) ** 2) + ((self.ycor() - obj.ycor()) ** 2))

        if distance < 112:
            return True
        else:
            return False

    def hide(self):
        self.goto(2000, 2000)
        self.hideturtle()


# Клас "Пари"
class Money(turtle.Turtle):
    def __init__(self, x, y):
        turtle.Turtle.__init__(self)
        self.shape("money.gif")
        self.color("green")
        self.penup()
        self.speed(0)
        self.goto(x, y)

    def hide(self):
        self.goto(3000, 3000)
        self.hideturtle()


# Клас "Куршум"
class Bullet(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shapesize(stretch_wid=0.2, stretch_len=0.2, outline=None)
        self.hideturtle()
        self.goto(-2000, 2000)
        self.shape('circle')
        self.color("yellow")
        self.status = "ready"
        self.penup()
        self.speed = 3

    # Функция за изстрелване на куршум
    def fire(self):
        if self.status == "ready" and player.bullets > 0:
            self.hideturtle()
            self.goto(player.xcor(), player.ycor())
            self.showturtle()
            self.setheading(player.heading())
            player.bullets -= 1
            show_bullets_quantity()

        self.status = "firing"

    # Функция за придвижване на куршум
    def bullet_move(self):
        if self.status == "firing":
            self.fd(self.speed)

    def collision(self, obj):
        distance = sqrt(((self.xcor() - obj.xcor()) ** 2) + ((self.ycor() - obj.ycor()) ** 2))

        if distance < 15:
            return True
        else:
            return False

    def wallcollision(self, x, y):
        x = self.xcor() - x
        y = self.ycor() - y
        distance = sqrt((x ** 2) + (y ** 2))

        if distance < 15:
            return True
        else:
            return False

    def hide(self):
        self.goto(3000, 3000)
        self.hideturtle()
        self.status = "ready"


# Клас "Портал"
class Portal(turtle.Turtle):
    def __init__(self, x, y):
        turtle.Turtle.__init__(self)
        self.hideturtle()
        self.shape("portal.gif")
        self.color("green")
        self.penup()
        self.speed(0)
        self.experience_points = 100
        self.goto(x, y)
        self.showturtle()

    def destroy(self):
        self.hideturtle()
        self.goto(2000, 2000)


# функция за показване сегашното нивото на екрана
def show_level():
    level_pen.undo()
    level_pen.color("white")
    level_pen.goto(-75, 410)
    scorestring = "LEVEL {}".format(player.currentLevel)
    level_pen.write(scorestring, False, align="left", font=("arial", 20, "bold"))


# Функция за показване на броя на оставащите куршуми на героя
def show_bullets_quantity():
    bullets_quantity_pen.undo()
    bullets_quantity_pen.color("white")
    bullets_quantity_pen.goto(-400, 450)
    scorestring = "Bullets left: {}".format(player.bullets)
    bullets_quantity_pen.write(scorestring, False, align="left", font=("arial", 14, "bold"))


# Функция за показване нивото на героя
def show_hero_level():
    hero_level_pen.undo()
    hero_level_pen.color("white")
    hero_level_pen.goto(-400, 470)
    scorestring = "Hero level: {}".format(player.level)
    hero_level_pen.write(scorestring, False, align="left", font=("arial", 14, "bold"))


# Функция за показване парите на героя
def show_money():
    score_pen.undo()
    score_pen.color("white")
    score_pen.goto(-400, 430)
    scorestring = "Money: {}".format(player.money)
    score_pen.write(scorestring, False, align="left", font=("arial", 14, "bold"))


# Функция за показване точките опит на героя
def show_exp_pts():
    points_pen.undo()
    points_pen.color("white")
    points_pen.goto(-400, 410)
    scorestring = "Experience Points: {}".format(player.exp_pts)
    points_pen.write(scorestring, False, align="left", font=("arial", 14, "bold"))

def won_game():
    won_game_pen.undo()
    won_game_pen.color("white")
    won_game_pen.goto(0, 0)
    scorestring = "GAME WON!"
    won_game_pen.write(scorestring, False, align="center", font=("arial", 30, "bold"))

# Функция за конструиране на нивото
def levelSetup(level):
    pen.clear()
    for y in range(len(level)):
        for x in range(len(level[y])):
            char = level[y][x]
            line_x = -392 + (x * 28)
            line_y = 392 - (y * 28)

            # Проверка дали има знак $ (представляващ стена)
            if char == "$":
                pen.goto(line_x, line_y)
                pen.shape("brickwall.gif")
                pen.stamp()
                wallsList.append((line_x, line_y))

            # Проверка дали има знак ! (представляващ черен квадрат)
            if char == "!":
                pen.goto(line_x, line_y)
                pen.shape("square")
                pen.stamp()
                wallsList.append((line_x, line_y))

            # Проверка дали има буква W (представляваща дървено препятствие)
            if char == "W":
                pen.goto(line_x, line_y)
                pen.shape("wooden.gif")
                obstacles.append(Obstacle(line_x, line_y))

            # Проверка дали има буква P (представляваща героя)
            if char == "P":
                player.goto(line_x, line_y)
                player.showturtle()

            # Проверка дали има буква N (представляваща неигрови персонаж)
            if char == "N":
                npc.goto(line_x, line_y)

            # Проверка дали има буква Е (представляваща противник)
            if char == "E":
                enemiesList.append(Enemy(line_x, line_y))

            # Проверка дали има буква М (представляваща пари)
            if char == "M":
                moneyAccount.append(Money(line_x, line_y))

            # Проверка дали има цифра 0 (представляваща портал)
            if char == "0":
                portalsList.append(Portal(line_x, line_y))


levelsList = [""]  # Списък с нива
wallsList = []  # Списък със стени
enemiesList = []  # Списък с противници
moneyAccount = []  # Списък с пари
portalsList = []  # Списък с портали
bulletsList = []  # Списък с куршуми
obstacles = []  # Списък с препятствия

# Добавяне на нивата в списъка с нива
levelsList.append(level_1)
levelsList.append(level_2)
levelsList.append(level_3)
levelsList.append(level_4)
levelsList.append(level_5)

# Обекти, участващи в конструкцията на нивата
pen = DrawingPen()
score_pen = DrawingPen()
points_pen = DrawingPen()
hero_level_pen = DrawingPen()
bullets_quantity_pen = DrawingPen()
level_pen = DrawingPen()
won_game_pen = DrawingPen()

player = Player()  # Създаване на обект "играч" от тип "Играч"
npc = NPC()  # Създаване на обект "неигрови персонаж" от тип "Неигрови персонаж"
bullet = Bullet()  # Създаване на обект "Куршум" от тип "Куршум"

level = 1  # Променлива за сегашното ниво
levelSetup(levelsList[1])
next_level = False

turtle.listen()

# Свързване на функции с клавиши за управление чрез клавиатурата
windowScreen.onkeypress(player.up, "w")
windowScreen.onkeypress(player.up, "Up")
windowScreen.onkeypress(player.down, "s")
windowScreen.onkeypress(player.down, "Down")
windowScreen.onkeypress(player.right, "d")
windowScreen.onkeypress(player.right, "Right")
windowScreen.onkeypress(player.left, "a")
windowScreen.onkeypress(player.left, "Left")
windowScreen.onkeypress(bullet.fire, "space")
windowScreen.onkeypress(player.buy_bullets, "b")
windowScreen.onkeypress(player.exit_game, "Escape")

for enemy in enemiesList:
    turtle.ontimer(enemy.enemy_move, t=500)

while True:
    windowScreen.update()
    show_money()
    show_exp_pts()
    show_hero_level()
    show_bullets_quantity()
    show_level()
    bullet.bullet_move()

    # Проверка дали играча трябва да премине на следващото ниво
    if next_level:
        next_level = False
        level += 1
        wallsList.clear()

        for money in moneyAccount:
            money.hide()

        for enemy in enemiesList:
            enemy.hide()

        moneyAccount.clear()
        enemiesList.clear()
        levelSetup(levelsList[level])
        
        for enemy in enemiesList:
            turtle.ontimer(enemy.enemy_move, t=500)

    # Проверка дали играча се "сблъсква" с неигрови персонаж
    if player.collision(npc):
        npc.hide()
        player.exp_pts += 1000

    # Проверка дали играча се "сблъсква" с пари
    for money in moneyAccount:
        if player.collision(money):
            player.money += 100
            money.hide()
            moneyAccount.remove(money)

    for portal in portalsList:

        # Проверка дали играча се "сблъсква" с портал
        if player.collision(portal):
            if player.currentLevel == 6:
                wallsList.clear()

                for money in moneyAccount:
                    money.hide()

                for enemy in enemiesList:
                    enemy.hide()

                moneyAccount.clear()
                enemiesList.clear()
                while True:
                    won_game()
            else:
                player.exp_pts += portal.experience_points
                player.currentLevel += 1

                portal.destroy()

                portalsList.remove(portal)
                next_level = True




    # Проверка дали изстрелян куршум се "сблъсква" с препятствие
    # като при установен сблъсък препятствието изчезва
    for obstacle in obstacles:
        if bullet.collision(obstacle):
            bullet.hide()
            obstacle.hide()
            obstacles.remove(obstacle)

    # Проверка дали изстрелян куршум се "сблъсква" със стена
    for (xcor, ycor) in wallsList:
        if bullet.wallcollision(xcor, ycor):
            bullet.hide()

    # Проверка дали противника се "сблъсква" с героят на играча
    # или с куршум. Ако има сблъсък с играча, играча загива, а ако
    # сблъсък с куршум, противника загива
    for enemy in enemiesList:
        if player.collision(enemy):
            player.hide()

        elif bullet.collision(enemy):
            player.exp_pts += 100
            enemy.hide()
            bullet.hide()
