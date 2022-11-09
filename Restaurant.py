"""Restaurant"""
def main():
    """print Restaurant"""
    age = int(input())
    plate = int(input())
    if age >= 60 and plate == 1:
        print("Free")
    elif age > 60 and plate > 1:
        sale = plate*100*(50/100)
        print("Pay %d bath"%sale)
    elif age < 60:
        bill = plate*100
        print("Pay %d bath"%bill)
main()
