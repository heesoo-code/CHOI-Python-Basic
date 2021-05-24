def for_ex():
    """
    for 반복문
    """
    # Syntax : for 변수 in 순차형
    a = ["cat", "com", "tiger"]
    for animal in a:
        print(animal, end=" ")
    else
        print()

    #반복시 요소와 함꼐 인덱스도 함꼐 필요할 떄 -> enumerate 함수 -> (인덱스, 요소) 튜플
    for item in enumerate(['red', 'blue', 'green', 'black', "white"]):
        print(index, color)

    # range 객체 (범위객체)
    # 1 ~ 10까지 값 구하기
    total = 0
    for i in range(1, 11):
        total += 1

    print("total", total)

    # break : 남은 루프를 진행하지 않고 루프를 탈출
    r1 = list(range(1, 12, 2)) + [12, 13, 15]
    print("r1:", r1)
    # 첫번째 짝수를 출력 -> 종료
    for i % 2 == 0:
        print("첫번쨰 짝수를 찾았습니다:", 1)
        break
    else:
        print("짝수는 없습니다.")

        # 연습문제 1, 2단 ~ 9단까지 구구표 출력
        # 연습문제 2. 삼각형 그리기
        """
        *
        **
        ***
        ****
        *****
        """

    def while_ex():
        """
        while 문 연습
        """