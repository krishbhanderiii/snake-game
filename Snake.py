from turtle import Turtle

SNAKE_COLOR = "black"
POSITION = [(0, 0), (-20, 0), (-40, 0)]


class Snake:

    def __init__(self):
        self.segment = []
        self.Creat_Snake()

    def Creat_Snake(self):
        for index in POSITION:
            self.add_segment(index)

    def Mov(self):
        for seg_num in range(len(self.segment) - 1, 0, -1):
            X = self.segment[seg_num - 1].xcor()
            Y = self.segment[seg_num - 1].ycor()
            self.segment[seg_num].goto(X, Y)
        self.segment[0].forward(20)

    def Up(self):
        self.segment[0].setheading(90)

    def Down(self):
        self.segment[0].setheading(-90)

        # self.turtle.setheading(-90)
        # self.turtle.forward(10)

    def Left(self):
        self.segment[0].setheading(180)

        # new_heading = self.turtle.heading() + 10
        # self.turtle.setheading(new_heading)
        # self.turtle.forward(10)

    def Right(self):
        self.segment[0].setheading(360)

        # new_heading = self.turtle.heading() - 10
        # self.turtle.setheading(new_heading)
        # self.turtle.forward(10)

    def Check_GOVER(self):
        is_over = False

        if self.segment[0].xcor() > 300 or self.segment[0].xcor() < -300 or self.segment[0].ycor() > 300 or \
                self.segment[0].ycor() < -300:
            is_over = True
            return is_over
        else:
            return is_over

    def Head(self):
        return self.segment[0]

    def add_segment(self, index):
        turtle = Turtle("square")
        turtle.color(SNAKE_COLOR)
        turtle.penup()
        turtle.goto(index)
        self.segment.append(turtle)

    def extend(self):
        self.add_segment(self.segment[-1].position())

    def Reset(self):
        for seg in self.segment:
            seg.goto(1000, 1000)

        self.segment.clear()
        self.Creat_Snake()
