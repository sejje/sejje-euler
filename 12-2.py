from eulertools import factorize as factors

def first_triangle_with_divisors(num):
    '''
    Find the first triangle number with
    at least num number of divisors
    '''
    count = 1
    triangle = 1
    factor_count = 0
    while factor_count < num:
        count += 1
        triangle += count
        if num < 100 or num > 100 and not triangle % 2 and not triangle % 3:
            factor_count = len(factors(triangle))
    return (triangle, factor_count)


print first_triangle_with_divisors(1)
print first_triangle_with_divisors(6)
print first_triangle_with_divisors(30)
print first_triangle_with_divisors(55)
print first_triangle_with_divisors(500)



