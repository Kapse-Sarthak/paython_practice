def classify_triangle(a, b, c):
    # First check validity
    if (a + b <= c) or (a + c <= b) or (b + c <= a):
        return "Invalid Triangle"

    # Classification
    if a == b == c:
        return "Equilateral Triangle (All sides equal)"
    elif a == b or b == c or a == c:
        return "Isosceles Triangle (Two sides equal)"
    else:
        return "Scalene Triangle (All sides different)"


# Main execution
a = float(input("Enter side 1: "))
b = float(input("Enter side 2: "))
c = float(input("Enter side 3: "))

print(classify_triangle(a, b, c))