# Write your code here :-)
from random import*
class Vector():
    pass
def direction(v1,v2):
    mag_v1=(v1.x**2+v1.y**2+v1.z**2)**0.5
    mag_v2=(v2.x**2+v2.y**2+v2.z**2)**0.5
    d1=v1.x/mag_v1
    d2=v1.y/mag_v1
    d3=v1.z/mag_v1
    d4=v2.x/mag_v2
    d5=v2.y/mag_v2
    d6=v2.z/mag_v2
    if d1==d4 and d2==d5 and d3==d6:
        return True
def magnitude(v1,v2):
    mag_v1=(v1.x**2+v1.y**2+v1.z**2)**0.5
    mag_v2=(v2.x**2+v2.y**2+v2.z**2)**0.5
    if mag_v1==mag_v2:
        return True
def main():
    t=Vector()
    m=Vector()
    t.x=randint(1,9)
    t.y=randint(1,9)
    t.z=randint(1,9)
    m.x=randint(1,9)
    m.y=randint(1,9)
    m.z=randint(1,9)
    if magnitude(t,m)==True and direction(t,m)==True:
        print('equal')
    else:
        print('unequal')
main()




