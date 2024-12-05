# break
# The break statement is used to exit a loop prematurely, regardless of whether the loop's condition is true or not. When break is encountered within a loop, the loop is terminated immediately, and the program execution continues with the statement immediately following the loop.
for i in range(10):
    if i == 5:
        break
    print(i)
# continue
# The continue statement is used to skip the rest of the code inside the loop for the current iteration and jump to the next iteration of the loop. It does not terminate the loop; instead, it continues with the next iteration
for i in range(5):
    if i == 2:
        continue
    print(i)
# pass
# Example using pass
for i in range(3):
    pass  # No operation is performed

# Output: No output, as pass does nothing

