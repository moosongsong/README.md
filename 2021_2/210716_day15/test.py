def my_range(first=0, last=10, step=1):
    number = first
    while number < last:
        yield number
        number += step


print(my_range)
print(my_range(1, 5))

genobj = (pair for pair in zip(['a', 'b'], ['1', '2']))
print(genobj)
for thing in genobj:
    print(thing)


def document_it(func):
    def new_function(*args, **kwargs):
        print(f'Running function:{func.__name__}')
        print(f'Positional arguments: {args}')
        print(f'Keyword arguments: {kwargs}')

        result = func(*args, **kwargs)

        print(f'Result: {result}')
        return result

    return new_function


def add_ints(a, b):
    return a + b


add_ints(3, 5)
cooler_add_ints = document_it(add_ints)
# 데코레이터 수동 할당

print(cooler_add_ints(3, 5))


######################################################
def document_it(func):
    def new_function(*args, **kwargs):
        print(f'Running function: {func.__name__}')
        print(f'Positional arguments: {args}')
        print(f'Keyword arguments: {kwargs}')

        result = func(*args, **kwargs)

        print(f'Result: {result}')
        return result

    return new_function


@document_it
def add_ints(a, b):
    return a + b


print(add_ints(3, 5))


###############################
def factorial(n):
    if n == 1:  # n이 1일 때
        return 1  # 1을 반환하고 재귀호출을 끝냄
    return n * factorial(n - 1)  # n과 factorial 함수에 n - 1을 넣어서 반환된 값을 곱함


print(factorial(5))


def hello():
    print('Hello, world!')
    # hello()


hello()

###################################################

short_list = [1, 2, 3]
while True:
    value = input("Position [q to quit]?")
    if value == 'q':
        break
    try:
        position = int(value)
        print(short_list[position])
    except IndexError as err:
        print(f"Bad index: {position}")
    except Exception as other:
        print(f"Something else broke: {other}")


class UppercaseException(Exception):
    pass


words = ['eenie', 'meenie', 'miny', 'Mo']
for word in words:
    if word.isupper():
        raise UppercaseException(word)


class OopsException(Exception):
    pass


try:
    raise OopsException('panic')
except OopsException as exc:
    print(exc)


#######################################################

class Quite():
    def __init__(self, person, words):
        self.person = person
        self.words = words

    def who(self):
        return self.person

    def says(self):
        return self.words

