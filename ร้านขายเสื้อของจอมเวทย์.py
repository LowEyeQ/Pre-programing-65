"""ร้านขายเสื้อของจอมเวทย์"""
def main():
    """print ร้านขายเสื้อของจอมเวทย์"""
    occupation = input()
    if occupation == "Magician":
        guild = input()
        amount = int(input())
        totalsuite = 12800*amount
        if guild == "Fairy Tail":
            total = (totalsuite*(100-20))/100
            print("Total %d Jewel" %total)
        elif guild == "Sabertooth" and amount > 5:
            total = (totalsuite*(100-15))/100
            print("Total %d Jewel" %total)
        elif guild == "Lamia Scale" and amount >= 3:
            total = (totalsuite*(100-10))/100
            print("Total %d Jewel" %total)
        elif guild == "Blue Pegasus" and amount > 10:
            total = (totalsuite*(100-5))/100
            print("Total %d Jewel" %total)
        else:
            print("Total %d Jewel" %totalsuite)
    else:
        num1 = int(input())
        totalsuite = 12800*num1
        print("Total %d Jewel" %totalsuite)
main()
