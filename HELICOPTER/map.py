from utils import randBool, randCell, randCell2
# 🎄 🌊 🚁🟩 🔥 🏥 💚 💵 🧳 🏆 🔲⚡⛅

#0 - поле
#1 - деревья
#2 - река
#3 - госпиталь
#4 - апгрейд
#5 - огонь

CELL_TYPES = "🟩🎄🌊🏥💵🔥"

class Map:
##############################################    СИСТЕМНЫЕ   ###########################################################

   # Инициализатор
    def __init__(self, w, h):
        self.w = w
        self.h = h
        self.cells = [[0 for i in range(w)] for j in range(h)]

   # Проверка границ
    def check_bound(self, x, y):
        if (x < 0 or y < 0 or x >= self.h or y >= self.w):
            return False
        return True
                    
    # Вывод карты
    def print_map(self, helico):
        print('🔲' * (self.w + 2))

        for ri in range(self.h):

            print('🔲', end = "")

            for ci in range(self.w):
                cell = self.cells[ri][ci]
                
                if (helico.x == ri and helico.y == ci):
                    print('🚁', end ="")

                elif (cell >= 0 and cell < len(CELL_TYPES)):
                    print(CELL_TYPES[cell], end = "")
                    
            print('🔲')
        print('🔲' * (self.w + 2))

##############################################    ГЕНЕРАТОРЫ   ###########################################################

    # Генерация реки
    def generate_river(self, l): # это L маленькая
        rc = randCell(self.w, self.h)
        rx, ry = rc[0], rc[1]
        self.cells[rx][ry] = 2
        while l > 0:
            rc2 = randCell2(rx, ry)
            rx2, ry2 = rc2[0], rc2[1]
            if (self.check_bound(rx2, ry2)):
                self.cells[rx2][ry2] = 2
                rx, ry  = rx2, ry2
                l -= 1

    # Генерация леса
    def generate_forest(self, r, mxr):
        for ri in range(self.h):
            for ci in range(self.w):
                if randBool(r, mxr):
                    self.cells[ri][ci] = 1

    # Обновление деревьев
    def generate_tree(self):
        c = randCell(self.w, self.h)
        cx, cy = c[0], c[1]
        if (self.check_bound(cx, cy) and self.cells[cx][cy] == 0):
            self.cells[cx][cy] = 1

##############################################    ОГОНЬ   ###########################################################

    # добавление огня
    def add_fire(self):
        c = randCell(self.w, self.h)
        cx, cy = c[0], c[1]
        if self.cells[cx][cy] == 1:
            self.cells[cx][cy] = 5

    # Обновление огня
    def update_fire(self):
        for ri in range(self.h):
            for ci in range(self.w):
                cell = self.cells[ri][ci]
                if cell == 5:
                    self.cells[ri][ci] = 0
        for i in range(10):
            self.add_fire()

##############################################    ВЕРТОЛЕТ   ###########################################################

    def processHelico(self, helico):
        c = self.cells[helico.x][helico.y]

        # Подбор воды
        if (c == 2):
            helico.tank = helico.maxtank