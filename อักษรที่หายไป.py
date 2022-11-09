"""อักษรที่หายไป"""
def main():
    """print อักษรที่หายไป"""
    txt0 = input()
    if txt0.count("\"") == 0:
        print("No error")
    else:
        txt1 = txt0.index("\"")
        txt2 = txt0.rindex("\"")
        txt3 = chr(int(txt0[txt1+1:txt2]))
        print(txt0.replace(txt0[txt1:txt2+1], txt3))
main()
