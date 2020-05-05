# Selection sort of an array
a = [56,23,76,2,182,9,0]   # array to be sorted

# function that finds the position of minimum element in the array
def small(a, i) :
    mini = a[i]
    pos = 0
    for j in range(i, 7):
        if a[j] < mini:
            mini = a[j]
            pos = j
    return mini, pos

# function that sorts
def select(a):
    for k in range(6):
        mini, pos = small(a, k)
        # place element at the beginning and exchange with first element
        tmp = a[k]
        a[k] = mini
        a[pos] = tmp
        print("After", k+1, "th sort:", a)

select(a)
