"""ค่าไฟแพงเกินปุยมุ้ย!!"""
def main():
    """print ค่าไฟแพงเกินปุยมุ้ย!!"""
    num_a = int(input())
    num_b = int(input())
    num_c = int(input())
    num_d = int(input())
    num_e = int(input())
    unit_a = ((num_a*3)/1000)*30
    unit_b = ((num_b*1)/1000)*30
    unit_c = ((num_c*0.5)/1000)*30
    unit_d = ((num_d*5)/1000*4)*30
    unit_e = ((num_e*24)/1000)*30
    print("TV %d Watt 1 ea for 3 hours"%num_a)
    print("%.2f unit."%unit_a)
    print("Microwave %d Watt 1 ea for 1 hours"%num_b)
    print("%.2f unit."%unit_b)
    print("Hair dryer %d Watt 1 ea for 0.5 hours"%num_c)
    print("%.2f unit."%unit_c)
    print("light bulb %d Watt 4 ea for 5 hours"%num_d)
    print("%.2f unit."%unit_d)
    print("Refrigerator %d Watt 1 ea for 24 hours"%num_e)
    print("%.2f unit."%unit_e)
main()
