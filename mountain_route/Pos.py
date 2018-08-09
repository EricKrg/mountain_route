
#  easier then indexing the whole thing
class Pos(object):
    def __init__(self, t, value):  # input is a tuple with y,x and an int value
        self.y = t[0]
        self.x = t[1]
        self.value = value # abs meters up/down

    def show(self):
        print(self.y, self.x, self.value)

    def straigth(self, terrain):
        return abs(terrain[self.y][self.x] - terrain[self.y][self.x + 1])

    def down(self, terrain):
        return abs(terrain[self.y][self.x] - terrain[self.y + 1][self.x + 1])

    def up(self, terrain):
        return abs(terrain[self.y][self.x] - terrain[self.y - 1][self.x + 1])
