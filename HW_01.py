def classify_triangle(s1, s2, s3):
    
    # Check if the triangle is valid
    if not (s1 + s2 > s3 and s2 + s3 > s1 and s1 + s3 > s2):
        return "Not a valid triangle"

    # Determine if it's equilateral
    if s1 == s2 == s3:
        return "Equilateral Triangle"

    # Determine if it's scalene or isosceles
    if s1 == s2 or s2 == s3 or s1 == s3:
        triangle_type = "Isosceles"
    else:
        triangle_type = "Scalene"

    # Determine if it's a right triangle
    if s1 ** 2 + s2 ** 2 == s3 ** 2 or s2 ** 2 + s3 ** 2 == s1 ** 2 or s1 ** 2 + s3 ** 2 == s2 ** 2:
        triangle_type += " Right Triangle"
    
    return triangle_type