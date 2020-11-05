def main():
    def larger_abs_val(a, b):
        a = abs(a)
        b = abs(b)
        if a > b:
            return True
        else:
            return False

    a = int(input('number for a: '))
    b = int(input('number for b: '))
    larger_abs_val(a, b)
    if  larger_abs_val(a, b):
        print(a)
    else:
        print(b)
    input()
        
        
if __name__ == '__main__':
    main()
