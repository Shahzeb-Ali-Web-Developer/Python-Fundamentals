#task-1
class Vectors:
    def __init__(self,x,y,z):
        self.x=x
        self.y=y
        self.z=z
def add(t,b):
    add=(f'{t.x+b.x},{t.y+b.y},{t.z+b.z}')
    return add
def stp(t,b,m):
    s=t.x*(m.y*b.z-b.y*m.z) -t.y*(m.x*b.z-b.x*m.z)+t.z*(m.x*b.y-b.x*m.y)
    return s
m=Vectors(3,-2,4)
t=Vectors(2,1,5)
b=Vectors(4,-1,-2)
print(f't:({t.x},{t.y},{t.z})')
print(f'b:({b.x},{b.y},{b.z})')
print(f'm:({m.x},{m.y},{m.z})')
print(f't+b: {add(t,b)}')
print(f'stp: {stp(t,b,m)}')



#task-2
import math
class Vectors:
    def __init__(self,x,y,z):
        self.x=x
        self.y=y
        self.z=z
    def magnitude(self):
        return math.sqrt(self.x**2+self.y**2+self.z**2)
t=Vectors(2,1,5)
print(f"Vector:({t.x}, {t.y}, {t.z})")
mag=Vectors.magnitude(t)
print(f'Unit Vector: ({t.x}/{mag:0.1f}, {t.y}/{mag:0.1f}, {t.z}/{mag:0.1f})')





#task-3
class Vectors:
    def __init__(self,x,y,z):
        self.x=x
        self.y=y
        self.z=z
    def scalar_multiple(self,n):
        self.x*=n
        self.y*=n
        self.z*=n
        return (f'{self.x},{self.y},{self.z}')
v=Vectors(2,1,5)
n=int(input("Enter number:"))
print(v.scalar_multiple(n))