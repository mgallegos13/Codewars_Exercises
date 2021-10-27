def remove_duplicate_words(s):
    
    new_list = s.split()
    list = []
    
    for i in new_list:
        if (s.count(i)>=1 and (i not in list)):
            list.append(i)
            
    return ' '.join(list)
    
    
    
