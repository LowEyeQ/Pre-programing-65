"""4 Addict"""
def main():
    """print 4 Addict"""
    num1 = float(input())
    txt1 = input()
    ans = ((((num1+4)**0.25+(num1/4))/(4*num1-4))*44)
    txt2 = int(num1//44)
    print(txt1*txt2)
    print("%.4f"%ans)
main()
