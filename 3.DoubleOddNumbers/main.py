def double_odd_numbers(amount_elements):
    if type(amount_elements) is not int:
        print('\n\tТип числа не int!')
        return 0

    return [
                element * 2
                for element in range(amount_elements)
                if element % 2 == 1
            ]

assert double_odd_numbers(5.5) == 0
assert double_odd_numbers(5) == [2, 6]
assert double_odd_numbers(6) == [2, 6, 10]