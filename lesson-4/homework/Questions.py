"""
continue: This statement is used to skip the rest of the code in the current iteration
and jump to the next iteration of the loop.
It does not terminate the loop but simply skips the current step.

break: This statement is used to immediately terminate the loop.
The control exits the loop and moves to the next part of the code outside the loop.

The for loop is used when you know the number of iterations or want to iterate over a sequence (like a list, string, or range).
It is typically used when you are working with a fixed collection of items or a predictable range.

while Loop:
The while loop is used when you don’t know the number of iterations in advance,
but you want the loop to run as long as a condition is true.
 It is useful for scenarios where the stopping condition depends on dynamic calculations or inputs.

 A nested for loop is simply a loop inside another loop.
 The inner loop will run completely for every iteration of the outer loop.
 This is commonly used in scenarios like working with matrices or multidimensional data.
"""

# Explanation for continue and break
print("Example of 'continue' and 'break':")
for num in range(5):
    if num == 2:
        continue  # Skip the number 2
    if num == 4:
        break  # Exit loop when num is 4
    print(num)

# Difference between 'for' and 'while'
print("\nExample of 'for' and 'while':")
for i in range(3):  # Known range
    print(f"For loop: {i}")

count = 0
while count < 3:  # Condition-based
    print(f"While loop: {count}")
    count += 1

# Nested for loop example
print("\nExample of nested 'for' loop:")
for i in range(2):
    for j in range(2):
        print(f"Outer: {i}, Inner: {j}")
