"""Activity 1
n=4
guess=input("Total points: 1 + 2 + 3 + 4 = ")
input("Formula: one calculation. Press Enter to run")
total=n*(n+1)/2
print("total=", total, "  steps=", 1)

input("Loop: adds one student at a time. Press Enter to run")
total=0
for student in range(1,n+1):
    total+=student
print("total=", total, "  steps=", n)

input("Double loop: adds one student at a time . Press Enter to run")
total=0
steps=0
for student in range(1, n+1):
    for point in range(1, student+1):
        total+=1
        steps+=1
print("total=", total, "  steps=", steps,"your guess was:", guess)"""

""" Activity 2
input("Double Loop at n = 4 took 10 steps.  Watch it grow.  Press Enter ")
for n in [10,100,1000]:
    input("n =" +str(n)+".  Press Enter to run")
    print("steps=", n * (n + 1) // 2)"""

"""Activity 3
n=4
guess=input("Predict: how many items in the list for n=4?")
points=list(range(1,n+1))
print(" your guess:", guess, "List:", points, "items:",len(points))
input(" Predict: what happens to List size ans n grows.  Press Enter to run")
for size in [4,10,100,1000]:
    print(f"n={size:<5} List uses{size:>5} items in memory")"""