import datetime

#this comment is to check how to push to github using git.:ppp
def calculate_bmi():
    print("=== BMI Calculator ===")
    while True:
        try:
            weight = float(input("Enter weight in Kg: "))
            if weight <= 0:
                print("Weight must be a positive number! Try again.\n")
                continue
            if weight > 500:
                print("The value is unusually high. Please check again\n")
                continue
            break
        except ValueError:
            print("Invalid input! Please enter a number\n")

    #taking in height with error handling
    while True:
        try:
            height = float(input("Enter height in meters: "))
            if height <= 0:
                print("Weight must be a positive number! Try again.\n")
                continue
            if height > 3:
                print("The value is unusually high. Please check again\n")
                continue
            break
        except ValueError:
            print("Invalid input! Please enter a number\n")

    #calculating the BMI
    bmi = weight / (height ** 2)

    #Conditions to show what value
    if (bmi < 18.5):
        body = "Underweight"
        emoji = "⚠️"
        advice = "Consider consulting a nutritionist to reach a healthy weight"
    elif (bmi < 25):
        body = "Normal weight"
        emoji = "✅"
        advice = "Great Job! Maintain your healthy lifestyle with balanced diet and exercise"
    elif (bmi < 30):
        body = "overweight"
        emoji = "⚠️"
        advice = "Consider regular exercise and a balanced diet. Consult a doctor if needed"
    else:
        body = "Obese"
        emoji = "🚨"
        advice = "Please consult a healthcare provider for a personalized health plan."

    #Printing the output 
    print(f"\nYour BMI is: {bmi:.2f}")
    print(f"Category: {body} {emoji}")
    print(advice)


    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("bmi_history.txt", "a") as file:
        file.write(f"{timestamp} | Weight: {weight}kg | Height: {height}m | BMI: {bmi:.2f} | {body}\n")


    print("\nResult saved to bmi_history.txt")

def view_history():
    """Display BMI Calculation History"""
    print("\n" + "="*60)
    print("         BMI History")
    print("=" * 60)

    try:
        with open("bmi_history.txt", "r") as file:
            lines = file.readlines()

            if lines:
                print(f"\nTotal entries: {len(lines)}\n")
                for i, line in enumerate(lines, 1):
                    print(f"{i}. {line.strip()}")
                print("\n" + "="*60)
            else:
                print("\nNo History Found Yet")
                print("Calculate you BMI first to start tracking.\n")
    except FileNotFoundError:
        print("\n No History Found")
        print("Calculate your BMI first to create history\n")

def main_menu():
    """Main Menu loop"""
    while True:
        print("\n" + "="*40)
        print("     BMI Calculator")
        print("="*40)
        print("1. Calculate BMI")
        print("2. View History")
        print("3. Exit")
        print("=" * 40)

        choice = input("\nChoose an option (1-3): ")

        if choice == "1":
            calculate_bmi()
        elif choice == "2":
            view_history()
        elif choice == "3":
            print("\nGoodbye Stay Healthy")
            break
        else:
            print("Invalid Option Please Choose A Number Between 1 and 3")

if __name__ == "__main__":
    main_menu()