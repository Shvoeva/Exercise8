max_age = 5000
max_transparency = 10000

def degree_of_transparency(n):
    transparency = max_transparency
    fibonacci_number1, fibonacci_number2 = 1, 1

    yield transparency, 0
    for age in range(1, n):
        if age == fibonacci_number2:
            transparency -= fibonacci_number2
            fibonacci_number1, fibonacci_number2 = \
                fibonacci_number2, fibonacci_number1 + fibonacci_number2
        else:
            transparency += 1
        yield transparency, age

def determine_the_age_of_the_ghost(transparency):
    if (type(transparency) is not int) \
            or (transparency < 0 or transparency > 10000):
        return 'Прозрачность введена неправильно!'

    generator_transparency = degree_of_transparency(max_age + 1)
    for i, age in generator_transparency:
        if transparency == i:
            return age
    return 'Призрак исчез'

assert determine_the_age_of_the_ghost(10000) == 0
assert determine_the_age_of_the_ghost(9999) == 1
assert determine_the_age_of_the_ghost(9997) == 2
assert determine_the_age_of_the_ghost(9994) == 3
assert determine_the_age_of_the_ghost(9995) == 4
assert determine_the_age_of_the_ghost(9990) == 5
assert determine_the_age_of_the_ghost(0) == 'Призрак исчез'
assert determine_the_age_of_the_ghost(0.5) == 'Прозрачность введена неправильно!'