
list = [10, 501, 22, 37, 100, 999, 87, 357]
even_numbers = []
odd_numbers = []
for num in list:
    if num % 2 == 0:
        even_numbers.append(num)
    else:
        odd_numbers.append(num)
print("Even Numbers:", even_numbers)
print("Odd Numbers:", odd_numbers)