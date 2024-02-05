def classifyTriangle(a, b, c):
    if a > 200 or b > 200 or c > 200:
        return 'InvalidInput'
        
    if a <= 0 or b <= 0 or c <= 0:
        return 'InvalidInput'
    
    if not(isinstance(a, int) and isinstance(b, int) and isinstance(c, int)):
        return 'InvalidInput'
      
    if (a + b <= c) or (a + c <= b) or (b + c <= a):
        return 'NotATriangle'
        
    if a == b == c:
        return 'Equilateral'
    elif a**2 + b**2 == c**2:
        return 'Right'
    elif a == b or b == c or a == c:
        return 'Isosceles'
    else:
        return 'Scalene'
