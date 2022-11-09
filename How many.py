"""How many"""
def main():
    """print How many"""
    txt1 = input().lower()
    txt2 = input().lower()
    num = txt1.count(txt2)
    numtxt = len(txt2)
    if num >= 1:
        if numtxt == 1:
            print("Character : %d" %num)
        else:
            print("Word : %d" %num)
    else:
        print("No word and character.")
main()
