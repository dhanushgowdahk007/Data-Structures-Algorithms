import heapq
from collections import Counter

heap = []

heapq.heappush(heap, 3)
heapq.heappush(heap, 1)
heapq.heappush(heap, -3)
heapq.heappush(heap, 9)
heapq.heappush(heap, 2)
heapq.heappush(heap, 7)

# print(heap)
# print()

smallest = heapq.heappop(heap)
# print(smallest)
# print(heap)
# print()

# print("peek: ", heap[0])
# print()

nums = [4, 7, 1, 3, 13, 15, -2, 5]
# heapq.heapify(nums)
# print(nums)
# print()

# Heap Sort - Ascending
def heapSort(arr):
    heapq.heapify(arr)
    min_list = [0] * len(arr)

    for i in range(len(arr)):
        minn = heapq.heappop(arr)
        min_list[i] = minn

    return min_list

# nums = heapSort(nums)
# print(nums)
# print()

# Max Heap 
B = [-4, 3, 1, 0, 2, 5, 10, 8, 12, 9]
def maxHeap(arr):
    heap = [-x for x in arr]
    heapq.heapify(heap)

    while heap:
        print(-heapq.heappop(heap), end=" ")

# maxB = maxHeap(B)
# print()

def heapSortDesc(arr):
    heap = [-x for x in arr]
    heapq.heapify(heap)

    ans = []

    while heap:
        ans.append(-heapq.heappop(heap))

    return ans

# sortB = heapSortDesc([-4, 3, 1, 0, 2, 5, 10, 8, 12, 9])
# print(sortB)
# print()
# A = heapSort(B)
# print(A)
# print()
    
D = [5, 4, 3, 5, 4, 3, 5, 5, 4]

counter = Counter(D)
print(counter)

cHeap = []

for key, val in counter.items():
    heapq.heappush(cHeap, (val, key))

print(cHeap)
