def solution(n,d):
    array = [int(a) for a in str(n)]
    
    if d <= 0:
        return []
        
    return array[-d:]
