import random


class SnakeModel:
    def __init__(self):
        self.lives = 5
        self.body = [
            [200, 200],
            [200, 210],
            [200, 220],
            [200, 230]
        ]
        self.direction = "Up"
        self.fruit = [0, 0]
        self.set_fruit_position()

    def set_fruit_position(self):
        x = random.randint(1, 400)
        y = random.randint(1, 400)
        xd = x % 10
        yd = y % 10
        x = x - xd
        y = y - yd

        if x > 390:
            x = 390
        elif x < 10:
            x = 10

        if y > 390:
            y = 390
        elif y < 10:
            y = 10

        self.fruit = [x, y]

    def move_body_parts(self):
        for i in range(len(self.body)-1, 0, -1):
            self.body[i][0] = self.body[i - 1][0]
            self.body[i][1] = self.body[i - 1][1]

    def eat_fruit(self):
        if self.fruit[0] == self.body[0][0] and self.fruit[1] == self.body[0][1]:
            self.body.append([self.body[-1][0], self.body[-1][1]])
            self.set_fruit_position()

    def move_up(self):
        if self.direction != "Down":
            if self.body[0][1] == 0:
                self.lives -= 1
                if self.lives == 0:
                    print("Game Over")
                    # exit()
            else:
                self.move_body_parts()
                self.body[0][1] -= 10
                self.direction = "Up"
                self.eat_fruit()

    def move_down(self):
        if self.direction != "Up":
            if self.body[0][1] == 390:
                self.lives -= 1
                if self.lives == 0:
                    print("Game Over")
                    # exit()
            else:
                self.move_body_parts()
                self.body[0][1] += 10
                self.direction = "Down"
                self.eat_fruit()

    def move_left(self):
        if self.direction != "Right":
            if self.body[0][0] == 0:
                self.lives -= 1
                if self.lives == 0:
                    print("Game Over")
                    # exit()
            else:
                self.move_body_parts()
                self.body[0][0] -= 10
                self.direction = "Left"
                self.eat_fruit()

    def move_right(self):
        if self.direction != "Left":
            if self.body[0][0] == 390:
                self.lives -= 1
                if self.lives == 0:
                    print("Game Over")
                    # exit()
            else:
                self.move_body_parts()
                self.body[0][0] += 10
                self.direction = "Right"
                self.eat_fruit()


if __name__ == '__main__':
    model = SnakeModel()
    print(model.body)
    model.move_up()
    print(model.body)

