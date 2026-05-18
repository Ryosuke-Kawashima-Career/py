def negativity_check(func):
    def wrapper(num):
        if num < 0 or not isinstance(num, int):
            raise Exception("Number must be a non-negative integer")
        return func(num)
    return wrapper

@negativity_check
def factorial(num: int) -> int:
    if num == 0:
        return 1
    else:
        return num * factorial(num - 1)

def main():
    try:
        print(factorial(5))
        print(factorial(-5))
    except Exception as e:
        print(e)

if __name__ == '__main__':
    main()
