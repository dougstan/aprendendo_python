"""class Point:
    def __init__(self, x=0, y=0): # init - vai ser criado automaticamente quando instanciar um objeto da classe; self - referencia o objeto que está sendo criado desta classe
        self.x = x
        self.y = y

    def setX(self, x):
        self.x = x

    def setY(self, y):
        self.y = y

    def get(self):
        return self.x, self.y

    def move(self, offsetx, offsety):
        self.x += offsetx
        self.y += offsety

    def __repr__(self):
        return '(' + str(self.x) + ',' + str(self.y) + ')'"""

def f1(n): 
    if n <= 1: 
        return 1 
    else: 
        return n * f1(n - 1) 