"""เรียงข้อความ ยามเธออ่านไม่ตอบ"""
def main():
    """print เรียงข้อความ ยามเธออ่านไม่ตอบ"""
    txt1, txt2, txt3 = input().capitalize(), input().capitalize(), input().capitalize()
    if len(txt1) < len(txt2) < len(txt3):
        print(txt1)
        print(txt2)
        print(txt3)
    elif len(txt3) < len(txt2) < len(txt1):
        print(txt3)
        print(txt2)
        print(txt1)
    elif len(txt2) < len(txt1) < len(txt3):
        print(txt2)
        print(txt1)
        print(txt3)
    elif len(txt3) < len(txt2) < len(txt1):
        print(txt3)
        print(txt2)
        print(txt1)
    elif len(txt1) < len(txt3) < len(txt2):
        print(txt1)
        print(txt3)
        print(txt2)
    elif len(txt2) < len(txt3) < len(txt1):
        print(txt2)
        print(txt3)
        print(txt1)
main()
