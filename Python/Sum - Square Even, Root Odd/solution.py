import math

def sum_square_even_root_odd(nums):
    count = 0
    
    for i in nums:
        if i % 2 == 0:
            count += i ** 2
        else:
            count += math.sqrt(i)
    return round(count, 2)
  
  
  
