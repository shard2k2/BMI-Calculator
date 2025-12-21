#this comment is to check how to push to github using git.:ppp
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

bmi = weight / (height ** 2)

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

print(f"\nYour BMI is: {bmi:.2f}")
print(f"Category: {body} {emoji}")
print(advice)