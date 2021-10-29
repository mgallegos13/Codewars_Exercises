def solution(number):
    if number < 0:
        return 0
    
    count = 0
    lst = range(number)
    
    for i in lst:
        if i % 3 == 0 or i % 5 == 0:
            count += i
    return count
  
  
  
