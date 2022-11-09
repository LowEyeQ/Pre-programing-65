"""เค้กช็อกโกแลต"""
def main():
    """print เค้กช็อกโกแลต"""
    money = int(input())
    pricecake = int(input())
    moneyleft = money%pricecake
    cakeleft = money//pricecake
    if money >= pricecake:
        print("Chocolate Cake: %d"%cakeleft)
        print("Money left: %d"%moneyleft)
    else:
        print("Not enough money;(")
        print("Money left: %d"%moneyleft)
main()
