"""เลือกคนคุยให้หน่อย"""
def main():
    """print เลือกคนคุยให้หน่อย"""
    character1 = input()
    character2 = input()
    if character1 == "Calm" and character2 == "Empathetic" or \
    character1 == "Empathetic" and character2 == "Calm":
        print("Ice")
    elif character1 == "Reliable" and character2 == "Courageous" or \
    character1 == "Courageous" and character2 == "Reliable":
        print("Fern")
    elif character1 == "Optimistic" and character2 == "Cheerful" or \
    character1 == "Cheerful" and character2 == "Optimistic":
        print("Bam")
    elif character1 == "Attractive" and character2 == "Creative" or \
    character1 == "Creative" and character2 == "Attractive":
        print("Tangmo")
    elif character1 == "Cheerful" and character2 == "Creative" or \
    character1 == "Creative" and character2 == "Cheerful":
        print("Mild")
    elif character1 == "Reliable" and character2 == "Optimistic" or \
    character1 == "Optimistic" and character2 == "Reliable":
        print("Prae")
    elif character1 == "Courageous" and character2 == "Calm" or \
    character1 == "Calm" and character2 == "Courageous":
        print("Dream")
    elif character1 == "Empathetic" and character2 == "Attractive" or \
    character1 == "Attractive" and character2 == "Empathetic":
        print("Aom")
main()
