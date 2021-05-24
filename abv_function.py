def dummy():
    pass

def my_function():
    print("Hello python")

def times(a, b):
    return a * b

def non():
    return

def scope_func3(a):
    g = 3
    return a + g

print(scope_func3())
print("global.g:", g)
