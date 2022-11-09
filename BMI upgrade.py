"""BMI upgrade"""
def main():
    """print BMI upgrade"""
    weight = float(input())
    high = float(input())/100
    age = int(input())
    total = weight/(high**2)
    if age < 18:
        print("Please use BMI for Children and Teens.")
    elif total < 16:
        print("Severe Thinness")
    elif total == 16 or total <= 16.99:
        print("Moderate Thinness")
    elif total == 17 or total <= 18.49:
        print("Mild Thinness")
    elif total == 18.5 or total <= 24.99:
        print("Normal")
    elif total == 25 or total <= 29.99:
        print("Overweight")
    elif total == 30 or total <= 34.99:
        print("Obese Class I")
    elif total == 35 or total <= 39.99:
        print("Obese Class II")
    elif total > 40:
        print("Obese Class III")
main()
