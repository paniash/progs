# Using bubble sort to sort a given array
# define an array
a = [56,23,76,2,182,9,0]

for j in range(7):
    for i in range(6):
        if a[i] > a[i+1]:
            temp = a[i]
            a[i] = a[i+1]
            a[i+1] = temp
    print("After", j+1, "th sort:", a)

print("Sorted array is", a)
