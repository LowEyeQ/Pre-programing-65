"""I N T E G E R is useful."""
def main():
    """print 10"""
    num = int(input())
    ans = (str(bin(num))[2:].replace("0", "close, ")).replace("1", "open, ")
    print(ans[:-2])
main()
