""""สมการตัวน้อย"""
def main():
    """print สมการตัวน้อย"""
    num1a = int(input())
    num2b = int(input())
    num3c = int(input())
    num4d = int(input())
    num5x = int(input())
    eq1 = num2b/(num1a**2/num4d)
    eq2 = num5x*num2b/num1a
    eq3 = (eq1+eq2)/num3c
    print("%.2f"%eq3)
main()
