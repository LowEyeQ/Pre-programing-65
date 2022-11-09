
# def func(x):
#     if not(x <= 20 !=x < 20):
#         print("True")
# func(222222222222222222)

# def func(x):
#     if x >= 0:
#         return True
#     else:
#         return False
# print(func(-1))

# def funcn(x):
#     if x < 0:
#         return False
#     return True
# print(funcn(-1))

# def main():
#     x = int(input())
#     if not x < 20:
#         print("True")
# main()

# def main(n):
# #     return lambda x: x-n
# # add1 = main(1)
# # add2 = main(2)
# # add3 = main(3)

# # print(add1(1))
# # print(add2(2))
# # print(add3(3))

# def main():
#     weight = [int(input()), int(input()), int(input()), \
# int(input()), int(input()), int(input()), int(input()), int(input())]
#     c = [i for i in weight if i % 2  == 0 ]
#     print(type(c[0 and 1 and 2 and 3 and 4 and 5 and 6 and 7 and 8]))
# # main()
# def main(pax,head,come,pay):
#     total = ((pax//come*pay)*head) + (pax%come*head)
#     return total
# print(main(int(input()),int(input()),int(input()),int(input())))
# """plan"""
# def main():
#     """main"""
#     text = input()
#     num1 = float(input())
#     num2 = float(input())
#     num3 = float(input())
#     if text == "Ascend":
#         aaa(num1, num2, num3)
#     elif text == "Descend":
#         bbb(num1, num2, num3)

# def aaa(num1, num2, num3):
#     """aaa"""
#     if num1 < num2 and num1 <num3 and num2 < num3:
#         print("%.2f, %.2f, %.2f" %(num1, num2, num3))
#     elif num1 < num2 and num3 < num2 and num1 <num3:
#         print("%.2f, %.2f, %.2f" %(num1, num3, num2))
#     elif num2 < num1 and num2 < num3 and num1 <num3:
#         print("%.2f, %.2f, %.2f" %(num2, num1, num3))
#     elif num2 < num1 and num2 < num3 and num3 <num1:
#         print("%.2f, %.2f, %.2f" %(num2, num3, num1))
#     elif num3 < num2 and num3 < num1 and num1 <num2:
#         print("%.2f, %.2f, %.2f" %(num3, num1, num2))
#     elif num3 < num1 and num3 < num2 and num2 <num1:
#         print("%.2f, %.2f, %.2f" %(num3, num2, num1))

# def bbb(num1, num2, num3):
#     """bbb"""
#     if num1 > num2 and num1 >num3 and num2 > num3:
#         print("%.2f, %.2f, %.2f" %(num1, num2, num3))
#     elif num1 > num2 and num3 > num2 and num1 >num3:
#         print("%.2f, %.2f, %.2f" %(num1, num3, num2))
#     elif num2 > num1 and num2 > num3 and num1 >num3:
#         print("%.2f, %.2f, %.2f" %(num2, num1, num3))
#     elif num2 > num1 and num2 > num3 and num3 >num1:
#         print("%.2f, %.2f, %.2f" %(num2, num3, num1))
#     elif num3 > num2 and num3 > num1 and num1 >num2:
#         print("%.2f, %.2f, %.2f" %(num3, num1, num2))
#     elif num3 > num1 and num3 > num2 and num2 >num1:
#         print("%.2f, %.2f, %.2f" %(num3, num2, num1))
#     elif num1 == num2 and num1 == num3 and num1 == num1:
#         print("%.2f, %.2f, %.2f" %(num1, num2, num3))

# main()


# """Sequence VIII"""
# def seqeight():
#     """Sequence VIII"""
#     nums = int(input())
#     for val in range(1, nums+1):
#         for space in range(nums-val):
#             print("  ", end=" ")
#         for space in range(1, val+1):
#             print("%02d"%space, end=" ")
#         print()
# seqeight()
# def func(a, b):
#     a = 3
#     c = a + b
#     return c
# a = 4
# x = func(2, a)
# print(a)
# print(1 and 0)
# for n in range(1,2):
#     print(n)
def f(a=0,b=1):
    return a+b
# """Sequence IX"""
# def seqnine():
#     """Sequence IX"""
#     nums = int(input())
#     for row in range(1, nums+1):
#         for _ in range(1, (nums+1)-row):
#             print("   ", end="")
#         for _ in range(1, row+1):
#             print("%02d"%_, end=" ")
#         for _ in range(2, row+1):
#             print("%02d"%(row-_ +1), end=" ")
#         print()
# seqnine()
print("")