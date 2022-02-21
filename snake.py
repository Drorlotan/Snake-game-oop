from turtle import Turtle, Screen

MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
class Snake:
    def __init__(self):
        self.segments = [0, 1, 2]
        for i in range(3):
            self.segments[i] = Turtle(shape="square")
            self.segments[i].penup()
            self.segments[i].back(20 * i)
            self.segments[i].color("white")
        self.head = self.segments[0]

    def extend(self):
        position_x = self.segments[-1].xcor()
        position_y = self.segments[-1].ycor()

        self.segments.append(Turtle(shape="square"))
        self.segments[-1].goto(position_x,position_y)
        self.segments[-1].color("white")
        self.segments[-1].penup()
    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
           self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)



    def check_tail(self):
        for segment in self.segments[1:]:
            if self.head.distance(segment) < 10:
                return True
        return False