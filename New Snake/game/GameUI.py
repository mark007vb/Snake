from tkinter import Tk, Canvas
from SnakeModel import SnakeModel


# EXERCISE 1: Make fruit appear 10 pixels away from the border
# EXERCISE 2: When snake head hits the border, don't move out of canvas
#             decrease lives, and if lives becomes ZERO, game over.


def key_pressed(e):
    key = e.keysym
    if model.lives > 0:
        if key == "Down":
            model.move_down()
        elif key == "Up":
            model.move_up()
        elif key == "Left":
            model.move_left()
        elif key == "Right":
            model.move_right()
    canvas.delete("all")
    display_snake()
    display_lives(model.lives)
    if model.lives == 0:
        model.fruit = [410, 410]
        canvas.create_text(200, 200, text="GAME OVER", fill="red", font=("Arial", 30))
        window.after(2000, window.quit)
    canvas.create_rectangle(model.fruit[0], model.fruit[1], model.fruit[0] + 10, model.fruit[1] + 10, fill="red")


def display_snake():
    for bp in model.body:
        canvas.create_rectangle(bp[0], bp[1], bp[0] + 10, bp[1] + 10, fill="green")

def display_lives(snake_lives):
    canvas.create_rectangle(300, 0, 400, 20, fill="white", outline="white", stipple="gray25")
    canvas.create_text(350, 10, text=f"Lives: {snake_lives}", fill="black", font=("Arial", 11), stipple="gray25")


window = Tk()
model = SnakeModel()

canvas = Canvas(window, bg="white", width=400, height=400)
canvas.grid(row=0, column=0)

display_snake()
display_lives(model.lives)

canvas.create_rectangle(model.fruit[0], model.fruit[1], model.fruit[0] + 10, model.fruit[1] + 10, fill="red")
window.bind('<KeyRelease>', key_pressed)

window.mainloop()
