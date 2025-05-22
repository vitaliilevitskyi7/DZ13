from typing import Union
from math import gcd

class RationalError(ZeroDivisionError):
    def __init__(self, message="Denominator cannot be zero"):
        super().__init__(message)

class RationalValueError(Exception):
    def __init__(self, message="Invalid value for Rational operation"):
        super().__init__(message)

def isIterable(obj):
    return hasattr(obj, '__iter__') and hasattr(obj, '__next__') or hasattr(obj, '__iter__') and hasattr(iter(obj), '__next__')

class MyClass:
    def __iter__(self):
        return self
    def __next__(self):
        return 42

def log_call(func):
    def wrapper(*args, **kwargs):
        print(f"Виклик функції {func.__name__}")
        return func(*args, **kwargs)
    return wrapper

@log_call
def example_function():
    print("Функція виконана")

def log_class(cls):
    class Wrapped(cls):
        def __init__(self, *args, **kwargs):
            print(f"Створено екземпляр класу {cls.__name__}")
            super().__init__(*args, **kwargs)
    return Wrapped

@log_class
class TestClass:
    def __init__(self):
        print("Виконується __init__ TestClass")

def main():
    import sys
    original_stdout = sys.stdout
    with open("output_demo.txt", "w", encoding="utf-8") as out:
        sys.stdout = out

        print("10.3.1: isIterable перевірка")
        print("List ->", isIterable([1, 2, 3]))
        print("Int  ->", isIterable(42))
        print("MyClass ->", isIterable(MyClass()))

        print("\n10.3.2: Тестуємо MyClass")
        it = MyClass()
        print(next(it))

        print("\n10.3.3: Тестуємо декоратор функції")
        example_function()

        print("\n10.3.4: Тестуємо декоратор класу")
        t = TestClass()

        sys.stdout = original_stdout

if __name__ == "__main__":
    main()
