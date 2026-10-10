marks = []

for i in range(5):
    while True:
        try:
            mark = int(input(f"Enter marks for student {i + 1} (0-100): "))
            if 0 <= mark <= 100:
                marks.append(mark)
                break
            else:
                print("Please enter marks between 0 and 100.")
        except ValueError:
            print("Please enter a valid whole number.")

total = sum(marks)
average = total / len(marks)
highest = max(marks)
lowest = min(marks)

print("\n--- Student Marks Analysis ---")
print("Student Marks:", marks)
print("Total Marks:", total)
print("Average Marks:", average)
print("Highest Marks:", highest)
print("Lowest Marks:", lowest)
