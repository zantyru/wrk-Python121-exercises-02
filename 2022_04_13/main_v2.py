class EmptyQueueError(Exception):
    pass


class Node:
    def __init__(self):
        self.data = None
        self.next = None


class Queue:

    def __init__(self):
        self.__head = None
        self.__tail = None

    def enqueue(self, item):
        # Настраиваем "голову"
        if self.__head is None:
            self.__head = Node()
            self.__head.data = item

        # Настраиваем "хвост"
        if self.__tail is None:
            self.__tail = self.__head
        else:
            prev_node = self.__tail
            self.__tail = Node()
            self.__tail.data = item
            prev_node.next = self.__tail

    def dequeue(self):
        # Настраиваем "голову"
        if self.__head is None:
            raise EmptyQueueError("Queue is empty.")
        else:
            node = self.__head
            self.__head = node.next
            item = node.data

        # Настраиваем "хвост"
        if self.__tail is node:
            self.__tail = None

        del node

        return item

    def is_empty(self):
        return self.__head is None


if __name__ == '__main__':

    q = Queue()

    q.enqueue("x")
    q.enqueue(34)
    q.enqueue(True)
    q.enqueue(5.6)

    while not q.is_empty():
        item = q.dequeue()
        print(item)

    try:
        _ = q.dequeue()
    except EmptyQueueError:
        print("А очередь пуста!")