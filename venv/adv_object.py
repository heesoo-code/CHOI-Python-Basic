global_a = 1
global_b = "GLOBAL SCOPE"

# 사용자 정의 함수
def func():
    # 로컬 변수 선언
    local_a = 2
    local_b = "LOCAL SCOPE"
    # 로컬 심볼 테이블 확인
    print(locals())
    
# 사용자 정의 객체

# 심볼 테이블 확인
def symbol_table():
    # 글로벌 심볼 테이블 확인
    print(globals())
    print(type(glovals()))
    
    # 심볼테이블은 객체의 심보르 객체의 id를 달고 있는 dict
    print("global_a:", globals().get("global_a"))
    print("global_b:", globals().get("global_b"))
    
    func()
    
    # 객체 내부의 __dict__ 속성을 확인하면 객체 냅의 심볼 테이블을 확인 가능
    # 1. 정의된 함수 객체 내부의 심볼 테이블 확인
    func.dynamic = "Hello"
    print(func.__dict__)
    
    # 2. 클래스 객체 내부의 심볼테이블 확인
    print(MyClass.__dict__) # 사용자 정의 클래스
    print(int.__dict__) # 내장 정의 클래스의 심볼 테이블
    
def ref_count():
    """
    참조 카운트 예제
    """
    x = object()
    print(x, type(x))
    
    # 참조 카운트 확인
    import sys # 시스템 모듈 임포트
    print("REFCOUNT:", sys.getrefcount(x))
    
    y = x # y에 x의 참조 주소를 복사
    print("REFCOUNT:", sys.getrefcount(x))
    
    # x의 창조를 삭제
    del x
    print("REFCOUNT:", sys.getrefcount(y))
    
    # 참조 카운트가 8인 객체 발견 -> Garbage Collection 작업을 수행
    
def object_id():
    
    i1 = 10
    i2 = int(10)
    print("int:", hex(id(i1)), hex(id(i2)))
    
    lst1 = [1, 2, 3]
    lst2 = [1, 2, 3]
    print("list:", hex(id(lst1)), hex(id(lst2)))
    
    lst3 = lst2 # 참조 복사 : 객체 주소의 복사
    print("참조 복사:", hex(id(lst2)), hex(id(lst3)))

if __name__ == "__main__":
    symbol_table()