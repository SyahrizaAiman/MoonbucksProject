# Shell sort in python
 
 
def shellSort(array, n):
 
    # Rearrange elements at each n/2, n/4, n/8, ... intervals
    interval = n // 2
    while interval > 0:
        for i in range(interval, n):
            temp = array[i]
            j = i
            while j >= interval and array[j - interval] > temp:
                array[j] = array[j - interval]
                j -= interval
 
            array[j] = temp
        interval //= 2
 
 
data = [16, 30, 95, 51, 84, 23, 62, 44]
size = len(data)
shellSort(data, size)
print()
print(data)
