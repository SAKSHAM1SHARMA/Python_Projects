def calculateRunningTotal(n, list_of_numbers):
    product = 1
    total_sum = 0
    has_zero = False
    has_three = False

    for num in list_of_numbers:
        product *= num
        total_sum += num
        if num == 0:
            has_zero = True
        if num == 3:
            has_three = True

    if product % 2 == 0:  # Even product
        if has_zero:
            return total_sum * 2
        else:
            return total_sum
    else:  # Odd product
        if has_three:
            return product + 1
        else:
            return product

# Example usage:
n = 4
list_of_numbers = [1, 2, 3, 4]
result = calculateRunningTotal(n, list_of_numbers)
print("Output:", result)  # Output should be 10
