"""Fibonacci ดูEasyเหมือนปลอกBanana"""
def main(number):
    """print Fibonacci ดูEasyเหมือนปลอกBanana"""
    if number <= 1:
        return number
    else:
        return main(number-1) + main(number-2)
print(main(int(input())))
