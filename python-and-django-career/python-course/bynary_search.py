
def binary_search(numbers, number_to_find, low, high):

    if low > high:
        return False
    
    mid = int((low + high) / 2)

    if numbers[mid] == number_to_find:
        return True
    elif numbers[mid] > number_to_find:
        return binary_search(numbers, number_to_find, low, mid - 1)
    else:
        return binary_search(numbers, number_to_find, mid + 1, high)


if __name__ == "__main__":
    numbers = [88, 99, 100, 1, 3, 4, 5, 6, 9, 10, 11, 25, 27, 28, 34, 36, 49, 51]
    numbers.sort()
    print(numbers)

    number_to_find = int(input('Enter number to find: '))

    result = binary_search(numbers, number_to_find, 0, len(numbers) - 1)

    if result is True:
        print('The number is in the list')
    else:
        print('The number NOT is in the list')

