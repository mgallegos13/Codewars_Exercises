def get_sum_of_digits(num):
    
    int_to_str = str(num)
    a_list = list(int_to_str)
    map_object = map(int, a_list)
    list_of_integers = list(map_object)
    
    count = 0
    
    for i in list_of_integers:
        count += i 
        
    return count
