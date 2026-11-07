
def calc():
    try:
        weight = float(input("Enter your weight: "))
        height = float(input("Enter your height in metres: "))
        
        if weight <= 0 or height <= 0:
            print("Error")
            return
            
        imt = weight / (height ** 2)
        print(f"Your IMT: {imt:.2f}")
        
        if imt < 18.5:
            c = "underweight"
        elif imt < 25:
            c = "normal weight"
        elif imt < 30:
            c = "overweight"
        else:
            c = "obesity"
            
        print(f"You have a/an: {c}")
        
    except ValueError:
        print("Error. It's not a digit")

calc()
