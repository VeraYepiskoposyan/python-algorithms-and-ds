import heapq

def top_k_largest(numbers, k):
    if not numbers or k <= 0:
        return []

    heap = []

    for num in numbers:
        heapq.heappush(heap, num)

        if len(heap) > k:
            heapq.heappop(heap)

    return heap

print(top_k_largest([10, 3, 7, 20, 15, 8, 30], 3))




