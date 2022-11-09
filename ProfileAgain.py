"""ProfileAgain"""
def main():
    """print ProfileAgain"""
    sex = input().lower().replace("female", "Mrs.").replace("male", "Mr.")
    idcode = input()
    name = input()
    surname = input()
    age = int(input())
    job = input()
    print("======")
    print("ID : "+idcode[0:6])
    print("Name :", sex, name.capitalize(), surname.capitalize())
    print("Age :", str(age), "years", "old")
    print("Occupation :", job.upper())
    print("======")
main()
