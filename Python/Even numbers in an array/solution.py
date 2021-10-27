def even_numbers(arr,n):
    evens = []
    
    for i in arr:
        if i % 2 == 0:
            evens.append(i)
    return evens[-n:]
  
  
