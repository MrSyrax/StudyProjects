from turtle import Turtle , Screen

class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        with open('C:/Users/karey/Documents/Python/data/data.txt') as file:
            self.high_score = int(file.read())
        self.score = 0
        self.penup()
        self.hideturtle()
        self.color('white')
        self.goto(0,260)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f'Score: {self.score} High Score: {self.high_score}', align='center', font=('Arial', 24, 'normal'))

    def increase_score(self):
        self.score+=1
        self.update_scoreboard()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open('C:/Users/karey/Documents/Python/data/data.txt', 'w') as new_high:
                new_high.write(str(self.high_score))
        self.score = 0
        self.update_scoreboard()

