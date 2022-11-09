"""show me the money"""
def main():
    """print show me the money"""
    moneyclient = float(input())
    pricegoods = float(input())
    if moneyclient > pricegoods:
        total = moneyclient-pricegoods
        bank100 = total//100
        total %= 100
        bank50 = total//50
        total %= 50
        bank20 = total//20
        total %= 20
        coin12 = total//12
        total %= 12
        coin10 = total//10
        total %= 10
        coin5 = total//5
        total %= 5
        coin2 = total//2
        total %= 2
        coin1 = total//1
        total %= 1
        coin050 = total//0.5
        total %= 0.5
        coin025 = total//0.25
        total %= 0.25
        print("เเบงค์ 100 บาท : %d"%(bank100))
        print("เเบงค์ 50 บาท : %d"%(bank50))
        print("เเบงค์ 20 บาท : %d"%(bank20))
        print("เหรียญ 12 บาท : %d"%(coin12))
        print("เหรียญ 10 บาท : %d"%(coin10))
        print("เหรียญ 5 บาท : %d"%(coin5))
        print("เหรียญ 2 บาท : %d"%(coin2))
        print("เหรียญ 1 บาท : %d"%(coin1))
        print("เหรียญ 50 สตางค์ : %d"%(coin050))
        print("เหรียญ 25 สตางค์ : %d"%(coin025))
    elif moneyclient < pricegoods:
        print("จำนวนเงินไม่พอ")
    elif moneyclient == pricegoods:
        print("จ่ายมาพอดี")
main()
