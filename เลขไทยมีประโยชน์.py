"""	เลขไทยมีประโยชน์"""
def main():
    """print เลขไทยมีประโยชน์"""
    thai = input()
    if thai == "N":
        nation = input()
    age = int(input())
    havecoupon = input()
    if age < 10 or age <= 20:
        price = 20
    elif age <= 10 or age <= 60:
        price = 0
    elif age > 20:
        price = 40
    if thai == "N":
        price *= 5
        if nation == "Vietnam" or nation == "Singapore" or nation == "India" :
            price /= 2
    if havecoupon == "Y":
        couponsale = int(input())
        price = (price*couponsale)/100
    print("%.2f"%price)
main()
