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
