def is_valid_triangle(a, b, c):
    # Check the Triangle Inequality Theorem
    if (a + b > c) and (a + c > b) and (b + c > a):
        return True
    return False

# Main execution
a = float(input("Enter side 1: "))
b = float(input("Enter side 2: "))
c = float(input("Enter side 3: "))

if a <= 0 or b <= 0 or c <= 0:
    print("❌ Side lengths must be positive numbers.")
elif is_valid_triangle(a, b, c):
    print("✅ These sides form a VALID triangle.")
else:
    print("❌ These sides DO NOT form a valid triangle.")