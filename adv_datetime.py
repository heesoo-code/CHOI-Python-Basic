import datetime

def get_datetime():
    now = datetime.dattime.now()
    print(now)

    # 생성자 이용, 직접 날짜를 지정
    dt =datetime.datetime(1999, 12, 31) # 최소 년 월일은 지정
    print(dt)

    print("date관련 속성:", dt.year, dt.month, dt.day)
    print("time관련 속성:", dt.hour, dt.minute, dt.second, dt.microsecond)

    print("오늘은 무슨요일?", now.weekday())


    print(now.date(), type(now.date()))
    print(now.time(), type(now.time()))

    print("date:", nowdate.year, nowdate.month, nowdate.day, nowdate.weekday())
    print("time:", nowtime.hour, nowtime.minute, nowtime.second, nowtime.microsecond)

def timedelta_ex():
    current = datetime.datetime.now()
    print("Current:", current)
    past = datetime.datetime(1999, 12, 31)
    print("PAST:", past)
    print("CURRENT가 PAST 이후?", current > past)

    diff = current - past
    print(diff, type(diff))

    print("timedelta:", diff.days, diff.seconds, diff.microseconds)
    print("total seconds:", diff.total_seconds())

    print("current:", current)
    diff = datetime.timedelta(100, 0, 0)
    print("100일 후:", current + diff)

if __name__ == "__main__"
    timedelta_ex()

def format_date():
    current = datetime.datetime.now()
    print("current:", current)

    print(current.strftime("%Y-%m-%d %H:%M"))
    print(current.strftime("%Y년 %m월 %d일 %H시:%M분"))

    s = "2021-05-24 17:00:00"
    dt = datetime.datetime.strifttime(s, "%Y-%m-%d %H:%M:%S")
    print(dt, type(dt))

    commit