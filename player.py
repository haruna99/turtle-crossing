from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super(Player, self).__init__()
        self.penup()
        self.shape("turtle")
        self.left(90)
        self.reset_position()

    def move(self):
        self.forward(MOVE_DISTANCE)

    def reset_position(self):
        self.goto(STARTING_POSITION)

    def at_finish_line(self):
        if self.ycor() > 280:
            return True
        else:
            return False

