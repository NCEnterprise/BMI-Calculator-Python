def calculate_bmi(weight, height):
    """
    Calculate BMI using the weight (in kilograms) and height (in meters) formula.
    Formula: BMI = weight / (height * height)
    """
    bmi = weight / (height ** 2)
    return bmi

def interpret_bmi(bmi):
    """
    Interpret BMI results based on standard categories.
    """
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 25:
        return "Normal Weight"
    elif 25 <= bmi < 30:
        return "Overweight"
    else:
        return "Obese"

def main():
    # Get user input for weight and height
    weight = float(input("Enter your weight in kilograms: "))
    height = float(input("Enter your height in meters: "))

    # Calculate BMI
    bmi_result = calculate_bmi(weight, height)

    # Interpret BMI results
    interpretation = interpret_bmi(bmi_result)

    # Display results
    print(f"\nYour BMI is: {bmi_result:.2f}")
    print(f"Interpretation: {interpretation}")

if __name__ == "__main__":
    main()
