
a = float(input())
b = float(input())

try: 
    sum = a+b
    print(sum)
except ValueError:
    print('Error')