"""วันจันทร์ฉันคิดถึงเธออยู่ วันอังคารไปหาได้ไหม"""
def main():
    """print time"""
    time = int(input())
    sec = time%60
    minutes = time//60
    minutes1 = minutes%60
    hours = minutes//60
    hours1 = hours%24
    days1 = hours//24
    print("%02d:%02d:%02d:%02d"%(days1, hours1, minutes1, sec))
main()
