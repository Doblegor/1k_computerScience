import math


def smaller_root(a, b, c):
    equation = str(a) + 'x^2 ' + ' + ' + str(b) + 'x ' + ' + ' + str(c)
    discriminant = b**2 - 4*a*b*c
    if discriminant == 0:
        return \
        'The smaller root of ' + equation + ' is:\n' + \
        'One real solution\n' + \
        '0.0' + '\n'
    
    elif discriminant < 0:
        return \
        'The smaller root of ' + equation + ' is:\n' + \
        'Error: no real solution\n' + \
        'None' + '\n'
    
    else:
        quadratic_equation = -b - math.sqrt(-b**2 - (-4*a*c))/(2*a)
        return \
        'The smaller root of ' + equation + ' is:\n' + \
        str(quadratic_equation) + '\n'


def main():
    print(smaller_root(1, 2, 3))
    print(smaller_root(2, 0, -10))
    print(smaller_root(6, -3, 5))
    print(smaller_root(1, 0, 0))

    input('\nComputer Science I    Lab: Quadratic    Cypress Ranch High School')


if __name__ == '__main__':
    main()

