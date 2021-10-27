def solve(s):
    upper, lower, number, special = 0, 0, 0, 0
    for i in range(len(s)): 
        if s[i].isupper(): 
            upper += 1
        elif s[i].islower(): 
            lower += 1
        elif s[i].isdigit(): 
            number += 1
        else: 
            special += 1
    
    return [upper, lower, number, special]
