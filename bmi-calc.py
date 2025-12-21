#this comment is to check how to push to github using git.:ppp
print("=== BMI Calculator ===")

weight = float(input("Enter your weight in kg: "))
height = float(input("Enter your height in meters: "))

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