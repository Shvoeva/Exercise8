def get_list_permutations(number1, number2, number3, sum_numbers):
    if type(number1) is not int or type(number2) is not int \
            or type(number3) is not int or type(sum_numbers) is not int:
        print('\n\tТип значений не int!')
        return 0

    numbers = [number1, number2, number3]
    combinations_set = {
                            f'{i} {j} {k}'
                            for i in numbers
                            for j in numbers
                            for k in numbers
                            if i + j + k != sum_numbers
                        }
    combinations_list = [
                            list(map(int, i.split()))
                            for i in combinations_set
                        ]
    combinations_list.sort()
    return combinations_list

assert get_list_permutations(0, 0, 1, 2) == \
       [[0, 0, 0], [0, 0, 1], [0, 1, 0], [1, 0, 0], [1, 1, 1]]
