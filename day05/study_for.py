# Day 05
# Examples of study case: for

fruits = ["Apple", "Orange", "Pear", "Banana", "Lemon"]
for fruit in fruits:
    print(fruit)

student_scores = [150, 50, 200, 300, 11, 588, 62, 70, 522, 588, 847]

# First option:

total_exam_score = sum(student_scores)
print(f'First: {total_exam_score}')

# Second option:

total_score = 0
for score in student_scores:
    total_score += score

print(f'Secord: {total_score}')

# Max score:

print(max(student_scores))

# Max score, looping:

max_score = 0
for score in student_scores:
    if score > max_score:
        max_score = score

print(max_score)

# The Gauss Challenge:
# Work out the total of the numbers between 1 and 100, inclusive of both a and 100

total_sum_numbers = 0
for number in range(1, 101):
    total_sum_numbers += number

print(total_sum_numbers)
