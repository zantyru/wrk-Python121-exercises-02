class Queue:

    class EmptyError(Exception):

        def __init__(self, *args, message=None, **kwargs):
            if message is None:
                message = "Queue is empty."
            self.message = message
            super().__init__(self.message, *args)

    def __init__(self):
        self.__body = []

    def enqueue(self, item):
        self.__body.append(item)

    def dequeue(self):
        try:
            item = self.__body.pop(0)
        except IndexError:
            raise Queue.EmptyError()

        return item

    def is_empty(self):
        return not self.__body


if __name__ == '__main__':

    q = Queue()

    q.enqueue("x")
    q.enqueue(34)
    q.enqueue(True)
    q.enqueue(5.6)

    while not q.is_empty():
        item = q.dequeue()
        print(item)
