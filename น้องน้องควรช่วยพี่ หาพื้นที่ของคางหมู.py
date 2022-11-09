"""พื้นที่ของคางหมู"""
def main():
    """print พื้นที่สี่เหลี่ยมคางหมู"""
    height, doublesidesizeone, doublesidesizetwo = float(input()), float(input()), float(input())
    print("Trapezoidal area = %.2f "%(1/2*height*(doublesidesizeone+doublesidesizetwo)))
main()
