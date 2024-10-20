numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

# TODO заменить значение пропущенного элемента средним арифметическим

mising_item = numbers.index(None)
sum_numbers = sum(numbers[:mising_item]) + sum(numbers[mising_item+1:])
average_numbers = sum_numbers / len(numbers)
numbers[mising_item] = average_numbers

print("Измененный список:", numbers)
