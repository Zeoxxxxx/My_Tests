from utils import randCell

class Helicopter:
    
    def __init__(self, w, h):
        rc = randCell(w, h)
        rx, ry = rc[0], rc[1]
        self.x = rx
        self.y = ry
        self.h = h
        self.w = w
        self.tank = 0
        self.maxtank = 1
        self.score = 0
        self.lives = 20

# Движение
    def move(self, dx, dy):
        nx, ny = dx + self.x, dy + self.y
        if ( nx >= 0 and ny >= 0 and nx < self.h and ny < self.w):
            self.x, self.y = nx, ny

# Статистика
    def printStats(self):
        print("🧳", self.tank, "/", self.maxtank, sep = " ", end = " | ")
        print("🏆", self.score, end = " | ")
        print("💚", self.lives)
    
#💚 💵 🧳 🏆
