"""Activity 1
n = 10
guess = input("Double Loop at n = 10 checks n x n pairs.  How many?  ")
input("Formula: one calculation, done.  Press Enter to run ")
steps = 1
print("  steps =", steps, "  ->  O(1)  constant time  ->  steps never change")

input("Loop: one step per item. Press Enter to run ")
steps = 0
for i in range(n):
    steps += 1
print("  steps =", steps, "  ->  O(n)  linear time  ->  steps grow with n")

input("Double Loop: checks every pair. Press Enter to run ")
steps = 0
for i in range(n):
    for j in range(n):
        steps += 1
print("  steps =", steps, "  your guess:", guess, "  ->  O(n^2)  quadratic time")

input("Two more notations. Press Enter ")
print("  Big Omega  Ω  ->  best case lower bound")
print("  Big Theta  Θ  ->  exact bound  (worst = best)")"""

"""Activity 2
scores = [3, 7, 2, 9, 4, 1, 8, 5, 6]
#          1  2  3  4  5  6  7  8  9

input("List: " + str(scores) + "   n = 9   Linear search — checks left to right.  Press Enter ")

target = int(input("Enter a number to search for: "))

input("Searching for " + str(target) + ".  Press Enter to run ")
steps = 0
for score in scores:
    steps += 1
    if score == target:
        break
print("  target =", target, "  found at position", steps, "  checks =", steps)

input("Compare with best and worst case.  Press Enter ")
mid = len(scores) // 2
print("  Best: 1 check -> O(1)   Average:", mid, "checks -> O(n)   Worst: 9 checks -> O(n)   Yours:", steps)

input("All three cases.  Press Enter ")
print("  Best O(1)  Average O(n)  Worst O(n)   ->   Big-O = worst case = O(n).")"""

"""Activity 3

n = int(input("Enter any n (try 5, 10, or 50): "))

input("One loop — runs once per item.  Press Enter to run ")
for i in range(n):
    pass
print("  n =", n, "  steps =", n, "  ->  O(n)  linear time")

input("Two nested loops — runs n x n times.  Press Enter to run ")
for i in range(n):
    for j in range(n):
        pass
print("  n =", n, "  steps =", n * n, "  ->  O(n^2)  quadratic time")
input("Rule: count the loops. Press Enter")
print("  0 loops -> O(1)   1 loop -> O(n)   2 nested -> O(n^2)")"""