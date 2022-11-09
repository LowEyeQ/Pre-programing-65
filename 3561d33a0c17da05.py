"""ร้านขายเสื้อของจอมเวทย์"""
def main():
    """print ร้านขายเสื้อของจอมเวทย์"""
    car = str(input())
    if car == 'Magician':
        guild = str(input())
        much = int(input())
        nor = (12800*much)
        if guild == 'Fairy Tail':
            pay1 = (12800*much)*(80/100)
            print("Total", int(pay1), "Jewel")
        elif guild == 'Sabertooth':
            if much > 5:
                pay2 = (12800*much)*(85/100)
                print("Total", int(pay2), "Jewel")
            else:
                print("Total", int(nor), "Jewel")
        elif guild == 'Lamia Scale':
            if much >= 3:
                pay3 = (12800*much)*(90/100)
                print("Total", int(pay3), "Jewel")
            else:
                print("Total", int(nor), "Jewel")
        elif guild == 'Blue Pegasus':
            if much > 10:
                pay4 = (12800*much)*(95/100)
                print("Total", int(pay4), "Jewel")
        else:
            print("Total", int(nor), "Jewel")
    else:
        much = int(input())
        nor = (12800*much)
        print("Total", int(nor), "Jewel")
main()
