def high_and_low(numbers):
    array = numbers.split(' ')
    new_array = list(map(int, array))
    new_array.sort()
    
    return str(new_array[-1]) + " " + str(new_array[0])
