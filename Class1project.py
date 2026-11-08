
n = 5
formula_total = n * (n + 1) // 2

print("Solution 1: Formula Method")
print("Total Running Points:", formula_total)
print()

loop_total = 0
steps_loop = 0

for lap in range(1, n + 1):
    loop_total = loop_total + lap
    steps_loop = steps_loop + 1

print("Solution 2: Loop Method")
print("Total Running Points:", loop_total)
print("Steps Taken:", steps_loop)
print()


double_loop_total = 0
steps_double_loop = 0

for lap in range(1, n + 1):
    for point in range(1, lap + 1):
        double_loop_total = double_loop_total + 1
        steps_double_loop = steps_double_loop + 1

print("Solution 3: Double Loop Method")
print("Total Running Points:", double_loop_total)
print("Steps Taken:", steps_double_loop)
print()
