"""Way to travel"""
def main():
    """print Way to travel"""
    weather = input()
    txt1 = input()
    distance = float(input())
    if weather == "rainy" and txt1 == "not important":
        print("Not go")
    else:
        if distance < 0:
            print("Error")
        elif distance < 1:
            print("Walk")
        elif distance < 20:
            print("Motorcycle")
        elif distance < 300:
            print("Car")
        elif distance >= 300:
            print("Private jet")
main()
