def check_even(numbers):
    even_numbers = []
    for num in numbers:
        if num % 2 == 0:
            even_numbers.append(num)
        else:
            pass
    return even_numbers
print(check_even([1,2,4,5,7,6]))
print(check_even([2,4,6]))
print(check_even([1,5,7]))