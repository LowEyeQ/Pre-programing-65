"""Oh! my matrix"""
def main():
    """print matrix"""
    mat1 = int(input())
    mat2 = int(input())
    mat3 = int(input())
    mat4 = int(input())
    matr1 = int(input())
    matr2 = int(input())
    matr3 = int(input())
    matr4 = int(input())
    matb1 = matr1-mat1
    matb2 = matr2-mat2
    matb3 = matr3-mat3
    matb4 = matr4-mat4
    print("b1: "+str(matb1))
    print("b2: "+str(matb2))
    print("b3: "+str(matb3))
    print("b4: "+str(matb4))
    print("D: %.2f"%((mat1*mat4-mat3*mat2)+(matb1*matb4-matb3*matb2)+(matr1*matr4-matr3*matr2)))
main()
