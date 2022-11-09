"""secrect code"""
def main():
    """print secret"""
    secret = int(input())
    xtr = str(secret//10**8%10)
    ytr = str(secret//10**6%10)
    ztr = str(secret//10**4%10)
    ttr = str(secret//10**2%10)
    utr = str(secret//10**0%10)
    print(xtr+ytr+ztr+ttr+utr)
main()
