def even_or_odd(s):
    
    #split and convert string to intergers
    a_list = list(s)
    map_object = map(int, a_list)
    list_of_integers = list(map_object)
    
    #even and odd variables
    evens = 0
    odds = 0
    
    #traverse thru list and adde them to count
    for i in list_of_integers:
        if i % 2 == 0:
            evens += i
        else:
            odds += i
    
    #return phrase
    if evens > odds:
        return "Even is greater than Odd"
    elif odds > evens:
        return "Odd is greater than Even"
    elif evens == odds:
        return "Even and Odd are the same"
    
