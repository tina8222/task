class SnakesLadders:
    
    def __init__(self):
        self.position = 0
        self.game_over = False

        # نردبان‌ها
        self.ladders = {
            2: 38, 7: 14, 8: 31, 15: 26, 21: 42,
            28: 84, 36: 44, 51: 67, 71: 91, 78: 98, 87: 94
        }

        # مارها
        self.snakes = {
            16: 6, 46: 25, 49: 11, 62: 19, 64: 60,
            74: 53, 89: 68, 92: 88, 95: 75, 99: 80
        }

    def play(self, die1, die2):
        if self.game_over:
            return "Game over!"

        move = die1 + die2
        self.position += move

        if self.position > 100:
            self.position = 100 - (self.position - 100)

        if self.position in self.ladders:
            self.position = self.ladders[self.position]

        elif self.position in self.snakes:
            self.position = self.snakes[self.position]

        if self.position == 100:
            self.game_over = True
            return "Player 1 Wins!"

        if die1 != die2:
            pass

        return f"Player 1 is on square {self.position}"
    
game = SnakesLadders()
print(game.play(1,1))
print(game.play(1,5))
print(game.play(3,3))
print(game.play(2,4))