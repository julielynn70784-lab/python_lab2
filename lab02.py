import math

# Part 1: Variables
name = "Your Name"
age = 20
height = 5.7
favorite_color = "Blue"

# 1. Print one variable at a time
print(name)
print(age)
print(height)
print(favorite_color)

# 2. Print with commas (yes, Python adds a space between each one)
print(name, age, height, favorite_color)

# 3. Print with f-strings and format specifiers
print(f"Hello: {name} my favorite color is {favorite_color}!")
print(f"Age: {age:d}")
print(f"Height: {height:f}")
print(f"Height to 1 decimal: {height:.1f}")

# 4. Multi-line string with all four variables
print(f"""
Name: {name}
Age: {age}
Height: {height}
Favorite Color: {favorite_color}
""")

# Test: extra spaces at the start of lines show up in the output
print(f"""
    Name: {name}
        Age: {age}
""")

# Circle area (radius 5), printed to ONLY 1 decimal place
radius = 5
circle_area = math.pi * radius ** 2
print(f"Circle area: {circle_area:.1f}")
# Part 2: math module
print(f"Square root of age: {math.sqrt(age):.2f}")
print(f"Sine of height: {math.sin(height):.4f}")
print(f"Cosine of height: {math.cos(height):.4f}")
# Part 3: Arithmetic
print(f"Sum of age and 5: {age + 5}")
print(f"Difference of height and 4: {height - 4:.1f}")
print(f"Product of age and height: {age * height:.1f}")
print(f"Quotient of height and 2: {height / 2:.2f}")
print(f"Remainder of age divided by 3: {age % 3}")
print(f"Age squared: {age ** 2}")
# Part 4: Fahrenheit to Celsius
fahrenheit = float(input("Enter a temperature in Fahrenheit: "))
celsius = (fahrenheit - 32) * 5 / 9
print(f"{fahrenheit}°F is {celsius:.1f}°C")