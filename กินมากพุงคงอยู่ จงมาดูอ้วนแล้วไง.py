"""กินมากพุงคงอยู่ จงมาดูอ้วนแล้วไง"""
def main():
    """print bmi"""
    name = input()
    weight = int(input())
    high = int(input())/100
    total = weight/(high**2)
    print("Name: %s \nWeight: %d kg.\nHeight: %.2f m.\nBMI: %.2f"%(name, weight, high, total))
main()
