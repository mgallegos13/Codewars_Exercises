def find_short(s):
    array = s.split()
    lst = []
    
    for i in array:
        lst.append(len(i))
    return min(lst)
