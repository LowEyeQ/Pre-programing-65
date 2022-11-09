"""รวมเงิน"""
def main():
    """print รวมเงิน"""
    name1 = input()
    name2 = input()
    money1 = float(input())
    money2 = float(input())
    total = money1+money2
    branch = input()
    separator = input()
    print(name1, name2+separator+str(total)+separator+branch)
main()
