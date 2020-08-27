def binary_search(input_array, value):
    """Your code goes here."""
    length = len(input_array)
    minimum = input_array[0]
    maximum = input_array[length - 1]
    if maximum < value <= minimum:
        return -1
    guess = input_array[int((length - 1)/2)]
    while guess != value:
        if guess > value:
            minimum = guess
            guess = input_array[]
        if guess < value:
            maximum = guess
            guess = input_array[]

test_list = [1,3,9,11,15,19,29]
test_val1 = 25
test_val2 = 15
print binary_search(test_list, test_val1)
print binary_search(test_list, test_val2)

#Big brain generic template
def binary_search(array) -> int:
    def condition(value) -> bool:
        pass

    left, right = min(search_space), max(search_space) # could be [0, n], [1, n] etc. Depends on problem
    while left < right:
        mid = left + (right - left) // 2
        if condition(mid):
            right = mid
        else:
            left = mid + 1
    return left
