"""ลองสลับการ์ด แล้วตัดขาดจากใจเธอ"""
def main():
    """print ลองสลับการ์ด แล้วตัดขาดจากใจเธอ"""
    row = int(input())
    if row == 12 or row == 21:
        print("A")
    elif row == 23 or row == 32:
        print("C")
    else:
        print("B")
main()
