class Vector2D:
    def __init__(self,x,y):
        self._x = x
        self._y = y

    def __add__(self,other):
         return Vector2D(self._x + other._x, self._y + other._y)

    def __sub__(self,other):
         return Vector2D(self._x - other._x, self._y - other._y)

    def __mul__(self,scalar):
         return Vector2D(self._x * scalar, self._y * scalar)

    def magnitude(self):
        return (self._x ** 2 + self._y ** 2) ** 0.5

    def normalize(self):
        mag = self.magnitude()
        if mag == 0:
            return Vector2D(0,0)
        return Vector2D(self._x / mag, self._y / mag)

    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y
