def calculate_runoff(length_feet, width_feet, rainfall_inches):
    gallons_per_cubic_foot = 7.48
    inches_to_feet = 12
    
    area_square_feet = length_feet * width_feet
    rainfall_feet = rainfall_inches / inches_to_feet
    
    runoff_gallons = (area_square_feet * rainfall_feet) * gallons_per_cubic_foot
    return runoff_gallons

def main():
    length = float(input("Enter the length of the surface in feet: "))
    width = float(input("Enter the width of the surface in feet: "))
    rainfall = float(input("Enter the amount of rainfall in inches: "))

    runoff = calculate_runoff(length, width, rainfall)
    print(f"The runoff in gallons is: {runoff:.2f} gallons")

if __name__ == "__main__":
    main()