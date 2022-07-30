import cmath


def solve_quadric_equation(a, b, c):
    try:
        d=b*b-4*a*c
        x1=(-b-cmath.sqrt(d))/(2*a)
        x2=(-b+cmath.sqrt(d))/(2*a)
        return f"The solution are x1={x1} and x2={x2}"
    except ZeroDivisionError:
        return "Zero Division Error" 
    except TypeError:
        return "Could not convert string to float"


print(solve_quadric_equation(1, 5, 6))
print(solve_quadric_equation(1, "abc", 6))
print(solve_quadric_equation(0, 8, 1))
print(solve_quadric_equation(1, 3, -4))
print(solve_quadric_equation(1, 4, 5))
print(solve_quadric_equation(0, 5, 9))
print(solve_quadric_equation(0, 5, 9))
