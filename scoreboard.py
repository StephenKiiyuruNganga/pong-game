from turtle import Turtle


FONT = ("Courier", 22, "normal")
ALIGNMENT = "center"


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.hideturtle()
        self.penup()
        self.write_text(f"Level: {self.level}", -220, 260)

    def increase_level(self):
        self.level += 1
        self.clear()
        self.write_text(f"Level: {self.level}", -220, 260)

    def write_text(self, text, x_cor=0, y_cor=0):
        """writes text on screen

        Arguments:
        :text: the text to be displayed
        :x_cor: x coordinate for the text. Default 0
        :y_cor: y coordinate for the text. Default 0
        """
        self.goto(x=x_cor, y=y_cor)
        self.write(text, align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.write_text(text="😔😔 GAME OVER 😔😔")
