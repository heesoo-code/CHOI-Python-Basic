def handling_exception():
    lst = []


    try:
        lst[3] = 1
        4 / 0
        int("String")
    except Exception:
        print("Error")

    try:
        lst[3] = 1
        4 / 0
        int("String")

    except ValueError as e:
        print("정수로 변환 불가!")
        print(e, type(e))
    except ZeroDivisonError as e:
        print("0으로는 나눌 수 없습니다")
        print(e, type(e))
    except IndexError as e:
        print("인덱스에 접근 불가!")
        print(e, type(e))
    except Exceptikon as e:
        print("Error")
        print(e, type(e))
    else:
        print("예외 없음!")
    finally:
        print("예외처리 종료!")


def raise_exception():
    def beware_dog(animal):
        if animal == "dog":
            raise RuntimeError("강아지는 출입을 제한합니다!")
    else:
        print(animal, "어서오세요!")
    try:
    beware_dog("cat")
    beware_dog("cow")
    beware_dog("dog")
    except Exception as e:
        print(e, type(e))

    print("end of code")

if __name__ == "__main__":
    handling_exception()