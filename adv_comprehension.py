def list_comprehension():
    """
    리스트 내포
    Syntax: [ 표현식 for 변수 in 수차형 if 조건식 ]
    """
    # 1 ~ 10까지의 리스트가 있을 때, 내부 항목을 제곱한 새로운 리스트 생성
    nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    results = []

    for num in nums:
        result = num * num
        results.append(result)
    print("결과:", results)

    results = [ num * num for num in nums]
    print("내포 결과:", results)

    strings = ['a', 'as', 'bat', 'car', 'dove', 'python']
    #strings의 요소 중에서 문자열의 길이가 3이하인 문자열 리스트 생성

    results = []
    for item in strings:
        if len(item) <= 3:
            results.append(item)
    print("FOR 결과:", results)

    # List 내포
    results = [ item for item in strings if len(item) <= 3]
    print("내포 결과:", results)

if __name__ == "__main__":
    list
