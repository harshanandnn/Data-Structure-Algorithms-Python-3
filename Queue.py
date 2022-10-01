class Queue():
    '''
    Queue Datatype
    '''
    
    def __init__(self, n):
        '''
        Creates a Queue for n elements
        Empty spaces denoted by '?'
        enq_position is the position where the element will be added
        deq_position is the position from where the element will be removed
        '''
        self.n = n
        self.queue = ['?'] * self.n
        self.enq_position = 0
        self.deq_position = 0
    
    def enqueue(self, x):
        '''
        Adds an element 'x' at the ending of the Queue
        '''
        if self.enq_position == self.n:
            print('Reset/Dequeue the Queue to Enqueue.')
            return None
        self.queue[self.enq_position] = x
        self.enq_position += 1
        return self.queue
    
    def dequeue(self):
        '''
        Removes the first element from the Queue.
        '''
        if self.deq_position == self.enq_position:
            print('Queue is empty.')
            return None
        self.queue[self.deq_position] = '?'
        self.deq_position += 1
        if self.deq_position == self.n:
            self.enq_position = 0
            self.deq_position = 0
        return self.queue
    
    def isEmpty(self):
        '''
        Return whether the Queue is empty or not.
        '''
        return self.enq_position == self.deq_position
    
    def isFull(self):
        '''
        Return whether the Queue is full or not.
        '''
        return self.deq_position == 0 and self.enq_position == self.n
    
    def peek(self):
        '''
        Return the first element of the Queue.
        '''
        if self.deq_position != self.enq_position:
            return self.queue[self.deq_position]
        print('Queue is empty.')
        return None