#Given an array of intervals [startTime, endTime], merge all overlapping intervals and return a sorted array of non-overlapping intervals.
# intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
# output[[1, 6], [8, 10], [15, 18]]

def is_overlapping(arr1, arr2):
    if arr2 is None or arr1 is None:
        return False
    min1 = arr1[0]
    print(arr1[0], arr2)
    max1 = arr1[1]    
    min2 = arr2[0]
    max2 = arr2[1]    
    if max2 <= max1 and max2 >= min1:
        return True
        
def perform_merge(arr1, arr2):
     if is_overlapping == True:
        min1 = arr1[0]
        max1 = arr1[1]
        min2 = arr2[0]
        max2 = arr2[1] 
        first = min(min1, min2)
        second = max(max1, max2)
        return [first, second]


def merge_intervals():
    sort_needed = True
    intervals = [[1,3],[2,6],[8,10],[15,18], [5,6]]
    print(intervals)
    print(type(intervals))
    sorted_intervals1 = sorted(intervals)
    print(sorted_intervals1)
    
    while sort_needed:
        for i in range(len(sorted_intervals1)-1):
            if is_overlapping(sorted_intervals1[i], sorted_intervals1[i+1]):
                print("overlapping")
                merged = perform_merge(sorted_intervals1[i], sorted_intervals1[i+1])
                sorted_intervals1[i] = merged
                del sorted_intervals1[i+1]
                break
        else:
            sort_needed = False
    print(sorted_intervals1)

    
if __name__ == "__main__":
    merge_intervals()