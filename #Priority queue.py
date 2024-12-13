#Priority queue
#In priority queue each value has a certain priority, and is popped based on its priority
#Higher priority is dequeued first compared to the one with lower priority
class priority_queue(object):
    def __init__(self):
        self.queue = []
    
    def __str__(self):
        return ' '.join([str(i) for i in self.queue])
    
    def isEmpty(self):
        return len(self.queue) == 0
    
    def insert(self,data):
        self.queue.append(data)

    def delete(self):
        try:
            max = 0
            for i in range(len(self.queue)):
                if self.queue[i] > self.queue[max]:
                    max = i
            item = self.queue[max]
            del self.queue[max]
            return item
        except IndexError:
            print()
            exit()

if __name__ == '__main__':
    q = priority_queue()
    q.insert(1)
    q.insert(13)
    q.insert(19)
    q.insert(2)
    q.insert(14)
    print(q)

    while not q.isEmpty():
        print(q.delete)
    
    



    