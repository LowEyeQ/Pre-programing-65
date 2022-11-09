"""Choose a book"""
import math
def main():
    """print Choose a book"""
    numbook = int(input())
    numbook1 = int(input())
    book = (math.factorial(numbook))/((math.factorial(numbook1))*(math.factorial(numbook-numbook1)))
    print(int(book))
main()
