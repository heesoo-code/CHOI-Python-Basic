# 함수 인수는 필요한 개수만큼 선언
def sum_val(a, b):
    return a + b

def incr(a, step=1):
    return a + step

print(sum_val(2, 3)) # 고정 변수르를 전달할 때는 순서대로
print(incr(10)) # 기본값이 있는 인수는 전달하지 않으면 기본값이 선택
print(incr(10, 2)) # 두 번째 인수의 기본값 무시, 전달한 값을 할당

# 키워드 인수
# 아슈의 값을 인수의 이름으로 전달 -> 연주의 순서는 바뀌어도 무관
def area(width, height):
    print("width:", width)
    print("height:", height)
    return width * height

print (area(10, 12)) # 인수 이름 명시 안함 -> 선언 순서대로 전달
print(area(height=12, width=10)) # 인수 이름 명시 -> 인수의 순서와는 관계 없음

# 가변인수
# 정해지지 않은 개수의 인수를 받을 때
# 인수명 앞에 *를 붙여 선언
def get_total(*args): # 여러 개의 인수를 전달 -> 합산 후 반응
    total = 0
    print("인수:", args, type(args))
    for x in args:
        total += x
        return total
    print(get_total(1, 3 ,5 ,7, 9))

def get_total2(*args):
    total = 0
    # TO DO music
    return total

print(get_total2(1, 2, 3, 4, 5))
print(get_total2(1, 2, "3", 4, 5))
print(get_total2(1, 2, [3, 4, 5]))

# 사전 키워드
# 지정되지 않은 키워드들 -> dict로 변환되서 사전 키워드로 전달
# 사전 키워드 인수 앞ㅇ데 **을 붙인다.
def args_test(a, b, *args, **kwd):
    # a, b -> 고정 인수
    # args -> 가변 인수
    # key -> 사전 키워드 인수
    print("고정인수:", a, b)
    print("가번인수:", args)
    print("사전 키워드 인수:", kwd)

args_test(10, 20, 30, 40, 50, optional="value1", option2="value2")

def plus(a, b):
    return a + b

def minus(a, b):
    return a - b

def calculator(a, b, func): # a, b -> 숫자, func -> 함수 전달
    if (callable(func)): # 넘어온 인수 func가 실행 가능 객체인가?
        return func(a, b)

print(calculator(1, 2, plus)) # 합산 함수를 외부에서 전달

dirty_strings = "python programming, java programming, LINUX, Windows".split()

def clean_string(string, funcs):
    results = []
    for string in strings:
        for func in funcs:
            if callable(func):
                string = func(string)
        results.append(string)
    return results

cleaned = clean_string(dirty_strings, str.stip, str.title)
print("Cleaned", cleaned)