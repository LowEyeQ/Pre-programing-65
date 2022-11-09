"""	Toy Factory"""
def main():
    """print Toy Factory"""
    realnum = int(input())
    txt = input().lower()
    funf = (15+realnum-(realnum**3))/(((realnum**2)/3)+11)
    fung = (realnum**3)+(4*realnum-1)
    if txt == "fog":
        ans = (15+fung-(fung**3))/(((fung**2)/3)+11)
        print("%.2f"%ans)
    else:
        ans = (funf**3)+(4*funf-1)
        print("%.2f"%ans)
main()
