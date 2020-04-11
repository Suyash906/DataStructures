import heapq
def kthSmallest(arr, n, k):
	arr.sort()
	return arr[k-1]

def kthSmallestHeap(arr, n, k):
    heapq.heapify(arr)
    while k !=0:
        res = heapq.heappop(arr)
        k -= 1
    return res

if __name__=='__main__': 
    arr = [12, 3, 5, 7, 19] 
    n = len(arr)
    k = 2
    print("K'th smallest element is", kthSmallest(arr, n, k))

    print("K'th smallest element is", kthSmallestHeap(arr, n, k))