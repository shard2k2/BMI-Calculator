#this comment is to check how to push to github using git.:ppp
print("=== BMI Calculator ===")

weight = float(input("Enter your weight in kg: "))
height = float(input("Enter your height in meters: "))

bmi = weight / (height ** 2)

if (bmi < 18.5):
    body = "Underweight"
elif (bmi < 25):
    body = "Normal weight"
elif (bmi < 30):
    body = "overweight"
else:
    body = "Obese"

print(f"\nYour BMI is: {bmi:.2f}")
print(f"You are {body}")