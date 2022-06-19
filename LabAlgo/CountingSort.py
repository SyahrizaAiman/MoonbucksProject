def counting(data):
    # Creates 2D list of size max number in the array
    counts = [0 for i in range(max(data)+1)]
 
    # Finds the "counts" for each individual number
    for value in data:
        counts[value] += 1
 
    # Finds the cumulative sum counts
    for index in range(1, len(counts)):
        counts[index] = counts[index-1] + counts[index]
 
    # Sorting Phase
    arr = [0 for loop in range(len(data))]
    for value in data:
        index = counts[value] - 1
        arr[index] = value
        counts[value] -= 1
 
    return arr
 
 
data = [16, 30, 95, 51, 84, 23, 62, 44]
print(counting(data))
