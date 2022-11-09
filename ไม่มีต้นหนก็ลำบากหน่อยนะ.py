"""ไม่มีต้นหนก็ลำบากหน่อยนะ"""
def main():
    """print ไม่มีต้นหนก็ลำบากหน่อยนะ"""
    fish = input()
    seaman = int(input())
    numfish = fish.count("<^))))><")
    if numfish > seaman:
        print("We have many fish ahoyy!!!")
    elif numfish == seaman:
        print("We have enough fish for everyone.")
    elif numfish*2 == seaman:
        print("We can share the fish together Yahoooo!!!")
    else:
     print("No one will eat them  because we cannot be divided the fish.")
main()
