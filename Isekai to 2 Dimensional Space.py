"""Isekai to 2 Dimensional Space"""
import math as m
def main():
    """print Isekai to 2 Dimensional Space"""
    posx = float(input())
    posy = float(input())
    displacement = float(input())
    degree = float(input())
    degreex = abs(m.radians(degree))
    degreey = abs(m.radians(degree))
    disx = m.cos(degreex)*displacement
    disy = m.sin(degreey)*displacement
    ansx = posx + disx
    ansy = posy + disy
    print("%.2f"%ansx)
    print("%.2f"%ansy)
main()
