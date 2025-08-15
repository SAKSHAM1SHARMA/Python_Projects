import tkinter as tk
import random

# Constants
GAME_WIDTH = 600
GAME_HEIGHT = 600
SPACE_SIZE = 20
SNAKE_SPEED = 150  # milliseconds (higher = slower)
BODY_PARTS = 3
SNAKE_COLOR = "#00FF00"
FOOD_COLOR = "#FF0000"
BG_COLOR = "#000000"

class Snake:
    def __init__(self):
        self.body_size = BODY_PARTS
        self.coordinates = [[0, 0] for _ in range(BODY_PARTS)]
        self.squares = []

        for x, y in self.coordinates:
            square = canvas.create_rectangle(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=SNAKE_COLOR)
            self.squares.append(square)

class Food:
    def __init__(self):
        while True:
            x = random.randint(0, (GAME_WIDTH // SPACE_SIZE) - 1) * SPACE_SIZE
            y = random.randint(0, (GAME_HEIGHT // SPACE_SIZE) - 1) * SPACE_SIZE
            if [x, y] not in snake.coordinates:
                break
        self.coordinates = [x, y]
        self.food = canvas.create_oval(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=FOOD_COLOR)

def next_turn():
    x, y = snake.coordinates[0]

    if direction == "up":
        y -= SPACE_SIZE
    elif direction == "down":
        y += SPACE_SIZE
    elif direction == "left":
        x -= SPACE_SIZE
    elif direction == "right":
        x += SPACE_SIZE

    new_head = [x, y]

    if new_head == food.coordinates:
        snake.coordinates.insert(0, new_head)
        square = canvas.create_rectangle(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=SNAKE_COLOR)
        snake.squares.insert(0, square)
        canvas.delete(food.food)
        spawn_food()
    else:
        snake.coordinates.insert(0, new_head)
        square = canvas.create_rectangle(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=SNAKE_COLOR)
        snake.squares.insert(0, square)

        # Remove last segment
        canvas.delete(snake.squares[-1])
        del snake.squares[-1]
        del snake.coordinates[-1]

    if check_collisions():
        game_over()
    else:
        window.after(SNAKE_SPEED, next_turn)

def change_direction(new_dir):
    global direction

    opposites = {"up": "down", "down": "up", "left": "right", "right": "left"}
    if direction != opposites.get(new_dir):
        direction = new_dir

def check_collisions():
    x, y = snake.coordinates[0]

    # Wall collision
    if x < 0 or x >= GAME_WIDTH or y < 0 or y >= GAME_HEIGHT:
        return True

    # Self collision
    if [x, y] in snake.coordinates[1:]:
        return True

    return False

def game_over():
    canvas.delete(tk.ALL)
    canvas.create_text(GAME_WIDTH // 2, GAME_HEIGHT // 2 - 30, font=("Arial", 30), text="GAME OVER", fill="red")
    retry_button.place(relx=0.5, rely=0.55, anchor="center")

def restart_game():
    global snake, food, direction

    retry_button.place_forget()
    canvas.delete(tk.ALL)

    direction = "right"
    snake = Snake()
    spawn_food()
    next_turn()

def spawn_food():
    global food
    food = Food()

# Main window
window = tk.Tk()
window.title("Snake Game")
window.resizable(False, False)

# Canvas
canvas = tk.Canvas(window, bg=BG_COLOR, height=GAME_HEIGHT, width=GAME_WIDTH)
canvas.pack()

# Retry button
retry_button = tk.Button(window, text="Retry", font=("Arial", 14), command=restart_game)

# Bind controls
window.bind("<Up>", lambda event: change_direction("up"))
window.bind("<Down>", lambda event: change_direction("down"))
window.bind("<Left>", lambda event: change_direction("left"))
window.bind("<Right>", lambda event: change_direction("right"))

# Initialize
direction = "right"
snake = Snake()
food = Food()
next_turn()

# Start
window.mainloop()
