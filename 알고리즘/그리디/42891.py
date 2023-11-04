import heapq

def solution(food_times, k):

    if sum(food_times) <= k:
        return -1
    
    heap = []
    
    for i in range(len(food_times)):
        heapq.heappush(heap, (food_times[i], i+1))
        
    count = len(food_times) # 남은 음식 개수
    sum_times = 0
    prev = 0
    
    while sum_times + ((heap[0][0] - prev)* count) <= k:
        now = heapq.heappop(heap)[0]
        sum_times += (now - prev) * count
        count -= 1
        prev = now
        
    heap.sort(key=lambda x: x[1])
    answer = heap[(k-sum_times)%count][1]
    
    return answer
