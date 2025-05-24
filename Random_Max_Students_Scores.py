import random

# Get the number of students from the user, with input validation
while True:
    user_input = input("How many students? ")
    try:
        num_of_students = int(user_input)
        if num_of_students > 0:
            break
        else:
            print("Please enter a number greater than 0.")
    except ValueError:
        print("Please enter an integer only.")

# Generate a list of random scores between 50 and 100 for each student
student_scores = [random.randint(50, 100) for _ in range(num_of_students)]

# Find the highest score
max_score = max(student_scores)

# Find all students who received the highest score
top_students = [i+1 for i, score in enumerate(student_scores) if score == max_score]

# Print the results
print(f"The highest score is: {max_score}")
print(f"It belongs to student(s) number: {top_students}")
