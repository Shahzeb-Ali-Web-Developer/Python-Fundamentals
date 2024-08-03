class Mat2by2:
    def __init__(self, a11=0, a12=0, a21=0, a22=0):
        self.setW(a11)
        self.setX(a12)
        self.setY(a21)
        self.setZ(a22)

    def setW(self, d):
        self.__a11 = d

    def getW(self):
        return self.__a11

    def setX(self, d):
        self.__a12 = d

    def getX(self):
        return self.__a12

    def setY(self, d):
        self.__a21 = d

    def getY(self):
        return self.__a21

    def setZ(self, d):
        self.__a22 = d

    def getZ(self):
        return self.__a22

    def __add__(self, rhs):
        m = Mat2by2()
        m.setW(self.getW() + rhs.getW())
        m.setX(self.getX() + rhs.getX())
        m.setY(self.getY() + rhs.getY())
        m.setZ(self.getZ() + rhs.getZ())
        return m

    def __sub__(self, rhs):
        m = Mat2by2()
        m.setW(self.getW() - rhs.getW())
        m.setX(self.getX() - rhs.getX())
        m.setY(self.getY() - rhs.getY())
        m.setZ(self.getZ() - rhs.getZ())
        return m

    def multiplication(self, rhs):
        m = Mat2by2()
        m.setW(self.getW() * rhs.getW() + self.getX() * rhs.getY())
        m.setX(self.getW() * rhs.getX() + self.getX() * rhs.getZ())
        m.setY(self.getY() * rhs.getW() + self.getZ() * rhs.getY())
        m.setZ(self.getY() * rhs.getX() + self.getZ() * rhs.getZ())
        return m

    def scalar_multiple(self, element):
        m = Mat2by2()
        m.setW(element * self.getW())
        m.setX(element * self.getX())
        m.setY(element * self.getY())
        m.setZ(element * self.getZ())
        return m

    def determinant(self):
        deter = self.getW() * self.getZ() - self.getX() * self.getY()
        return deter

    def singular(self):
        deter = self.getW() * self.getZ() - self.getX() * self.getY()
        if deter == 0:
            return 'It is a Singular Matrix'
        else:
            return 'It is not a Singular Matrix'

    def __str__(self):
        return "(" + str(self.getW()) + "," + str(self.getX()) + "," + str(self.getY()) + "," + str(self.getZ()) + ")"


def main():
    t = Mat2by2(2, 3, 4, 5)
    s = Mat2by2(2, 2, 2, 2)
    element = 2
    print(f"t: {t}")
    print(f"s: {s}")
    a = t + s
    print(f"t + s: {a}")
    s = t - s
    print(f"t - s: {s}")
    m = t.multiplication(s)
    print(f"t * s: {m}")
    scalar = t.scalar_multiple(element)
    print(f"Scalar Multiple: {scalar}")
    dm = s.determinant()
    print(f'Determinant = {dm}')
    sing= s.singular()
    print(f'Singular Matrix: {sing}')


main()
