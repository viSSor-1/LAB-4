
def chetv():
    try:
        x = float(input("X: "))
        y = float(input("Y: "))
        
        if x > 0 and y > 0:
            c = "1 coordinate quadrant"
        elif x < 0 and y > 0:
           с ="2 coordinate quadrant"
        elif x < 0 and y < 0:
            с ="3 coordinate quadrant"
        elif x > 0 and y < 0:
            с="4 coordinate quadrant"
        elif x == 0 and y != 0:
            с="Y-axis"
        elif x != 0 and y == 0:
            c="X-axis"
        else:
            c="origin of coordinates"
        print(f'Your coordinate quadrant is {c}')
           
    except ValueError:
        print("Error ")

chetv()
