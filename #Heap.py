#Heap
import heapq
l = [15,13,6,54,21]
print(l)
#Converting the list to a heap
heapq.heapify(l)
print(list(l))
#Adding an element to the heap 
heapq.heappush(l,3)
print("After Inserting element")
print(l)
#Popping elements from the heap
print(heapq.heappop(l))
print(heapq.heappop(l))
print(l)