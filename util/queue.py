'''
@file util/queue.py
@author Caleb Burke
@date 2024-02-15

A simple queue ADT
'''

class Queue:
    def __init__(self):
        self.elements = []

    def enqueue(self, element) -> None:
        """Enqueues element on queue
        
        Parameters
        ----------

        """
        self.elements.append(element)

    def dequeue(self):
        """Dequeues element off queue

        Returns
        -------
        int:
            The size of the Queue
        """
        return self.elements.pop(0)

    def first(self):
        """Returns first element of queue"""
        return self.elements[0]

    def is_empty(self) -> bool:
        """Returns if queue is empty or not
        
        Returns
        -------
        bool:
            If the queue is empty or not
        """
        return True if self.size() <= 0 else False

    def size(self) -> int:
        """Returns size of queue
        
        Returns
        -------
        int:
            The size of the Queue
        """
        return len(self.elements)
    
    def to_string(self) -> str:
        """Creates a string representation of the class

        Returns
        -------
        str:
            String representaion of the class
        """
        _str = f"POS\tVALUE"
        for i, val in enumerate(self.elements):
            _str += f"{i}\t{val}\n"
        return _str
    
    def __str__(self) -> str:
        """Defines a string representation of the class

        Returns
        -------
        str:
            A string that represents the class

        Usage
        -----
        >>> que = Queue()
        >>> print(que)  # prints return of que.__str__
        """
        return to_string()

    def print(self):
        """Prints elements of queue to stdout"""
        print(to_string())

