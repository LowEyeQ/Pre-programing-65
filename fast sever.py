"""Fast server"""
def main():
    """print Fast server"""
    speed_a = int(input())
    unit_a = input()
    speed_b = int(input())
    unit_b = input()
    if unit_a == "Millisecond":
        seconda = speed_a*(10**-3)
    elif unit_a == "Microsecond":
        seconda = speed_a*(10**-6)
    elif unit_a == "Nanosecond":
        seconda = speed_a*(10**-9)
    elif unit_a == "Picosecond":
        seconda = speed_a*(10**-12)
    if unit_b == "Millisecond":
        secondb = speed_b*(10**-3)
    elif unit_b == "Microsecond":
        secondb = speed_b*(10**-6)
    elif unit_b == "Nanosecond":
        secondb = speed_b*(10**-9)
    elif unit_b == "Picosecond":
        secondb = speed_b*(10**-12)
    if seconda == secondb:
        print("equal")
    elif seconda < secondb:
        print("Server A, %.6f second"%seconda)
        print("Faster than server B , %d times"%(secondb//seconda))
    elif secondb < seconda:
        print("Server B, %.6f second"%secondb)
        print("Faster than server A , %d times"%(seconda//secondb))
main()
