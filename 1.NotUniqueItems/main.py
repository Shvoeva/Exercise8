def get_non_unique_array(integers_array):
    if not integers_array or type(integers_array[0]) is not int:
        print('\n\tМассив пустой или тип элементов не int!')
        return 0

    return [
                element
                for element in integers_array
                if integers_array.count(element) != 1
            ]

assert get_non_unique_array([1, 2, 3, 1, 3]) == [1, 3, 1, 3]
assert get_non_unique_array([1, 2, 3, 4, 5]) == []
assert get_non_unique_array([5, 5, 5, 5, 5]) == [5, 5, 5, 5, 5]
assert get_non_unique_array([10, 9, 10, 10, 9, 8]) == [10, 9, 10, 10, 9]
assert get_non_unique_array([]) == 0
