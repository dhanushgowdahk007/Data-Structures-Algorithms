# https://leetcode.com/problems/kth-largest-element-in-an-array/

import heapq

def kthLargest(arr, k):
    heap = [-x for x in arr]
    heapq.heapify(heap)

    for _ in range(k-1):
        heapq.heappop(heap)

    return -heapq.heappop(heap)

# Example usage 
nums = [3,2,1,5,6,4]
k = 2
res = kthLargest(nums, k)

print(res)

# Time Complexity : O(n + klogn) O(n) for negating elements, O(n) for heapify(), and k heap pops so, O(klogn)
# Space Complexity: O(n) Extra heap of size n