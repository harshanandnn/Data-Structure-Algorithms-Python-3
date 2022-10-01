class Stack():
    '''
    Stack Datatype
    '''
    
    def __init__(self, n):
        '''
        Creates a Stack for n elements
        Empty spaces are denoted by '?'
        n_count is the index where the element will be inserted
        '''
        self.n = n
        self.stack = ['?'] * self.n
        self.n_count = -1
    
    def push(self, x):
        '''
        Adds an element 'x' at the very last Non-empty space
        '''
        if self.stack[0] != '?':
            print('Stack is full.')
            return None
        self.stack[self.n_count] = x
        self.n_count -= 1
        return self.stack
    
    def pop(self):
        '''
        Removes the recent added element
        '''
        if self.n_count == -1:
            print('Stack is empty.')
            return None
        self.stack[self.n_count + 1] = '?'
        self.n_count += 1
        return self.stack
    
    def isEmpty(self):
        '''
        Returns whether the stack is empty or not.
        '''
        return self.n_count == -1
    
    def isFull(self):
        '''
        Returns whether the stack is full or not.
        '''
        return self.stack[0] != '?'
    
    def peek(self):
        '''
        Returns the recently added element.
        '''
        if self.n_count == -1:
            print('Stack is empty.')
            return None
        return self.stack[self.n_count + 1]