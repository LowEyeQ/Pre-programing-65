"""เต่าบิน"""
def main():
    """print เต่าบิน"""
    money = float(input())
    water = float(input())
    change = money-water
    maxcoin = change/0.25
    coin10 = change//10
    coin10_1 = change%10
    coin5 = coin10_1//5
    coin5_1 = coin10_1%5
    coin2 = coin5_1//2
    coin2_1 = coin5_1%2
    coin1 = coin2_1//1
    coin1_1 = coin2_1%1
    coin05 = coin1_1//0.5
    coin05_1 = coin1_1%0.5
    coin025 = coin05_1//0.25
    print(int(maxcoin))
    print(int(coin10+coin5+coin2+coin1+coin05+coin025))
    print(float(change))
main()
