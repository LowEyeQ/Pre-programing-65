"""นี่คือสูตรความเร็ว พี่ปวดเอวเจ็บหัวใจ"""
def main():
    """print อัตราเร็ว"""
    nauticalmile = float(input())
    millisecond = int(input())
    distance = 1852*nauticalmile
    time = 0.001*millisecond
    speed = distance/time
    print("อัตราเร็วเท่ากับ : %.3f เมตรต่อวินาที" %(speed))
main()
