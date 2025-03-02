#Task 1: Create a Dictionary of Student Marks

# Initialize the dictionary with some student marks
student_marks = {
    "John": 85,
    "Emma": 92,
    "Michael": 78,
    "Sarah": 95,
    "David": 88
}

# Get student name from user
student_name = input("Enter student's name: ")

# Try to retrieve and display the marks
if student_name in student_marks:
    print(f"{student_name}'s marks: {student_marks[student_name]}")
else:
    print("Student not found")

# Task 2: Demonstrate List Slicing

numbers = list(range(1, 11))
first_five = numbers[:5]

# Reverse the extracted elements
reversed_five = first_five[::-1]

# Print both lists
print("\nOriginal list: ", numbers)
print("Extracted first five elements: ", first_five)
print("Reversed extracted elements: ", reversed_five)
