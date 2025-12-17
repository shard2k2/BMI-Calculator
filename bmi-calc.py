#this comment is to check how to push to github using git.:ppp
print("=== BMI Calculator ===")

weight = float(input("Enter your weight in kg: "))
height = float(input("Enter your height in meters: "))

bmi = weight / (height ** 2)

print(f"\nYour BMI is: {bmi:.2f}")