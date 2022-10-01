class CircularQueue():
    '''
    Circular Queue Datatype
    '''
    
    def __init__(self, n):
        '''
        Creates a Queue for n elements
        Empty spaces denoted by '?'
        Tracker keeps the check whether the Dequeueing position is before Enqueueing poistion or not
        enq_position is the position where the element will be added
        deq_position is the position from where the element will be removed
        '''
        self.n = n
        self.cir_queue = ['?'] * self.n
        self.tracker = 0
        self.enq_position = 0
        self.deq_position = 0
    
    def enqueue(self, x):
        '''
        Adds an element 'x' in the Circular Queue
        '''
        if self.tracker == 0:
            self.cir_queue[self.enq_position] = x
            self.enq_position += 1
            if self.enq_position == self.n:
                self.enq_position -= self.n
                self.tracker = 1
            return self.cir_queue
        if self.enq_position == self.deq_position:
            print('Circular Queue is full')
            return self.cir_queue
        else:
            self.cir_queue[self.enq_position] = x
            self.enq_position += 1
            return self.cir_queue
    
    def dequeue(self):
        '''
        Removes the earliest entry from the Queue
        '''
        if self.tracker == 0 and self.enq_position == self.deq_position:
            print('Circular Queue is empty')
            return None
        self.cir_queue[self.deq_position] = '?'
        self.deq_position += 1
        if self.deq_position ==self.n:
            self.deq_position -= self.n
            self.tracker = 0
        return self.cir_queue
    
    def isEmpty(self):
        '''
        Returns whether the Circular Queue is empty or not
        '''
        return self.tracker == 0 and self.enq_position == self.deq_position
    
    def isFull(self):
        '''
        Returns whether the Circular Queue is full or not
        '''
        return self.tracker == 1 and self.enq_position == self.deq_position
    
    def peek(self):
        '''
        Returns the earliest entry in the Circular Queue
        '''
        if self.isEmpty():
            print('Circular Queue is empty')
            return None
        else:
            return self.cir_queue[self.deq_position]